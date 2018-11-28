#include<cstdio>
#include<cstring>
using namespace std;

int main(){
	FILE* fin=fopen("C-large.in","r");
	FILE* fout=fopen("C-large.out","w");
	
	int t,cas=0;
	fscanf(fin,"%d",&t);
	while(t--){
		int n;
		fscanf(fin,"%d",&n);
		int sum=0,mmin=1000005,vxor=0;
		for(int i=0;i<n;i++){
			int v;
			fscanf(fin,"%d",&v);
			sum+=v;
			vxor^=v;
			if(v<mmin) mmin=v;
		}
		fprintf(fout,"Case #%d: ",++cas);
		if(vxor){
			fprintf(fout,"NO\n");
		}else{
			fprintf(fout,"%d\n",sum-mmin);
		}
	}
}