#include  "iostream" 
#include  "string.h"
#include  "sstream"
#include  "cstdio"

using namespace std;
long long arr[1003];
long long ab[1003];
long long sum[1003];
int main()
{	

	freopen("C-largo.in", "r", stdin);
	freopen("Cjp.out", "w", stdout);

	int ca,r,k,n;
	//scanf("%d",&ca);
	cin>>ca;
	for(int i=1;i<=ca;i++)
	{
		//scanf("%d %d %d",&r,&k,&n);
		cin>>r>>k>>n;
		for(int ii=0;ii<n;ii++)
			cin>>ab[ii];
		long long res=0;
		memset(arr,0,sizeof arr);
		for(int i=0;i<n;i++)
		{
			sum[1003]=0LL;
		}
		int cont=1;
		//pos inicial
		int pos=0;
		long long ten=0;
		int ves=1;
		sum[0]=0;
		while(1)
		{
			if(ten==0)
			{
				//encontro ciclo
				if(arr[pos]>0)
				{
					long long lon_cycle=ves-arr[pos];
					int ini=ves-lon_cycle;
					int fin=ves-1;
					long long sum_en_cycle=sum[fin]-sum[ini-1];
					long long queda=r-ves+1;
					long long resto=queda%lon_cycle;
					long long ciclos=queda/lon_cycle;
					res+=( (sum_en_cycle*ciclos));
					if(resto!=0)
						res+=sum[ini+resto-1]-sum[ini-1];
					break;
				}
				else
				{
					long long su=0LL;
					int in=pos;
					ten=0LL;
					int pode=1;
					while(ten+ab[pos]<=k)
					{
						ten+=ab[pos];
						su+=ab[pos];
						res+=ab[pos];
						pos++;
						pos%=n;
						pode++;
						if(pode>n)
							break;
					}
					/*cout<<su<<endl;*/
					//tengo hasta ahora
					sum[ves]=sum[ves-1]+su;
					//seteo la ves que lo encontre
					arr[in]=ves++;
				}
			}
			else
			{
				ten=0LL;
				cont++;
				if(cont>r)
					break;
			}
		}
		cout<<"Case #"<<i<<": ";
		cout<<res<<endl;
	}
	return 0;
}