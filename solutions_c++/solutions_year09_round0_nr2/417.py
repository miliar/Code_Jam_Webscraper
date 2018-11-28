#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <complex> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <cassert> 
using namespace std;

const int dx[]={-1,0,0,1};
const int dy[]={0,-1,1,0};
int F[11111];
void clear(){
	memset(F,-1,sizeof(F));
}
int getF(int a){
	return F[a]==-1?a:F[a]=getF(F[a]);
}
bool merge(int a,int b){
	a=getF(a),b=getF(b);
	if(a!=b){
		F[a]=b;
		return true;
	}
	return false;
}
int a[111][111];
char z[11111];
int main(){
	int T,n,m,tests=0;
	scanf("%d",&T);
	while(T--){
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				scanf("%d",&a[i][j]);
		clear();
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++){
				int minv=a[i][j],target=-1;
				for(int k=0;k<4;k++){
					int nx=i+dx[k],ny=j+dy[k];
					if(nx>=0&&nx<n&&ny>=0&&ny<m&&a[nx][ny]<minv){
						minv=a[nx][ny];
						target=nx*m+ny;
					}
				}
				if(target!=-1)
					merge(i*m+j,target);
			}
		printf("Case #%d:\n",++tests);
		memset(z,0,sizeof(z));
		int cs=0;
		for(int i=0;i<n*m;i++){
			int f=getF(i);
			if(z[f]==0)
				z[f]='a'+cs++;
			putchar(z[f]);
			if(i%m==m-1)
				putchar('\n');
			else
				putchar(' ');
		}
	}
}
