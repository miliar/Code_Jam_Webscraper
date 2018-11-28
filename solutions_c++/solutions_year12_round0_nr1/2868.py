#include <stdio.h>
#include <string.h>

#define MAX 110

FILE *in,*out;

int main(void)
{
	int i,j,k,T;
	char G[MAX],translate[27]="ynficwlbkuomxsevzpdrjgthaq",result[MAX],blank;

	in=fopen("A-small-attempt1.in","r");
	out=fopen("output.txt","w");

	fscanf(stdin,"%d%c",&T,&blank);

	for(i=0;i<T;i++){
		G[0]='\0';
		fgets(G,102,stdin);
		for(j=0;j<strlen(G)-1;j++){
			if(G[j] == ' ') result[j]=' ';
			else{
				for(k=0;k<26;k++){
					if(G[j] == translate[k]){
						result[j]=k+97;
						break;
					}
				}
			}
		}
		result[j]='\0';
		fprintf(stdout,"Case #%d: %s\n",i+1,result);
	}

	fclose(in);
	fclose(out);

	return 0;
}