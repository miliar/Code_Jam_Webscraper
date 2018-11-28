#include<stdio.h>
#include<string>

using namespace std;
int T[2][100];
int a=0,b=0;
int lastb,lasto;
void check(int x);
int main()
{
	FILE *f,*g;
	f=fopen("input","r");
	g=fopen("output","w");
	
	int nrO=0,nrB=0;
	int k;
	char c;
	int aux;
	int n;
	string buffer;

	fscanf(f,"%d\n",&n);
	for(int i=0;i<n;i++)
	{
		fscanf(f,"%d ",&k);
		for(int j=0;j<k;j++)
		{
			fscanf(f,"%c ",&c);
			fscanf(f,"%d ",&aux);
			if(c=='O')
			{
				T[0][j]=aux;
				T[1][j]=0;
			}
			else
			{
				T[1][j]=aux;
				T[0][j]=0;
			}
			
		}
		lastb=1;
		lasto=1;
		for(int x=0;x<k;x++)
			check(x);
		fprintf(g,"Case #%d: %d\n",(i+1),a>b?a:b);
		a=0;
		b=0;
	}
	fcloseall();
}

void check(int x)
{
	int aux;
	if(T[1][x])
	{
		aux=T[1][x]-lasto;
		lasto=T[1][x];
		if(aux<0)aux=aux*(-1);
		aux++;
			if((aux+a)<(b+1)) 
				{

					a=b+1;
				}
				else
					a+=aux;
		
	}
	else
	{
		
		aux=T[0][x]-lastb;
		lastb=T[0][x];
		if(aux<0)aux=aux*(-1);
		aux++;
		
			if((aux+b)<(a+1)) b=a+1; 
				else
					b+=aux;
		
		
	}
	 
	T[1][x]=0;
	T[0][x]=0;
}