#include <iostream>
#include <fstream>

using namespace std;

int gcd(int x,int y)
{
	return (x%y==0)?y:gcd(y,x%y);
}

int main()
{
	int t,n,x,y,i,a,c,d,b,e;
	freopen("input.txt","r",stdin);
	fstream fout("out.txt");
	cin>>t;
	for( i = 1 ; i <= t ; i++)
	{
		cin>>n>>x>>y;
		if(x!=0)
		{
			e = gcd(100,x);
			a = x/e;
			b = 100/e;
			if(y!=0)
			{
				e = gcd(100,y);
				c = y/e;
				d = 100/e;
				if((c==d&&a==b)||(c<d&&b<=n)) fout<<"Case #"<<i<<": Possible"<<endl;
				else fout<<"Case #"<<i<<": Broken"<<endl;
			}
			else fout<<"Case #"<<i<<": Broken"<<endl;
		}
		else 
		{
			if(y==0) fout<<"Case #"<<i<<": Possible"<<endl;
			else fout<<"Case #"<<i<<": Broken"<<endl;
		}
		/*if(c==d)	
		{
			//if(a==b)	printf("Case #%d: Possible\n",i);
			//else	printf("Case #%d: Broken\n",i);
		}
		else
		{
			//if(b<=n)	printf("Case #%d: Possible\n",i);
			//else printf("Case #%d: Broken\n",i);
		}*/
	}
	return 0;
}