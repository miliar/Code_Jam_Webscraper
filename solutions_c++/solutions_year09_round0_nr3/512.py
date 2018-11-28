/*
 * GCJ_C.cpp
 *
 *  Created on: 2009-9-3
 *      Author: yaoman
 */

#include <iostream>
#include <cstring>
#include <string>
using namespace std;

string s0 = "welcome to code jam";
int f[19];

int main(){
	int t,i,j,k;
	string s;
	freopen("C-large.in","r",stdin);
	freopen("ans.out","w",stdout);
	scanf("%d",&t);
	for (i=0; i<t; i++){
		while (getline(cin,s), s=="") ;
		memset(f,0,sizeof(f));
		for (j=0; j<(int)s.size(); j++){
			if (s[j]=='w'){
				f[0]++;
				f[0] %= 10000;
				continue;
			}
			for (k=0; k<(int)s0.size(); k++){
				if (s[j]==s0[k]){
					f[k] += f[k-1];
					f[k] %= 10000;
				}
			}
		}
		printf("Case #%d: %04d\n",i+1,f[18]%10000);
	}
	return 0;
}
