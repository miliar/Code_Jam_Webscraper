#include <cstdio>
#include <queue>
#include <cmath>
#include <string>
#include <map>

using namespace std;

int main()
{
	int N, ccN, C;
	scanf("%d", &ccN);
	for(int cc=0;cc < ccN;cc++) {
		map<string, char> combine;
		string conflect[26];
		scanf("%d", &C);
		for(int i=0;i<C;i++) {
			char a[3], b;
			scanf(" %2s%c ", a, &b);
			if(a[0] > a[1]) {
				char t;
				t = a[0];
				a[0] = a[1];
				a[1] = t;
			}
			combine[string(a)] = b;

		}
		scanf("%d", &C);
		for(int i=0;i<C;i++) {
			char a, b;
			scanf(" %c%c ", &a, &b);
			conflect[a-'A'] += b;
			conflect[b-'A'] += a;
		}
		vector<char> ele;
		scanf("%d", &N);
		for(int i=0;i<N;i++) {
			char a;
			scanf(" %c ", &a);
			if(ele.empty())
				ele.push_back(a);
			else {
				char b[3] = {0};
				b[0] = a;
				b[1] = ele[ele.size()-1];
				if(b[0] > b[1]) {
					char t;
					t = b[0];
					b[0] = b[1];
					b[1] = t;
				}
				if(combine.find(string(b)) != combine.end()) {
					ele[ele.size()-1] = combine[string(b)];
					continue;
				}
				for(int j=0;j<ele.size();j++) {
					if(conflect[a-'A'].find(ele[j]) != string::npos) {
						ele.clear();
						break;
					}
				}
				if(ele.size() != 0)
					ele.push_back(a);
			}
		}
		printf("Case #%d: ", cc+1);
		if(ele.size() == 0)
			printf("[]");
		else {
			printf("[%c", ele[0]);
			for(int i=1;i<ele.size();i++)
				printf(", %c", ele[i]);
			printf("]");
		}
		printf("\n");
	}
	return 0;
}
