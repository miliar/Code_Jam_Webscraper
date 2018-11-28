#include<cstdio>
#include<cstring>
using namespace std;
#define ABS(x) (x>0?x:(-x))

int val[102];
char rob[102][5];
int main(){
	FILE* fin=fopen("A-large.in","r");
	FILE* fout=fopen("A-large.out","w");
	
	int t,cas=0;
	fscanf(fin,"%d",&t);
	while(t--){
		int n;
		fscanf(fin,"%d",&n);
		for(int i=0;i<n;i++){
			fscanf(fin,"%s %d",rob[i],&val[i]);
		}

		int bt=0,ot=0,time=0;
		int bp=1,op=1;
		for(int i=0;i<n;i++){
			if(rob[i][0]=='O'){
				if(ABS((val[i]-op))+ot<time){
					time+=1;
					op=val[i];
					ot=time;
				}else{
					time=ABS((val[i]-op))+ot+1;
					op=val[i];
					ot=time;
				}
			}else{
				if(ABS((val[i]-bp))+bt<time){
					time+=1;
					bp=val[i];
					bt=time;
				}else{
					time=ABS((val[i]-bp))+bt+1;
					bp=val[i];
					bt=time;
				}
			}
//			printf("= %c %d\n",rob[i][0],val[i]);
//			printf("= (%d,%d) (%d,%d) %d\n",bt,bp,ot,op,time);
		}
		fprintf(fout,"Case #%d: %d\n",++cas,time);
	}
}