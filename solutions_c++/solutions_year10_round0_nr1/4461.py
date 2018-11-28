#include <stdio.h>
FILE *fin = fopen("input.txt","r");
FILE *fout = fopen("output.txt","w");
int n,k;
bool snapper[100];
void input()
{
	fscanf(fin,"%d %d",&n,&k);
}
void pro()
{
	int i,j;
	for (i=0;i<n;i++){ snapper[i]=false;}

	for (j=0;j<k;j++){
		for (i=0;i<n;i++){
			if (i!=0 && snapper[i-1] == true)  break;
			snapper[i] = !snapper[i];
		}
	}
}
void output()
{
	int i;
	for (i=0;i<n;i++){
		if (snapper[i] == false) break;
	}
	if (i==n){
		fprintf(fout,"ON\n");
	}else{
		fprintf(fout,"OFF\n");
	}
}
int main()
{
	int i,t;
	fscanf(fin,"%d",&t);
	for (i=0;i<t;i++){
		input();
		pro();
		fprintf(fout,"Case #%d: ",i+1);
		output();
	}
	return 0;
}