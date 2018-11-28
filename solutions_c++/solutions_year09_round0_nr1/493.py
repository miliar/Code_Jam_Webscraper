/*
 * GCJ_A.cpp
 *
 *  Created on: 2009-9-3
 *      Author: yaoman
 */

#include <iostream>
#include <cstring>
#include <string>
using namespace std;

char s[5001][20];
string str;
bool b[20][27];

void decode(){
	int t,k,i;
	t = 0; k = 0;
	for (i=0; i<(int)str.size(); i++){
		if (str[i]=='('){
			t++;
			continue;
		}
		if (str[i]==')'){
			t--;
			if (t==0) k++;
			continue;
		}
		b[k][str[i]-'a'] = true;
		if (t==0) k++;
	}
}

int main(){
	int L,D,N,i,j,k,ans;
//	freopen("A-large.in","r",stdin);
//	freopen("ans.out","w",stdout);
	scanf("%d%d%d",&L,&D,&N);
	for (i=0; i<D; i++){
		scanf("%s",s[i]);
	}
	for (i=0; i<N; i++){
		cin>>str;
		memset(b,false,sizeof(b));
		decode();
		ans = 0;
		for (j=0; j<D; j++){
			for (k=0; k<L; k++){
				if (!b[k][s[j][k]-'a']) break;
			}
			if (k==L) ans++;
		}
		printf("Case #%d: %d\n",i+1,ans);
	}
	return 0;
}
