#include <cstring>
#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;

int main(){
	int cas;
//	scanf("%d",&cas);
	cin >> cas;
	int idx = 0;
	while(cas--){idx++;
		//char bf[32];
		///memset(bf,0,sizeof bf);
		//scanf("%s",bf);
		string s; cin >> s;string cp = s;
		int sz = s.size();
		if(next_permutation(s.begin(),s.end())){
			printf("Case #%d: %s\n",idx,s.c_str());
			continue;
		}
		//we have to add a zero
		string s2 = "0"+cp;
		//for(int i=sz;i>=1;i--)bf[i]=bf[i-1];
		//bf[0]='0';sz++;
		//cout << s2 << endl;
		int ans = next_permutation(s2.begin(),s2.end());
		printf("Case #%d: %s\n",idx,s2.c_str());
	}
	return 0;
}
