#include <cstdio>
#include <cstdlib>
#include <utility>
#include <sstream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>

using namespace std;

const int LARGE = (1 << 30);

inline string rotr(const string &S)
{
	string R = "";
	R += S[S.length()-1];
	R += S.substr(0,S.length()-1);
	return R;
}

int main(int argc, char *argv[])
{
	int T, A, B;
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		scanf("%d %d", &A, &B);
		multimap<int,int> ms; ms.clear();
		set<int> s; s.clear();
		int count = 0;
		for (int i = A; i <= B; i++) {
			ostringstream out;
			out << i;
			string S = out.str();
#if 0	
			int mn = LARGE, mn_k;
			for (int k = 0; k < (int)S.length(); k++) {
				int digit = S[k] - '0';
				if (digit <= mn) { 
					mn = digit;
					mn_k = k;
				}
			}
			string S2 = S.substr(mn_k) + S.substr(0,mn_k);
#endif
			vector<string> V; V.clear();
			V.push_back(S);
			for (int k = 1; k < (int)S.length(); k++) {
				V.push_back(rotr(V[k-1]));
			}
			stable_sort(V.begin(), V.end());
			string S2 = V[0];
			int j;
			for (j = 0; (j < (int)S2.length()) && (S2[j] == '0'); j++);
			int key = atoi(S2.substr(j).c_str());
			ms.insert(make_pair(key,i));
			s.insert(key);
		}
		for (set<int>::iterator itr = s.begin(); itr != s.end() ; ++itr) {
			int c = int(ms.count(*itr));
			count = count + (c * (c-1) / 2 );
#if 0
			printf("%d : %d ::", int(*itr), int(ms.count(*itr)));
			pair<multimap<int,int>::iterator, multimap<int,int>::iterator> P = ms.equal_range(*itr);
			for (multimap<int,int>::iterator itr2 = P.first; itr2 != P.second ; ++itr2)
				printf("%d ", itr2->second);
			printf("\n");
#endif
		}
		printf("Case #%d: %d\n", t+1, count); 
	}

	return 0;
}
