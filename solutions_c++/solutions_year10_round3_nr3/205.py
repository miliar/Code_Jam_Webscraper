#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;
#define MAXN 520
int t,n,m,p,num,big,ans,jlh[MAXN],lo,hi,mid,v[MAXN];
int mat[MAXN][MAXN];
char s[MAXN][MAXN];

int to(char c){
	if (c>='0' && c<='9') return c-'0';
	return c-'A'+10;
}

int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
	int xx=1;
	scanf("%d",&t);
	while (t--){
		scanf("%d%d",&n,&m);
		for (int i=0;i<n;i++){
			scanf("%s",s[i]);
		}
		for (int i=0;i<n;i++){
			for (int j=0;j<strlen(s[i]);j++){
				int angka=to(s[i][j]);
				int now=4;
				while (now){
					mat[i][j*4+now-1]=(angka%2);
					angka/=2;
					now--;
				}
			}
		}
		ans=0;
		p=min(n,m);
		while (1){
			lo=1;hi=p;
			big=-1;
			while (1){
				mid=(lo+hi)/2;
				//cout<<"Z"<<mid<<' '<<lo<<' '<<hi<<endl;
				bool valid=0;
				for (int i=0;i<n;i++){
					for (int j=0;j<m;j++){
						if (i+mid-1>=n || j+mid-1>=m) break;
						valid=1;
						// start 0
						for (int k=0;k<mid;k++){
							for (int l=0;l<mid;l++){
								if ((k+l)%2==0){
									if (mat[i+k][j+l]!=0){
										valid=0;
										break;
									}
								}
								else {
									if (mat[i+k][j+l]!=1){
										valid=0;
										break;
									}
								}
							}
							if (!valid) break;
						}
						if (valid){
							break;
						}
						valid=1;
						// start 1
						for (int k=0;k<mid;k++){
							for (int l=0;l<mid;l++){
								if ((k+l)%2==0){
									if (mat[i+k][j+l]!=1){
										valid=0;
										break;
									}
								}
								else {
									if (mat[i+k][j+l]!=0){
										valid=0;
										break;
									}
								}
							}
						}
						if (valid){
							break;
						}
					}
					if (valid) break;
				}
				if (valid){
					big=mid;
					lo=mid+1;
				}
				else hi=mid-1;
				if (lo>hi) break;
			}
			if (big==-1) break;
			v[ans++]=big;
			num=0;
			for (int i=0;i<n;i++){
				for (int j=0;j<m;j++){
					if (i+big-1>=n || j+big-1>=m) break;
					bool valid=1;
					// start 0
					for (int k=0;k<big;k++){
						for (int l=0;l<big;l++){
							if ((k+l)%2==0){
								if (mat[i+k][j+l]!=0){
									valid=0;
									break;
								}
							}
							else {
								if (mat[i+k][j+l]!=1){
									valid=0;
									break;
								}
							}
						}
						if (!valid) break;
					}
					if (!valid){
						valid=1;
						// start 1
						for (int k=0;k<big;k++){
							for (int l=0;l<big;l++){
								if ((k+l)%2==0){
									if (mat[i+k][j+l]!=1){
										valid=0;
										break;
									}
								}
								else {
									if (mat[i+k][j+l]!=0){
										valid=0;
										break;
									}
								}
							}
							if (!valid) break;
						}
					}
					if (valid){
						num++;
						for (int k=0;k<big;k++){
							for (int l=0;l<big;l++){
								mat[i+k][j+l]=2;
							}
						}
					}
				}
			}
			jlh[big]=num;
			p=big-1;
			if (big==1) break;
		}
		printf("Case #%d: %d\n",xx++,ans);
		for (int i=0;i<ans;i++){
			printf("%d %d\n",v[i],jlh[v[i]]);
		}
	}
	return 0;
}
