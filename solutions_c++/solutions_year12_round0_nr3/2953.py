#include <fstream>
using namespace std;
ifstream f("input");
ofstream g("output");
unsigned a,b,n,m,t,i,j,v[11],nrc,aux,ok,q,bun,ii,qq,zero;
bool viz[2000001];
int main()
{
	f>>t;
	for(j=1;j<=t;j++)
	{
		f>>a>>b;
		bun=0;
		while(a<b)
		{
			nrc=0;
			aux=a;
			while(aux)
				v[10-nrc]=aux%10,aux/=10,nrc++;
			nrc--;
			i=10-nrc;
				for(ii=i+1;ii<=10;ii++)	
				{
					n=0;
					if(v[ii]!=0)
					{
						for(qq=ii;qq<=10;qq++)
								n=n*10+v[qq];
							for(qq=i;qq<ii;qq++)
								n=n*10+v[qq];
							if(n<=b&&viz[n]==0&&n>a)viz[n]=1,bun++;
						
				
					}

				}
						for(zero=0;zero<=b+1;zero++)viz[zero]=0;
			a++;
			
		}
		g<<"Case #"<<j<<": "<<bun<<'\n';
		
	}
	f.close();
	g.close();
}