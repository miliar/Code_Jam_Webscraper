#include <cstdio>
#include <algorithm>
#include <memory.h>
char a[33][33];
int d[10][1<<10];
int temp[2][33];
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d\n",&t);
	for(int tc=1; tc<=t; tc++){
		int n,m;
		scanf("%d %d\n",&n,&m);
		memset(a,0,sizeof(a));
		memset(d,0,sizeof(d));
		for(int i=0; i<n; i++)
			scanf("%s\n",a[i]);
		for(int i=0; i<n; i++){
			if(i==0){
				for(int j=0; j<(1<<m); j++){
			memset(temp,0,sizeof(temp));
					int cnt=0;
					int two=1;
					for(int k=0; k<m; k++){
						if(two&j){
							temp[1][k]=1;
							cnt++;
						}
						else
							temp[1][k]=0;
						two*=2;
					}
					bool ok = true;
					for(int k=0; k<m; k++){
						if(temp[1][k]==1 && a[i][k]=='x'){
							ok=false;
							break;
						}
					}
					for(int k=0; k<m; k++){
						if(temp[1][k] ==1 && temp[1][k-1]==1){
							ok=false;
							break;
						}
					}
					if(ok)
						d[i][j] = cnt;
				}
			}
			else{
				for(int j=0; j<(1<<m); j++){
					memset(temp,0,sizeof(temp));
					int cnt=0;
					int two=1;
					for(int k=0; k<m; k++){
						if(two&j){
							temp[1][k]=1;
							cnt++;
						}
						else
							temp[1][k]=0;
						two*=2;
					}
					for(int k=0; k<(1<<m); k++){
						two=1;
						for(int l=0; l<m; l++){
							if(two&k){
								temp[0][l]=1;
							}
							else
								temp[0][l]=0;
							two*=2;
						}
						bool ok = true;
						for(int l=0; l<m; l++){
							if(temp[1][l]==1 && a[i][l]=='x'){
								ok=false;
								break;
							}
							if(temp[0][l]==1 && a[i-1][l]=='x'){
								ok=false;
								break;
							}
						}
						if(ok){
							bool oo=true;
							for(int l=0; l<m; l++){
								if(l!=0){
									if(temp[0][l-1]==1 && temp[1][l]==1)
										oo=false;
									if(temp[0][l-1]==1 && temp[0][l]==1)
										oo=false;
									if(temp[1][l-1]==1 && temp[1][l]==1)
										oo=false;
								}
								if(l!=m-1){
									if(temp[0][l+1]==1 && temp[1][l]==1)
										oo=false;
									if(temp[0][l+1]==1 && temp[0][l]==1)
										oo=false;
									if(temp[1][l+1]==1 && temp[1][l]==1)
										oo=false;
								}
							}
							if(oo){
								d[i][j] = std::max(d[i][j],d[i-1][k] + cnt);
							}
						}
					}
				}
			}
		}
		printf("Case #%d: %d\n",tc,*std::max_element(d[n-1],d[n-1]+(1<<m)));
	}
	return 0;
}