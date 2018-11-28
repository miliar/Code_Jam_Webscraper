#include<stdio.h>
typedef struct {
int height_A;
int height_B;
}link;
int main(){
	FILE *fpin,*fpout;
	fpin=fopen("input.txt","r");
	fpout=fopen("output.txt","w");
	int no_of_testcases;
	int i;
	link links[1000];
	fscanf(fpin,"%d\n",&no_of_testcases);
	for(i=1;i<=no_of_testcases;i++)
	{
		int no_of_links;
		int intersections=0;
		int k,l,j;
		fscanf(fpin,"%d\n",&no_of_links);
		for(j=0;j<no_of_links;j++)
		{
			fscanf(fpin,"%d %d\n",&links[j].height_A,&links[j].height_B);
		}
		for(k=0;k<no_of_links;k++)
		{
			for(l=k+1;l<no_of_links;l++)
			{
				if( (links[k].height_A<links[l].height_A && links[k].height_B>links[l].height_B) || (links[k].height_A>links[l].height_A && links[k].height_B<links[l].height_B) ){intersections++;}
			}
		}
		fprintf(fpout,"Case #%d: %d\n",i,intersections);
	}
	fclose(fpin);
	fclose(fpout);
	return 1;
}
