#include <iostream>
#include <vector>
using namespace std;
int main(){
	int i,j,k;
	int T,r,t;
	int x1,x2,y1,y2,x,y,z;
	
	cin>>T;
	t=1;
	while(T--){
		scanf("%d",&r);
		vector<vector<int> > vv(105,vector<int> (105,0));
		
		z = 0;
		for(i=0;i<r;i++){
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			z = max(z,max(x2,y2));
			for(j=x1;j<=x2;j++){
				for(k=y1;k<=y2;k++)
					vv[j][k] = 1;
			}
		}
			
		int ans = 0;
		bool flag = true;
		while(flag){
			vector<vector<int> > vp(105,vector<int> (105,0));
			
			flag = false;
			for(i=1;i<=z;i++){
				for(j=1;j<=z;j++){
					if(vv[i][j] == 1){
						flag =true;
						vp[i][j] = 1;
					}
					
					if(vv[i-1][j] == 1 && vv[i][j-1] == 1)
						vp[i][j] = 1;
					if(vv[i-1][j] == 0 && vv[i][j-1] == 0)
						vp[i][j] = 0;
				}
			}
			if(flag){
				ans++;
				vv = vp;
			}
		}
		printf("Case #%d: %d\n",t,ans);
		t++;
	}
	return 0;
}

		
	
	