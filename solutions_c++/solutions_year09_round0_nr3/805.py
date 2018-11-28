#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;

const int maxn= 600;
const int mod =10000;
int d[maxn][100];
const char word[]={"welcome to code jam"};
char str[maxn];
int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int i,j,k,T;
	scanf("%d",&T);
	getchar();
	for(int ca=1;ca<=T;ca++){
		
		gets(str);
		//cout<<str<<endl;
		printf("Case #%d: ",ca);
		memset(d,0,sizeof(d));
		for(i=0;str[i];i++){
			for(j=1;j<=19;j++){
				d[i+1][j]=d[i][j];
				if( str[i]==word[j-1] ){
					
					if( j==1 )d[i+1][j] = (d[i+1][j] + d[i][j-1]+1)%mod;
					else d[i+1][j] = (d[i+1][j] + d[i][j-1])%mod;
					
				}
			}
			//for(j=1;j<=19;j++)cout<<d[i+1][j]<<" ";
			//cout<<endl;
		}

		

		printf("%04d\n",d[i][19]);
	}
}
