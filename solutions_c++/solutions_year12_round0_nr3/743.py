#include<math.h>
#include<stdio.h>
#include<memory.h>
#include<string.h>
FILE*in=fopen("input.txt","r");
FILE*out=fopen("output.txt","w");
int T;
int A,B;
char buf1[101];
int L,L2;
bool V[10000001];
int Ans;
int main()
{
	int t,k,c,i,j;
	fscanf(in,"%d",&T);
	for(t=1;t<=T;t++)
	{
		fscanf(in,"%d %d",&A,&B);
		memset(V,0,sizeof(V));
		Ans=0;
		for(k=A;k<=B;k++)
		{
			if(V[k]) continue;
			sprintf(buf1,"%d",k);
			L=strlen(buf1);
			c=1; L2=L; i=k;
			V[k]=1;
			while(--L)
			{
				j=i;
				i=(j%10)*(int)pow((double)10,L2-1)+(j/10);
				if(!V[i]&&A<=i&&i<=B) V[i]=1,c++;
			}
			Ans+=(c*(c-1))/2;
		}
		fprintf(out,"Case #%d: %d\n",t,Ans);
	}
}