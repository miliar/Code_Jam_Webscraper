#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

int A,B,m,cncn;
char cn[8],cnc[8];
int len;

struct pairs
{
	int n1,n2;
}p[1000];
int pn=0;

int k;char temp;
void cycle()
{
	//printf("\n%s",cn);
	char temp=cn[len];
	for(k=len;k>0;--k)
	{
		cn[k]=cn[k-1];
	}
	cn[0]=temp;
	//printf("\n%s",cn);
}

void dupli_check(int &n)
{
	int i,j;
	for(i=0;i<pn-1;++i)
	{
		for(j=i+1;j<pn;++j)
		{
			if(p[i].n1==p[j].n1 && p[i].n2==p[j].n2)
				{
					//printf("\np1:%d %d\np2:%d %d",p[i].n1,p[i].n2,p[j].n1,p[j].n2);
					--n;
					break;
				}
		}

	}
}
int check()
{
	int i,j,n=0;
	for(i=A;i<B;++i)
	{
		sprintf(cn,"%d",i);
		strcpy(cnc,cn);
		for(j=0;j<len;++j)
		{
			cycle();
			cncn=atoi(cn);
			if( (i<cncn && A<=i && cncn<=B))// || (i>cncn && A<=cncn && i<=B) )
			{
				//if(check_existing())
					p[pn].n1=i;
					p[pn++].n2=cncn;
					n+=1;
				//printf("\n%s %s",cn,cnc);
			}
		}
	}
	dupli_check(n);
	return n;
}

int main() {

	int num_t;
	scanf("%d",&num_t);
	for(int l=1;l<=num_t;++l)
	{
		scanf("%d %d",&A,&B);
		sprintf(cn,"%d",A);
		len=strlen(cn)-1;
		printf("Case #%d: %d\n",l,check());
		pn=0;
	}
	return 0;
}
