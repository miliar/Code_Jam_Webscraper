#include<cstdio>
#include<cmath>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

int map[10][10];

int main(void){
	FILE *fin=fopen("input.txt","r");
	FILE *fout=fopen("output.txt","w");

	int T;
	int R,C,D;
	fscanf(fin,"%d",&T);
	for(int t=1;t<=T;t++){
		fscanf(fin,"%d %d %d",&R,&C,&D);
		for(int i=0;i<R;i++){
			for(int j=0;j<C;j++){
				fscanf(fin,"%1d",&map[i][j]);
				map[i][j] += D;
			}
		}
		bool flag = false;
		int ss;
		int RC = R>C ? C : R;
		for(ss=RC;ss >= 3;ss--){
			for(int j=0;j<=R-ss;j++){	
				for(int k=0;k<=C-ss;k++){
					float massx = 0;
					float massy = 0;
					float mass = 0;
					for(int t1 = j; t1 < j+ss; t1++){
						for(int t2 = k; t2 < k+ss; t2++){
							if(t1 == j && t2 == k) continue;
							if(t1 == j+ss-1 && t2 == k+ss-1) continue;
							if(t1 == j && t2 == k+ss-1) continue;
							if(t1 == j+ss-1 && t2 == k) continue;
							massx += ((float)(t1 - j)+0.5f) * (float)map[t1][t2];
							massy += ((float)(t2 - k)+0.5f) * (float)map[t1][t2];
							mass += (float)map[t1][t2];
						}
					}
					massx /= (float)(mass);
					massy /= (float)(mass);
					
					float cx, cy;
					if(ss % 2 == 0){
						cx = cy = (float)ss / 2.0f;
					} else{
						cx = cy = (float)(ss / 2) + 0.5f;
					}

					if( massx == cx && massy == cy ) flag = true;
				}
				if(flag) break;
			}
			if(flag) break;
		}
		if(!flag) fprintf(fout,"Case #%d: IMPOSSIBLE\n", t);
		else{
			fprintf(fout,"Case #%d: %d\n", t, ss);
		}
	}

	fcloseall();
}