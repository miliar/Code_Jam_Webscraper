#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <set>
#include <cmath>
using namespace std;
const double PI = acos(-1.0);
const int mn=105,mr=255,inf=1<<29;

int D,I,M,n,a[mn],f[mn][mr+10],ch[mr+10][mr+10];

int add(int a, int b){
    //if(abs(a-b)<=M)return 0;
    return (abs(a-b)-1)/M;
}

int main() {
  //  freopen("B-small-attempt0.in", "r", stdin);
   // freopen("B-small-attempt0.out", "w", stdout);
    //freopen("B-small-attempt1.in", "r", stdin);
    //freopen("B-small-attempt2.out", "w", stdout);
 //   freopen("B-small-attempt2.in", "r", stdin);
 //   freopen("B-small-attempt2.out", "w", stdout);
    freopen("B-small-attempt3.in", "r", stdin);
    freopen("B-small-attempt3.out", "w", stdout);
    
	int Tn;
	scanf("%d", &Tn);
	for (int T = 1; T <= Tn; T++) {
		scanf("%d%d%d%d",&D,&I,&M,&n);
		for(int i=1;i<=n;i++)scanf("%d",a+i);
		
		/*for(int i=0;i<=mr;i++)
            for(int j=i+1;j<=mr;j++)
                ch[i][j]=ch[j][i]=add(i,j);*/
        
		for(int i=0;i<=mr;i++)
            f[1][i]=abs(i-a[1]);
            /*
        int tmp[mr+10]; 
		for(int i=1;i<=n+1;i++){
		    if(M!=0){
                for(int k=0;k<=mr;k++)tmp[k]=f[i-1][k];
                for(int j=0;j<=mr;j++){
                    for(int k=0;k<=mr;k++)
                        tmp[j]=min(tmp[j],f[i-1][k]+ch[k][j]*I);
                }
                for(int j=0;j<=mr;j++)f[i-1][j]=min(f[i-1][j],tmp[j]);
		    }
		    
		    for(int j=0;j<=mr;j++){
		        f[i][j]=f[i-1][j]+D;
		        for(int k=max(j-M,0);k<=min(mr,j+M);k++){
		            f[i][j]=min(f[i][j],f[i-1][k]+abs(a[i]-j));
		            //f[i][j]=min(f[i][j],f[i-1][k]+ch[k][j]*I+(a[i]==j?0:I+D));
		        }
		    }
		    
		    for(int j=0;j<=mr;j++){
		        for(int k=0;k<=mr;k++)tmp[k]=f[i][k];
		        for(int k=0;k<=mr;k++)
                    tmp[j]=min(tmp[j],f[i-1][k]+add(f[i-1][k],j));
		    }
		    for(int j=0;j<=mr;j++)f[i-1][j]=min(f[i-1][j],tmp[j];
		    
		}*/
		
        for(int i=2;i<=n;i++)
            for(int j=0;j<=mr;j++){
                f[i][j] = f[i-1][j]+D;
                for (int k=0;k<=mr;k++){
                    int tmp=f[i-1][k]+abs(a[i]-j);
                    if(j!=k){
                        if(M>0)
                            tmp+=add(j,k)*I;
                        else
                            continue;
                    }
                    f[i][j]=min(f[i][j],tmp);
                }
            }
		
		
		printf("Case #%d: ", T);
		int ans=inf;
		for(int i=0;i<=mr;i++){
		    ans=min(ans,f[n][i]);
		}
		printf("%d\n",ans);
	}
	return 0;
}
