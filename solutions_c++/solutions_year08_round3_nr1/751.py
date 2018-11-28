#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int compare_int(const int *a, const int *b)
{
    return *b - *a;
}

int main(int argc, char *argv[])
{
	int i,j,m,n,p,k,l,ans;
	int alphabet[1024];
	FILE *fp,*fp_out;

	if((fp=fopen("A-small-attempt0.in","r"))==NULL)return -1;
	if((fp_out=fopen("A-small-attempt0.in.txt","w"))==NULL)return -1;

	fscanf(fp,"%d\n",&n);
	for(i=0;i<n;i++){
		fscanf(fp,"%d %d %d\n",&p,&k,&l);

		for(j=0;j<l;j++){
			fscanf(fp,"%d",&alphabet[j]);
		}

		qsort(alphabet, l, sizeof(int), (int (*)(const void*, const void*))compare_int);

		ans=0;
		for(j=0;j<l;j++){
			ans+=alphabet[j]*(j/k+1);
		}

		printf("Case #%d: %d\n",i+1,ans);
		fprintf(fp_out,"Case #%d: %d\n",i+1,ans);
	}
	//printf("Finished!\n");
	fclose(fp);
	fclose(fp_out);
	
	getchar();
}
