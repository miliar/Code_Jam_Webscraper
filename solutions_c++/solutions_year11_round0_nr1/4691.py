#include <cstdlib>
#include <iostream>
#include <cstring>
using namespace std;

int main(int argc, char* argv[])
{
	int t,m=1;
	char ch;
	int p;
	FILE *fp1,*fp2; 
    fp2=fopen("D:\\in.txt","r+");
	fp1=fopen("D:\\fileout.txt","w+");
	fscanf(fp2,"%d",&t);
	for(int i=0;i<t;i++)
	{
		int n,vo=1,vb=1,preo=1,preb=1;
		int sum=0;
		char op;
		fscanf(fp2,"%d",&n);
		for(int j=0;j<n;j++)
		{	fscanf(fp2,"%c",&op);
			fscanf(fp2,"%c%d",&ch,&p);
			if(!(ch-'O')) {
				if(vo>p) {if(preo<=p||vo-preo>preo-p){sum++;vb++;} else {sum+=2*preo-p-vo+1;vb+=2*preo-p-vo+1;}}
				else {sum+=p-vo+1;vb+=p-vo+1;}
				vo=p;
				preo=p;
			}
			else {
				if(vb>p) {if(preb<=p||vb-preb>preb-p){sum++;vo++;} else {sum+=2*preb-p-vb+1;vo+=2*preb-p-vb+1;}}
				else {sum+=p-vb+1;vo+=p-vb+1;}
				vb=p;
				preb=p;
			}
		}
		fprintf(fp1,"Case #%d: %d\n",m,sum);
		m++;
	}
	fclose(fp1);
    fclose(fp2);
	return 0;
}