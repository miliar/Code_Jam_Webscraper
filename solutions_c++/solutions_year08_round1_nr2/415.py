#include <iostream>
#include <string>
#include <map>
#include <utility>
#include <algorithm>
#include <set>
#include <vector>
#include <sstream>

using namespace std; 
int a[101][22]; //i=customer j=number = which malt
int b[101][22]; //which flavour
int ainx[101];
bool csat[101];
int main(){
	int t,n,m,tmp,mal;
	int maxv,res=50,cnt,outp;
	bool ok;
	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++){
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		memset(ainx,0,sizeof(ainx));
		res=50;
		scanf("%d",&n); 
		scanf("%d",&m);
		maxv=(1<<n);
		for(int i=0;i<m;i++){
			scanf("%d",&ainx[i]);
			for(int j=0;j<ainx[i];j++){
				scanf("%d %d",&a[i][j],&b[i][j]);
				a[i][j]--;
			}
		}
		//cout<<"here "<<maxv<<endl;
		for(int i=0;i<maxv;i++){
			//cout<<i<<" "<<m<<endl;
			memset(csat,0,sizeof(csat));
			cnt=0;ok=true;
			for(int j=0;j<n;j++){
				//cout<<" "<<j<<endl;
				if(i&(1<<j)){ //malted flavour for flavour j;
					cnt++;
					for(int k=0;k<m;k++)
					if(!csat[k]){
						//cout<<"  "<<k<<" "<<ainx[k]<<endl;
						for(int mn=0;mn<ainx[k];mn++)
						if(a[k][mn]==j && b[k][mn]==1){
							csat[k]=true;
						}
					}
				}
				else{
					for(int k=0;k<m;k++)
					if(!csat[k]){
						//cout<<"  "<<k<<" "<<ainx[k]<<endl;
						for(int mn=0;mn<ainx[k];mn++)
						if(a[k][mn]==j && b[k][mn]==0){
							csat[k]=true;
						}
					}
				}
			}
			for(int j=0;j<m;j++)
			if(!csat[j]){ok=false;}
			if(ok){if(cnt<res){res=cnt;outp=i;}}
		}
		if(res==50)printf("Case #%d: IMPOSSIBLE\n",tc);
		else{ printf("Case #%d:",tc);
		for(int i=0;i<n;i++){
			printf(" %d",(outp&1));
			outp/=2;
		}
		printf("\n");
		}
		
	}
	return 0;
}