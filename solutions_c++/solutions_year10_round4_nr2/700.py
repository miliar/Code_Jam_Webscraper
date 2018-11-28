#include <queue>
#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

long long dp[2000000][20];
long long kan[2000000];
long long kir[2000000];
int tri=0;
long long M[2000000];
int n;
long long harg[2000000];
long long wow(int pos,int x){
//	cout<<pos<<" "<<x<<endl;
	if (pos==-1) return 0;
	if (pos<(1<<n)) {
	   				 if (x>M[pos]) return 9999999999ll;
	   				 else return 0;
						}
	if (dp[pos][x]!=-1) return dp[pos][x];
	long long tmp=0;
	tmp=min(wow(kan[pos],x+1)+wow(kir[pos],x+1) ,
	wow(kan[pos],x)+wow(kir[pos],x)+harg[pos]);
	
	dp[pos][x]=tmp;
	return tmp;
	}
	
int main(){
	int zz=0;
	int T=0;
	 freopen("bol.in","r",stdin); 
	 freopen("bol_o.out","w",stdout);
	scanf("%d",&T);
	while (T--){
		  memset(dp,-1,sizeof(dp));
		  memset(harg,0,sizeof(harg));
		  memset(kan,0,sizeof(kan));
		  memset(kir,0,sizeof(kir));
		  tri=0;
		  scanf("%d",&n);
		  for (int i=0;i<(1<<n);i++) {tri++;scanf("%d",&M[i]);}
		  for (int i=1;i<=n;i++){int naek=0;
		  	  for (int j=0;j<(1<<(n-i));j++){
		  	  int tmp;
		  	  scanf("%d",&tmp);
			  harg[tri]=tmp;
			  
			  if (tri>=(1<<n)){
			  	 			   kan[tri]=tri-(1<<(n-i+1))+naek;
			  	 			   kir[tri]=tri-(1<<(n-i+1))+1+naek;
			  	naek++;
				   			   	  }
			  tri++;
				}
				}
			//	cout<<kan[2]<<" "<<kir[2]<<endl;
			zz++;
		  printf("Case #%d: %d\n",zz,wow(tri-1,0));
		  }
	
	
//	system("pause");
	}
