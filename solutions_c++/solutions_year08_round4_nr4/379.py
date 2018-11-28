#include<cstdio>
#include<cmath>
#include<algorithm>
#include<cstdlib>
#include<vector>
#include<queue>
#include<cstring>
using namespace std;

typedef long long LL;

#define FT first
#define SD second
#define MP make_pair
#define PB push_back

int T;
int tab[10];
char s[1006];
char stmp[1006];
int ca,k,co,res;

int main(){
	ca=0;
	scanf("%d",&T);
	while(T--){
		ca++;
		scanf("%d",&k);
		scanf("%s",s);
		int n = strlen(s);
		res=n+100;
		for(int i=1;i<=k;i++){
			tab[i-1]=i;
		}
		do{
			/*for(int i=0;i<k;i++){
				printf("%d",tab[i]);
			}
			printf("\n");*/
			for(int i=0;i<n/k;i++){
				for(int j=0;j<k;j++){
					stmp[j+i*k]=s[tab[j]-1+i*k];
				}
			}
			//printf("%s\n",stmp);
			co=0;
			char last = 0;
			for(int i=0;i<n;i++){
				if(stmp[i]!=last){
					co++;
					last=stmp[i];
				}
			}
			res=min(res,co);
		}while(next_permutation(tab,tab+k));
		printf("Case #%d: ",ca);
		printf("%d\n",res);
	}
	return 0;
}

