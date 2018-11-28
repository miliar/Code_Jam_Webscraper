#include<cstdio>
#include<cstring>
using namespace std;

char cc[40][5];
char dd[40][5];
char str[105];
char stk[105];
int main(){
	FILE* fin=fopen("B-large.in","r");
	FILE* fout=fopen("B-large.out","w");
	
	int t,cas=0;
	fscanf(fin,"%d",&t);
	while(t--){
		int c,d;
		fscanf(fin,"%d",&c);
		for(int i=0;i<c;i++){
			fscanf(fin,"%s",cc[i]);
		}
		fscanf(fin,"%d",&d);
		for(int i=0;i<d;i++){
			fscanf(fin,"%s",dd[i]);
		}
		
		int n;
		fscanf(fin,"%d",&n);
		fscanf(fin,"%s",str);
		puts(str);
		int sp=0;
		for(int i=0;i<n;i++){
			if(i==0) stk[sp++]=str[0];
			else{
				bool flag=true;
				if(sp>0){
					for(int j=0;j<c;j++){
						if(stk[sp-1]==cc[j][0]&&str[i]==cc[j][1]){
							stk[sp-1]=cc[j][2]; flag=false;
							break;
						}
						if(stk[sp-1]==cc[j][1]&&str[i]==cc[j][0]){
							stk[sp-1]=cc[j][2]; flag=false;
							break;
						}
					}
				}
				if(flag){
					for(int j=0;j<sp;j++){
						for(int k=0;k<d;k++){
							if(stk[j]==dd[k][0]&&str[i]==dd[k][1]){
								sp=0; flag=false;
								break;
							}
							if(stk[j]==dd[k][1]&&str[i]==dd[k][0]){
								sp=0; flag=false;
								break;
							}
						}
						if(!flag) break;
					}
				}
				if(flag) stk[sp++]=str[i];
			}
		}
		fprintf(fout,"Case #%d: [",++cas);
		for(int i=0;i<sp;i++){
			if(i) fprintf(fout,", ");
			fprintf(fout,"%c",stk[i]);
		}
		fprintf(fout,"]\n");
	}
}