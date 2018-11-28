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
typedef long double ld;
typedef pair<int,int> pi;
const int dx[8]={-1,-1,-1,0,0,1,1,1};
const int dy[8]={-1,0,1,-1,1,-1,0,1};
const char dc[8]={'\\','|','/','-','-','/','|','\\'};
const int dz[8]={1,1,1,1,-1,-1,-1,-1};
const int md=1000003;
int n,m,nn,mm;
char a[1000][1000];
int bb[1000][1000];
int pr[101][101][400];
int yr[1000][1000];
int yr0[1000];
int ws[1000];


int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int tt;
	scanf("%d",&tt);
	for (int ti=0;ti<tt;ti++){
		printf("Case #%d: ",ti+1);
		scanf("%d %d",&n,&m);
		for (int i=0;i<n;i++){
			scanf("%s",a[i]);
		}
		memset(yr,0,sizeof(yr));
		memset(yr0,0,sizeof(yr0));
		memset(pr,0,sizeof(pr));
		memset(bb,0,sizeof(bb));
		mm=0;
		for (int i=0;i<n;i++){
			for (int j=0;j<m;j++) {//if (i==0 || j==0 || i==n-1 || j==m-1){
				pr[i][j][mm++]=1;
				bb[i][j]=1;
			}
		}
		/*for (int i=0;i<n;i++){
			for (int j=0;j<m;j++){
				
			}
		}*/
		nn=0;
		for (int i=0;i<n;i++){
			for (int j=0;j<m;j++){// if (i==0 || j==0 || i==n-1 || j==m-1){				
				for (int k=0;k<8;k++) {
					int nx=(i+dx[k]+n)%n;
					int ny=(j+dy[k]+m)%m;
					if (a[nx][ny]==dc[k]){
						if (dz[k]==1){
							for (int l=0;l<mm;l++){
								yr[nn][l]^=pr[nx][ny][l];
							}							
						} else {
							for (int l=0;l<mm;l++){
								yr[nn][l]^=pr[nx][ny][l];
							}
							yr0[nn]^=1;
						}
					}
				}
				yr0[nn]^=1;
				nn++;
			}
		}
	/*	for (int i=0;i<nn;i++){
			for (int j=0;j<mm;j++)
				cerr<<yr[i][j]<<" ";
			cerr<<yr0[i]<<" ";
			cerr<<endl;
		}              */
		int ks=nn;
		for (int i=0;i<nn;i++){
			ws[i]=0;
		}
		while (1){
			int mx=-1;
			int my=-1;
			for (int i=0;i<nn;i++)if (ws[i]==0){
				for (int j=0;j<mm;j++){
					if (yr[i][j]==1){
						mx=i;
						my=j;
						break;
					}
				}
				if (mx!=-1) break;
			}
			if (mx==-1) break;
			ws[mx]=1;
			for (int i=0;i<nn;i++)if (i!=mx && yr[i][my]==1){
				for (int j=0;j<mm;j++){
					yr[i][j]^=yr[mx][j];
				}
				yr0[i]^=yr0[mx];
			}
			ks--;
		}
		int ans;
		bool bl=false;
		for (int i=0;i<nn;i++){
			int sum=0;
			for (int j=0;j<mm;j++)
				sum+=yr[i][j];
			if (sum==0 && yr0[i]==1){
				bl=true;
			}
		}
		if (bl) ans=0; else {
			ans=1;
			for (int i=0;i<ks;i++){
				ans=(ans*2)%md;
			}
		}
		cout<<ans;
		printf("\n");
	}
    return 0;
}









