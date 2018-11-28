#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <iostream>
#include <queue>
using namespace std;
int tc;
char s[100];
int main(){
	scanf("%d",&tc);
	for (int c=1;c<=tc;c++){
		scanf("%s",s);
		int type=0;
		int n=strlen(s),p[100];
		p[0]=1;
		for (int i=1;i<n;i++) p[i]=-1;
		for (int i=1;i<n;i++){
			bool ap=1;
			for (int j=0;j<i;j++)
				if (s[i]==s[j]){
					ap=0;
					if (p[j]!=-1) p[i]=p[j];
				}
			if (ap) p[i]=type++;
			if (type==1) type++;
		}
		if (type<2) type=2;
		long long k=1,AC=0;
		for (int i=n-1;i>=0;i--){
			AC+=p[i]*k;
			k*=type;
		}
		printf("Case #%d: %lld\n",c,AC);
	}
}
