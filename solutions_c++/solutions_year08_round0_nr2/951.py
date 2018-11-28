#include <stdio.h>
#include <vector>
using namespace std;

vector<int> CA[2000];
vector<int> CB[2000];
int stayA[2000];
int stayB[2000];

int main(){
	int N;
	scanf("%d",&N);
	for(int t=1;t<=N;t++){
		for(int i=0;i<2000;i++){
			CA[i].clear();
			CB[i].clear();
			stayA[i]=0;
			stayB[i]=0;
		}
		int T,NA,NB,retA=0,retB=0;
		scanf("%d%d%d",&T,&NA,&NB);	
		for(int i=0;i<NA;i++){
			int dm,dh,am,ah;
			scanf("%d:%d %d:%d",&dh,&dm,&ah,&am);
			CA[dh*60+dm].push_back(ah*60+am);	
		}
		for(int i=0;i<NB;i++){
			int dm,dh,am,ah;
			scanf("%d:%d %d:%d",&dh,&dm,&ah,&am);
			CB[dh*60+dm].push_back(ah*60+am);	
		}
		int ha = 0,hb = 0;
		for(int i=0;i<=1439;i++){
			ha+=stayA[i];
			hb+=stayB[i];
			for(int j=0;j<CA[i].size();j++){
				stayB[CA[i][j]+T]++;
				ha--;
				if(ha==-1){
					retA++;
					ha=0;	
				}	
			}
			for(int j=0;j<CB[i].size();j++){
				stayA[CB[i][j]+T]++;
				hb--;
				if(hb==-1){
					retB++;
					hb=0;	
				}	
			}
		}
		printf("Case #%d: %d %d\n",t,retA,retB);
	}
	
}
