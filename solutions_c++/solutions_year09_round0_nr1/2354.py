#include <stdio.h>
#include <string.h>

int L, D, N;
char Dic[5010][20];
char Test[510][500];

int main(){
	FILE *fin = fopen("A-large.in","r");

	fscanf(fin,"%d%d%d",&L,&D,&N);

	for(int i=1;i<=D;i++)
		fscanf(fin,"%s",Dic[i]);
	for(int i=1;i<=N;i++)
		fscanf(fin,"%s",Test[i]);

	fclose(fin);

	FILE *fout = fopen("A-large.out","w");

	for(int k=1;k<=N;k++){
		int len=strlen(Test[k]);
		int cnt=0;

		for(int i=1;i<=D;i++){
			int flag=0;
			int j;
			int w=0;
			for(j=0;j<len;j++){
				if(Test[k][j]=='('){
					flag=1;
				}else if(Test[k][j]==')'){
					if(flag==1)
						break;
					flag=0;
				}else if(flag==2){
					continue;
				}else if(flag==0){
					if(Dic[i][w]!=Test[k][j])
						break;				
					w++;
				}else if(flag==1){
					if(Dic[i][w]==Test[k][j]){
						flag=2;
						w++;
					}
				}
			}
			if(j==len)
				cnt++;
		}

		fprintf(fout,"Case #%d: %d\n",k,cnt);
	}

	fclose(fout);

	return 0;
}
