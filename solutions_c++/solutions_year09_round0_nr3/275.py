#define MD(x) if (1) {x;}
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

char s[] = "welcome to code jam";
char t[1<<10];
int d[20];

int main(){
	int tc;
	scanf("%d\n",&tc);
	for (int ti=1; ti<=tc; ti++){
		gets(t);
		memset(d,0,sizeof(d));
		for (int i=0; t[i]; i++){
			for (int j=18; j>=0; j--){
				if (t[i]==s[j]){
					if (j==0) d[j]++;
					else d[j]+=d[j-1];
					d[j]%=10000;
				}				
			}
		}
		printf("Case #%d: %04d\n",ti,d[18]);
	}
	return 0;
}
