#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
#include<cmath>
#define SIZE 3

using namespace std;

long prev[SIZE];

long cycle(long x, int l, int z)
	{
	int k=0; long y;
	if (z)
		{
		y=x;
		while (y%10==0)
			{			
			k++;
			y/=10;
			}
		}
	y=(x/pow(10,k+1));
	y+=(fmod(x,pow(10,k+1)))*pow(10,l-k-1);
	return (y);
	}	

main()
	{
	ifstream fin("C-small-attempt0.in");
	ofstream fout("output.in");
	int T;
	fin>>T;
	for (int t=0;t<T;++t)
		{
		long A, B;
		int pair=0;
		fin>>A;
		fin>>B;
		long a=A;
		int l=0;
		while (a)
			{
			++l;
			a/=10;
			}
		for (long n=A; n<=B; ++n)
			{
			prev[0]=prev[1]=prev[2]=0;
			long m=n;
			int z=0;
			while (m)
				{
				if (m%10==0)
					++z;
				m/=10;
				}
			m=n;
			for (int i=0; i<l-z-1; ++i)
				{
				m=cycle(m,l,z);
				prev[i]=m;
				if ((m>n) && (m<=B))
					{
					pair++;
					for (int j=0; j<i;++j)
					if (m==prev[j])
						pair--;
					}
				
				}
			}
		fout<<"Case #"<<t+1<<": "<<pair<<"\n";
		}	
	fin.close();
	fout.close();
	return 0;
	}
