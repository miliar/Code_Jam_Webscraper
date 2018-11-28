#include<cstdio>
#include<cstring>

#include<map>
#include<algorithm>

using namespace std;

char c[5002][17];
char s[1000];
long long ma[100];
int nma;

int main(){
	int l,d,n;
	scanf("%d%d%d",&l,&d,&n);
	for(int i=0;i<d;i++){
		scanf("%s", c[i]);
	}
	
	for(int i=0;i<n;i++){
		int ci = 0;
		scanf("%s", s);
		memset(ma,0,sizeof(ma));
		nma = 0;
		
		//printf("%s\n",s);
		for(int j=0; s[j]!='\0'; j++){
			if(s[j]=='('){
				ci=1;
			}else if(s[j]==')'){
				ci = 0;
				nma++;
			}else{
				ma[nma] |= (1LL<<(s[j]-'a'));
				//printf(" eat %c\n",s[j]);
				if(!ci)nma++;
			}
		}
		int ans = 0;
		int k;
		for(int j=0;j<d;j++){
			for(k=0;k<l;k++){
				if((ma[k] | (1LL<<(c[j][k]-'a')))!= ma[k]){
					//printf("  %d - %d: %c %d %d\n",j,k,c[j][k],(ma[k] | (1LL<<(c[j][k]-'a'))),ma[k]);
					break;
				}
			}
			if(k==l)ans++;
		}
		
		printf("Case #%d: %d\n", i+1, ans);
	}
		
	return 0;
}
