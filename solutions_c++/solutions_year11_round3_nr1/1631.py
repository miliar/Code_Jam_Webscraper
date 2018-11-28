#include<string>
#include<vector>
#include<iostream>
#include<cstdio>
#include<algorithm>

using namespace std;

#define rep(i,n) for(int i=0;i<int(n);i++)
#define reps(i,n) for(int i=1;i<=int(n);i++)

int main(){
	int t;
	cin>>t;
	
	rep(p,t){
		int r,c;
		cin>>r>>c;
		
		int masu[55][55]={0};
		rep(i,r){
			string a;
			cin>>a;
			
			rep(j,c){
				if(a[j]=='#'){
					masu[i][j]=1;
				}else{
					masu[i][j]=0;
				}
			}
		}
		
		char ans[55][55]={0};
		
		int dx[]={0,1,0,1};
		int dy[]={0,0,1,1};
		
		rep(i,r-1){
			rep(j,c-1){
				int flg=1;
				rep(k,4){
					int ddx=i+dx[k];
					int ddy=j+dy[k];
					
					if(masu[ddx][ddy]!=1){
						flg=0;
					}
				}
				
				if(flg==0)continue;
				
				rep(k,4){
					int ddx=i+dx[k];
					int ddy=j+dy[k];
					
					masu[ddx][ddy]='.';
					if((dx[k]+dy[k])%2==0){
						ans[ddx][ddy]='/';
					}else{
						ans[ddx][ddy]='\\';
					}
				}
			}
		}
		
		int fflg=0;
		rep(i,r)rep(j,c){
			if(masu[i][j]==1){
				fflg=1;
			}
		}
		
		
		printf("Case #%d:\n",p+1);
		if(fflg){
			puts("Impossible");
			continue;
		}
		
		rep(i,r){
			rep(j,c){
				if(ans[i][j]!=0){
					printf("%c",ans[i][j]);
				}else{
					printf(".");
				}
			}puts("");
		}
	}
}