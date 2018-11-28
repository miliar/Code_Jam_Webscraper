/*
 * GCJ_R1_B.cpp
 *
 *  Created on: 2009-9-13
 *      Author: yaoman
 */

#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int main(){
	int t,k;
	bool b,plus;
	char s[30],ss[30];
	freopen("B-small-attempt4.in","r",stdin);
	freopen("ans.out","w",stdout);
	scanf("%d",&t);
	for (k=1; k<=t; k++){
		scanf("%s",s);
		plus = false;
		while (b=next_permutation(s,s+strlen(s)),s[0]=='0'){
			if (!b) plus = true;
		}
		memcpy(ss,s,sizeof(s));
		if (!b || plus){
			memcpy(s+2,ss+1,strlen(s));
			s[1] = '0';
		}
		printf("Case #%d: %s\n",k,s);
	}
	return 0;
}
