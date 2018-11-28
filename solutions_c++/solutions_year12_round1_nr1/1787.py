#include <iostream>
#include <stdio.h>
#include <cmath>

using namespace std;

int tamanho(int A)
{
	return static_cast<int> (powf(2,A));
}


int main(int argc, char* argv[])
{
	int A,B,n,bandera,div,i,j,k,lim;
	float* pos;
	float ans,aux;
	freopen("s.in","rt+",stdin);
	freopen("s.out","w+",stdout);
	cin>>n;
	int tam;
	for(i=1;i<=n;i++)
	{
		cin>>A>>B;
		B++;
		tam=tamanho(A);
		pos=new float[tam];
		for(j=0;j<tam;j++)
		{
			pos[j]=1;
		}
		ans=0;
		div=tam;
		for(j=0;j<A;j++)
		{
			cin>>aux;
			div=div/2;
			bandera=1;
			for(k=0;k<tam;k++)
			{
				if(bandera <= div)
				{
					pos[k]=pos[k]*aux;
				}
				else
				{
					pos[k]=pos[k]*(1-aux);
				}
				bandera++;
				if(bandera== ((2*div)+1) )
				{
					bandera =1;
				}
			}
		}


		for(j=1;j<=A+1;j++)
		{
			aux=0;
			lim=(int) powf(2,j-1);
			for(k=0;k<tam;k++)
			{
				if(pos[k] !=0)
				{
					if(k<lim)
					{
						aux=aux+ (B-A+2*(j-1)) * pos[k];
					}
					else
					{
						aux=aux+(B-A+B+2*(j-1)) *pos[k];
					}
				}
			}
			if(aux<ans || ans==0)
			{
				ans=aux;
			}
		}
		aux=0;
		for(k=0;k<tam;k++)
		{
			aux=aux+ (B+1) * pos[k];
		}
		if(aux<ans || ans==0)
		{
			ans=aux;
		}

		//cout<<"Case #"<<i<<": "<<ans<<'\n';
		printf("Case #%d: %.6f\n",i,ans);
		delete pos;
	}
	fclose(stdin);
	fclose(stdout);

	return 0;
}

