#include<iostream>
#include<string.h>
using namespace std;

char v[21]="1welcome to code jam";

long n;
char str[501];
long state[21];

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	long i,j,z;
	scanf("%ld",&n);
	str[0]='1';
	for(z=1;z<=n;z++){
		while(getchar()!='\n');
		scanf("%[^\n]",&str[1]);
		memset(state,0,sizeof(state));
		state[0]=1;
		for(i=1;i<strlen(str);i++){
			for(j=1;j<21;j++)
				if(str[i]==v[j])
					state[j]=(state[j]+state[j-1])%10000;
		}
		printf("Case #%ld: %04ld\n",z,state[19]%10000);
	}
	return 0;
}