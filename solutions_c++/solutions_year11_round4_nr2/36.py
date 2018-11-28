#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<ctime>
#include<cassert>
using namespace std;
#define y1 fndjifhwdn
#define ws vfsdkofsjd
#define fs first
#define sc second
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef double ld;
typedef pair<int,int> pi;
int n,m,d;
char a[1000][1000];
ld b1[1000][1000];
ld b2[1000][1000];
ld b3[1000][1000];
ld sum1[1000][1000];
ld sum2[1000][1000];
ld sum3[1000][1000];
const ld eps=1e-7;
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
	int tt;
    scanf("%d",&tt);
    for (int ti=0;ti<tt;ti++){
    	printf("Case #%d: ",ti+1);
    	scanf("%d%d%d",&n,&m,&d);
    	for (int i=0;i<n;i++){
    		scanf("%s",a[i]);
    		for (int j=0;j<m;j++){
    			b1[i][j]=(a[i][j]-'0')*(i+0.5);
    			b2[i][j]=(a[i][j]-'0')*(j+0.5);
    			b3[i][j]=(a[i][j]-'0');
    		}
    	}
    	for (int i=0;i<=n;i++){
    		for (int j=0;j<=m;j++){
    			sum1[i][j]=0;
    			sum2[i][j]=0;
    			sum3[i][j]=0;
    		}
    	}
    	for (int i=n-1;i>=0;i--){
    		for (int j=m-1;j>=0;j--){
    			sum1[i][j]=sum1[i+1][j]+sum1[i][j+1]-sum1[i+1][j+1]+b1[i][j];
    			sum2[i][j]=sum2[i+1][j]+sum2[i][j+1]-sum2[i+1][j+1]+b2[i][j];
    			sum3[i][j]=sum3[i+1][j]+sum3[i][j+1]-sum3[i+1][j+1]+b3[i][j];
    		}
    	}
    	int ans=2;
    	bool bol=false;
    	for (int i=0;i<n;i++){
    		for (int j=0;j<m;j++){
    			for (int k=ans+1;k+i-1<n && k+j-1<n;k++){
    				if (fabs(sum1[i][j]-sum1[i+k][j]-sum1[i][j+k]+sum1[i+k][j+k]-b1[i][j]-b1[i][j+k-1]-b1[i+k-1][j]-b1[i+k-1][j+k-1]-
    				        (sum3[i][j]-sum3[i+k][j]-sum3[i][j+k]+sum3[i+k][j+k]-b3[i][j]-b3[i][j+k-1]-b3[i+k-1][j]-b3[i+k-1][j+k-1])*(i+k*0.5))<eps)
    				if (fabs(sum2[i][j]-sum2[i+k][j]-sum2[i][j+k]+sum2[i+k][j+k]-b2[i][j]-b2[i][j+k-1]-b2[i+k-1][j]-b2[i+k-1][j+k-1]-
    				        (sum3[i][j]-sum3[i+k][j]-sum3[i][j+k]+sum3[i+k][j+k]-b3[i][j]-b3[i][j+k-1]-b3[i+k-1][j]-b3[i+k-1][j+k-1])*(j+k*0.5))<eps){
    					ans=k;
    					bol=true;
    				}
    			}
    		}
    	}
    	if (bol){
    		printf("%d",ans);
    	} else 
    		printf("IMPOSSIBLE");
    	printf("\n");
    }
    return 0;
}









