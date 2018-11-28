#include<cstdio>
using namespace std;

int main(){
	FILE* fin = fopen("C-large.in","r");
	FILE* fout = fopen("C-large.out","w");
	int t;
	int min,xorSUM,SUM;
	int in,n;
	fscanf(fin,"%d",&t);
	for(int i = 1;i <= t;i ++){
		fscanf(fin,"%d",&n);
		fscanf(fin,"%d",&in);
		SUM = in;
		xorSUM = in;
		min = in;
		for(int j = 1;j < n;j ++){
			fscanf(fin,"%d",&in);
			SUM += in;
			xorSUM = xorSUM ^ in;
			if(min > in){
				min = in;
			}
		}
		fprintf(fout,"Case #%d: ",i);
		if(xorSUM != 0){
			fprintf(fout,"NO\n");
		}
		else{
			SUM -= min;
			fprintf(fout,"%d\n",SUM);
		}

	}
	return 0;
}

