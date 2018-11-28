#include<cstdio>
#include<algorithm>
using namespace std;

int Z,R,C,D;
char s[505];
int a[505][505];
bool rr[505][505];
bool cc[505][505];

int SS(int x1,int x2,int y1,int y2){
	return a[x2][y2] + a[x1-1][y1-1] - a[x2][y1-1] - a[x1-1][y2];
}

int main(){
	scanf("%d",&Z);
	for (int z=1;z<=Z;++z){
		scanf("%d%d",&R,&C,&D);
					gets(s);

		for (int i=0;i<R;++i){
			scanf("%s",s);
			for (int j=0;j<C;++j){
				a[i+1][j+1] = a[i+1][j] + a[i][j+1]- a[i][j] + (s[j]-'0');
			}
		}
		
		int ans = min(R,C);
		bool ok = false;
		while (!ok && ans>=3){
		
			int sum = 0;
			
			for (int i=1;i+ans-1<=R;++i){
				for (int j=1;j+ans-1<=C;++j){
					if (j==1){
					
						sum = 0;
						
						if (ans%2==1){
							for (int k=1;k<=ans;++k){
								sum += SS(i,i+ans-1,k,k) * (k-(ans/2+1));
							}
						}else{
							for (int k=1;k<=ans;++k){
								if (k<=ans/2)
									sum += SS(i,i+ans-1,k,k) * (k-(ans/2+1));
								else
									sum += SS(i,i+ans-1,k,k) * (k-(ans/2));
							}
						}
						
					}else{
						if (ans%2==1){
							sum -= SS(i,i+ans-1,j-1,j+ans-1-1);
							sum += SS(i,i+ans-1,j-1,j-1) * (ans/2 + 1);
							sum += SS(i,i+ans-1,j+ans-1,j+ans-1) * (ans/2);
						}else{
							sum -= SS(i,i+ans-1,j-1,j+ans-1-1);
							sum += SS(i,i+ans-1,j-1,j-1) * (ans/2 + 1);
							sum -= SS(i,i+ans-1,j+ans/2-1,j+ans/2-1);
							sum += SS(i,i+ans-1,j+ans-1,j+ans-1) * (ans/2);
						}
					}
					
					int r = sum + (ans/2)*(SS(i,i,j,j)+SS(i+ans-1,i+ans-1,j,j)-SS(i,i,j+ans-1,j+ans-1)-SS(i+ans-1,i+ans-1,j+ans-1,j+ans-1));
					
					if (r==0){
						rr[i][j] = 1;
					}else{
						rr[i][j] = 0;
					}
					
					
				}
			}
			
			for (int j=1;j+ans-1<=C;++j){
				for (int i=1;i+ans-1<=R;++i){
					if (i==1){
					
						sum = 0;
						
						if (ans%2==1){
							for (int k=1;k<=ans;++k){
								sum += SS(k,k,j,j+ans-1) * (k-(ans/2+1));
							}
						}else{
							for (int k=1;k<=ans;++k){
								if (k<=ans/2)
									sum += SS(k,k,j,j+ans-1) * (k-(ans/2+1));
								else
									sum += SS(k,k,j,j+ans-1) * (k-(ans/2));
							}
						}
						
					}else{
						if (ans%2==1){
							sum -= SS(i-1,i+ans-1-1,j,j+ans-1);
							sum += SS(i-1,i-1,j,j+ans-1) * (ans/2 + 1);
							sum += SS(i+ans-1,i+ans-1,j,j+ans-1) * (ans/2);
						}else{
							sum -= SS(i-1,i+ans-1-1,j,j+ans-1);
							sum += SS(i-1,i-1,j,j+ans-1) * (ans/2 + 1);
							sum -= SS(i+ans/2-1,i+ans/2-1,j,j+ans-1);
							sum += SS(i+ans-1,i+ans-1,j,j+ans-1) * (ans/2);
						}
					}
					
					int r = sum + (ans/2)*(SS(i,i,j,j)-SS(i+ans-1,i+ans-1,j,j)+SS(i,i,j+ans-1,j+ans-1)-SS(i+ans-1,i+ans-1,j+ans-1,j+ans-1));
					
					if (r==0){
						cc[i][j] = 1;
					}else{
						cc[i][j] = 0;
					}
					
					
				}
			}
			
			for (int i=1;i+ans-1<=R;++i){
				for (int j=1;j+ans-1<=C;++j){
					if (rr[i][j] && cc[i][j]){
						ok = true;
					}
				}
			}
			if (ok==false) --ans;
		}
		
		
		printf("Case #%d: ",z);
		if (ok){
			printf("%d\n",ans);
		}else{
			printf("IMPOSSIBLE\n");
		}
		
		
	}
	return 0;
}
