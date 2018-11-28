#include<iostream>
#include<string.h>
using namespace std;

long t;
bool z[40];
bool us[40];
long x[40];

int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	long h,i,k,n;
	__int64 j;
	char st[100];
	scanf("%ld",&t);
	for(h=1;h<=t;h++){
		scanf("%s",st);
		n=0;memset(z,0,sizeof(z));memset(us,0,sizeof(us));
		for(i=0;i<40;i++)
			x[i]=-1;
		for(i=0;i<strlen(st);i++)
			if(st[i]>='0' && st[i]<='9' && z[st[i]-'0']==0){
				z[st[i]-'0']=1;
				n++;
			}else if(st[i]>='a' && st[i]<='z' && z[st[i]-'a'+10]==0){
				z[st[i]-'a'+10]=1;
				n++;
			}
		if(n==1)n=2;
		;k=0;
		if(st[0]>='0' && st[0]<='9'){
			x[st[0]-'0']=1;
		}else if(st[0]>='a' && st[0]<='z'){
			x[st[0]-'a'+10]=1;
		}
		j=1;		
		us[1]=1;
		for(i=1;i<strlen(st);i++){
			j*=n;
			if(st[i]>='0' && st[i]<='9'){
				if(x[st[i]-'0']==-1){
					while(us[k])k++;
					x[st[i]-'0']=k;
					us[k]=1;
				}
				j+=x[st[i]-'0'];
			}else if(st[i]>='a' && st[i]<='z'){
				if(x[st[i]-'a'+10]==-1){
					while(us[k])k++;
					x[st[i]-'a'+10]=k;
					us[k]=1;
				}
				j+=x[st[i]-'a'+10];
			}
		}
		printf("Case #%ld: %I64d\n",h,j);
	}
	return 0;
}