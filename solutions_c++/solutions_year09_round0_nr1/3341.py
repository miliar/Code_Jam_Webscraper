#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

int main(){
	int l,m,n;
	string word[1000],cas[1000];
	int sum[1000];
	scanf("%d %d %d",&l,&m,&n);
	for (int i=0;i<m;++i)
		cin >> word[i];
	for (int i=0;i<n;++i)
		cin >> cas[i];
	
	for (int i=0;i<n;++i){
		string tmp[300];
		int c=0;
		for (unsigned int j=0;j<cas[i].size();){
			if (cas[i][j]=='('){
				j++;
				for (int k=j;cas[i][k]!=')';++k){
					tmp[c]+=cas[i][k];
					j++;
				}
				j++;
				c++;
			}
			else {
				tmp[c]+=cas[i][j];
				c++; j++;
			}
		}
		
		for (int j=0;j<m;++j){
			bool truth=true;
			for (int k=0;k<l;++k){
				for (unsigned int l=0;l<tmp[k].size();++l){
					if (tmp[k][l]==word[j][k]) {
						truth=true;
						break;
					}
					else truth=false;
				}
				if (!truth) break;
			}
			if (truth) sum[i]++;
		}
	}
	
	for (int i=0;i<n;++i)
		printf("Case #%d: %d\n",i+1,sum[i]);
	return 0;
}
