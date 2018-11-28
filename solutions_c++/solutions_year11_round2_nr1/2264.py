#include<cstdio>
#include<cstring>
using namespace std;
char game[110][110];
int main(){
	FILE* fin = fopen("A-large.in","r");
	FILE* fout = fopen("out.txt","w");
	int t,n,cnt = 0,cn,chang,cc;
	double score,wp[110],owp[110],oowp[110],w;
	fscanf(fin,"%d",&t);
	while(t --){
		cnt ++;
		//memset(wp,0,sizeof(wp));
		memset(owp,0,sizeof(owp));
		memset(oowp,0,sizeof(oowp));
		fscanf(fin,"%d",&n);
		for(int i = 0;i < n;i ++){
			fscanf(fin,"%s",game[i]);
		}
		for(int i = 0;i < n;i ++){
			cn = 0;
			chang = 0;
			for(int j = 0;j < n;j ++){
				if(game[i][j] == '1')
					cn ++;
				if(game[i][j] != '.')
					chang ++;
			}
			//printf("%d\n",cn);
			wp[i] = (double)((double)cn / (double)chang);
		}
		/*for(int i = 0;i < n;i ++){
			printf("%lf\n",wp[i]);
		}*/
		for(int i = 0;i < n;i ++){
			chang = 0;
			w = 0.0;
			for(int j = 0;j < n;j ++){
				if(game[i][j] != '.'){
					cn = 0;
					cc = 0;
					for(int k = 0;k < n;k ++){
						if(game[j][k] == '1' && k != i){
							cn ++;
						}
						if(game[j][k] != '.' && k != i){
							cc ++;
						}
					}
					w = w + (double)cn / (double)cc;
					chang ++;
				}
			}
			owp[i] = w / (double)(chang);
		}
		for(int i = 0;i < n;i ++){
			chang = 0;
			for(int j = 0;j < n;j ++){
				if(game[i][j] != '.'){
					oowp[i] += owp[j];
					chang ++;
				}
			}
			oowp[i] = oowp[i] / (double)(chang);
		}
		fprintf(fout,"Case #%d:\n",cnt);
		for(int i = 0;i < n;i ++){
			score = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
			fprintf(fout,"%.12lf\n",score);
		}
		
	}
	//scanf("%d",&n);
	return 0;
}
