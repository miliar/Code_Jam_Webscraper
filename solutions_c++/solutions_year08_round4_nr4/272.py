
#include <iostream>
#include <vector>
typedef long long LL;
using namespace std;

int main(void){
	int cases;
	cin >> cases;
	for(int case_no=1; case_no<=cases; case_no++){
		int k;
		string s;
		cin >> k >> s;
		vector<int> perm;
		for(int i=0; i<k; i++)
			perm.push_back(i);
		int ans = s.size();
		do{
			string s2 = s;
			for(int i=0; i<s.size()/k; i++)
				for(int j=0; j<k; j++)
					s2[i*k + j] = s[i*k + perm[j]];
			int score = s.size();
			for(int i=1; i<s2.size(); i++)
				if(s2[i-1] == s2[i])
					score--;
			ans = min(ans, score);
		}while(next_permutation(perm.begin(), perm.end()));
		cout << "Case #"<<case_no<<": " << ans << endl;
	}
	return 0;
}
