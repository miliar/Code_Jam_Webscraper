#include <stdio.h>
#include <string.h>

int T;
char N[100];
char Outp[100];
int Len;
int Count[10];

int main(){
	int i, j;
	int flag;
	int temp;

	FILE *fin = fopen("B-large.in","r");
	FILE *fout = fopen("B-large.out","w");

	fscanf(fin,"%d",&T);
	for(int k=1;k<=T;k++){
		fscanf(fin,"%s",&N);

		Len=strlen(N);

		for(i=0;i<10;i++)
			Count[i]=0;

		flag=0;
		Count[N[Len-1]-'0']++;
		for(i=Len-2;i>=0;i--){
			Count[N[i]-'0']++;
			if(N[i]<N[i+1]){
				for(j=0;j<i;j++)
					Outp[j]=N[j];

				temp=i;

				for(j=N[i]-'0'+1;j<10;j++){
					if(Count[j]!=0){
						Count[j]--, Outp[temp++]='0'+j; 
						break;
					}
				}
				for(j=0;j<10;j++){
					while(Count[j]>0){
						Outp[temp++]='0'+j;
						Count[j]--;
					}
				}
				Outp[Len]='\0';

				break;
			}
		}

		if(i==-1){
			flag=0;
			Count[0]++, temp=0, Outp[Len+1]='\0';
			for(i=1;i<=9;i++){
				while(Count[i]>0){
					Outp[temp++]=i+'0';
					Count[i]--;
					if(flag==0){
						for(j=0;j<Count[0];j++){
							Outp[temp++]='0';
						}
						flag=1;
					}
				}
			}
		}

		fprintf(fout,"Case #%d: %s\n",k,Outp);
	}

	fclose(fin);
	fclose(fout);

	return 0;
}
