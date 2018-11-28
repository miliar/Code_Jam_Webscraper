#include <iostream>
#include <string>
#include <string.h>
#include <cstring>
#include <algorithm>
#include <math.h>
#include <vector>
#include <set>
#include <map>
#include <bitset>

using namespace std;

int a[200][200];
int b[200];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int c;
	scanf("%d",&c);

	for (int cc=1; cc<=c; cc++){
		printf("Case #%d: ",cc);
		int n;
		scanf("%d",&n);
		memset(a,-1,sizeof(a));
		for (int i=1; i<=n; i++){
			int st=n-i+1;
			b[i]=st%2;
			for (int j=1; j<=i; j++)
				scanf("%d",&a[i][st]), st+=2;
		}
		for (int i=1; i<n; i++){
			int st=i+1;
			b[i+n]=st%2;
			for (int j=1; j<=n-i; j++)
				scanf("%d",&a[n+i][st]), st+=2;
		}
		b[0]=1-b[1];
		for (int i=2; i<=3*n; i++)
			b[i]=1-b[i-1];

		int res=1000000;
		for (int i=0; i<=2*n; i++)
			for (int j=0; j<=2*n; j++){
				int x=i, y=j;
				int gd=1;
				if (b[i]!=y%2) gd=0;
				for (int N=0; N<=40; N++){
					int go=1;
					for (int k=1; k<2*n; k++){
						for (int l=1; l<2*n; l++)
							if (a[k][l]!=-1){
								if (abs(k-x)+abs(l-y)>N){
									go=0;
									break;
								}
							}
							if (!go) break;
					}
					if (!go) continue;
					int tr=1;
					for (int k=x-N; k<=x+N; k++){
						for (int l=y-N; l<=y+N; l++){
							int tx=k, ty=l;
							int dx=x-(k-x), dy=y-(l-y);
							if (tx>0&&ty>0&&dx>0&&dy>0){
								if (a[tx][ty]!=-1&&a[dx][dy]!=-1){
									if (a[tx][ty]!=a[dx][dy]){
										tr=0;
										break;
									}
								}
							}
							dx=x-(k-x), dy=l;
							if (tx>0&&ty>0&&dx>0&&dy>0){
								if (a[tx][ty]!=-1&&a[dx][dy]!=-1){
									if (a[tx][ty]!=a[dx][dy]){
										tr=0;
										break;
									}
								}
							}
							dx=k, dy=y-(l-y);
							if (tx>0&&ty>0&&dx>0&&dy>0){
								if (a[tx][ty]!=-1&&a[dx][dy]!=-1){
									if (a[tx][ty]!=a[dx][dy]){
										tr=0;
										break;
									}
								}
							}
							if (tr==0) break;
						}
						if (tr==0) break;
					}
					if (tr){
						int upd=((N+(1-gd))/2)*2;
						res=min(res,upd+gd);
						if (res==2){
							int kkk=1;
						}
					}
				}
			}
			printf("%d\n",res*res-n*n);
	}

	return 0;
}