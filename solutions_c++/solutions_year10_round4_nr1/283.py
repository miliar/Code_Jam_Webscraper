#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <string.h>
#include <math.h>


using namespace std;

#define BASE 300
int ans;
int n;


char map[1000][1000];

int main(){
	freopen("out.txt","w",stdout);
	int cntcase,casenum;

	int cx,cy;
	cin>>casenum;
	int nx[5];
	int midx,midy;

	for(int cntcase=1;cntcase<=casenum;cntcase++){

		memset(map,0,sizeof(map));
		cin>>n;
		cin.getline(map[0],2);

		for(int i=BASE+1;i<=BASE+n+n-1;i++){
			cin.getline(map[i]+BASE+1,1000);
			//cout<<map[i]+BASE+1<<endl;
			for(int j=0;j<=2*n+1;j++){
				if(map[i][j+BASE]==' '){
					map[i][j+BASE] = 0;

				}

			}
		}

		midx = n+BASE;
		midy = n+BASE;

		ans = INT_MAX;
		for(int i=BASE+1;i<=BASE+2*n;i++){
			// 			int j;
			// 			int k;
			// 			for(k=BASE+1;;k++){
			// 				if(map[i][k]!=0){
			// 					break;
			// 				}
			// 			}
			// 			j = k;
			for(int j=BASE+1;j<=BASE+2*n;j++){
				// 
				// 				bool nonum = true;
				// 				for(int k=j;k<=BASE+2*n;k++)
				// 				{
				// 					if(map[i][k]!=0){
				// 						nonum = false;
				// 						break;
				// 					}
				// 				}
				// 				if(nonum)break;

				cx = i;
				cy = j;

				bool fail = false;

				for(int u=BASE+1;u<=BASE+2*n;u++)
				{
					for(int v=BASE+1;v<=BASE+2*n;v++){

						nx[1] = map[u][v];
						if(map[u][v]==0)continue;

						nx[2] = map[cx-(u-cx)][v];
						nx[3] = map[u][cy-(v-cy)];

						if(nx[1]!=0&&nx[2]!=0){
							if(nx[1]!=nx[2]){
								fail = true;
							}
						}
						if(nx[1]!=0&&nx[3]!=0){
							if(nx[1]!=nx[3]){
								fail = true;
							}
						}

						if(fail)break;

					}
				}


				int ran = 0;
				int rad = 0;
				if(!fail){
					rad = abs(cx-midx)+abs(cy-midy)+n;
					ans = min(ans,rad*rad-n*n);
				}

			}
		}




		printf("Case #%d: %d\n",cntcase,ans);
	}

}