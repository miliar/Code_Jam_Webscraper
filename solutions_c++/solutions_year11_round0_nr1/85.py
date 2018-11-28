#include <iostream>
#include<stdio.h>
using namespace std;
char A[101];
int B[101];
int main (int argc, char * const argv[]) {
    int n;
	int t;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for(int caso=1;caso<=t;caso++)
	{
		cin>>n;
		for(int i=0;i<n;i++)
		{
			cin>>A[i];
			cin>>B[i];
		}
		int cont=0;
		int azul=1;
		int rojo=1;
		int ca=0,cr=0;
		int cual=0;
		while(cual<n)
		{
			
			while(1)
			{
				if(ca<cual)
				{
					ca=cual;
					continue;
				}
				if(ca==n)break;
				if(A[ca]=='O')
				{
					ca++;
					continue;
				}
				break;
			}
			while(1)
			{
				if(cr<cual)
				{
					cr=cual;
					continue;
				}
				if(cr==n)break;
				if(A[cr]=='B')
				{
					cr++;
					continue;
				}
				break;
			}
			
			if(A[cual]=='O')
			{
				if(azul<B[ca])azul++;
				if(azul>B[ca])azul--;
				if(rojo==B[cual])cual++;
				else
				{
				if(rojo<B[cual])rojo++;
				if(rojo>B[cual])rojo--;
				}
			}
			else {
				if(rojo<B[cr])rojo++;
				if(rojo>B[cr])rojo--;
				if(azul==B[cual])cual++;
				else{
				if(azul<B[cual])azul++;
				if(azul>B[cual])azul--;
				}
			}

			cont++;
		}
		
		cout<<"Case #"<<caso<<": "<<cont<<endl;
		
	}
    return 0;
}
