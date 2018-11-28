#include<stdio.h>
int main(){
	int T,cb,rm,n,s;
	char CB[100][4],RM[100][3],data[200];
	FILE *fp=fopen("b.in","r");
	FILE *fo=fopen("b.out","w");
	fscanf(fp,"%d",&T);
	for(int casen = 1; casen <= T; casen++){
		fscanf(fp,"%d",&cb);
		for(int i=0;i<cb;i++) fscanf(fp,"%s",CB[i]);
		fscanf(fp,"%d",&rm);
		for(int i=0;i<rm;i++) fscanf(fp,"%s",RM[i]);
		fscanf(fp,"%d",&n);
		fscanf(fp,"%s\n",data);
		s=0;
		for(int i=1;i<n;i++){
			for(int j=0;j<cb;j++){
				if(CB[j][0]==data[i]&&CB[j][1]==data[i-1]){
					
					data[i]=CB[j][2];
					for(int k=i-1;k>0;k--){
						data[k]=data[k-1];
					}
					s++;
					break;
				}
				else if(CB[j][1]==data[i]&&CB[j][0]==data[i-1]){
					
					data[i]=CB[j][2];
					for(int k=i-1;k>0;k--){
						data[k]=data[k-1];
					}
					s++;
					break;
				}
			}
			for(int j=0;j<s;j++) data[j]='.';
			for(int j=0;j<rm;j++){
				for(int k=s;k<=i-1;k++){
					if(RM[j][0]==data[k]&&RM[j][1]==data[i]){
						s=i+1;
						break;
					}
					else if(RM[j][1]==data[k]&&RM[j][0]==data[i]){
						s=i+1;
						break;

					}
				}
			}
			for(int j=0;j<s;j++) data[j]='.';
			

		}
		fprintf(fo,"Case #%d: [",casen);
		for(int i=0;i<n;i++){
			if(data[i]!='.'){
				fprintf(fo,"%c",data[i]);
				if(i!=n-1) fprintf(fo,", ");
			}

		}
		fprintf(fo,"]\n");

	}
	return 0;
}