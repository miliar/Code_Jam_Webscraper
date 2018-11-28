#include<iostream>
#include<algorithm>
#include<cmath>
#include<string>
using namespace std;

int Btodec(int x,const int B)
{
   int ret=0,dig=0,tmp=x,bde=10;

   while(tmp>9)
   {
	   tmp = tmp/10;
	   dig++;
   }

   bde = pow(10,dig);

   for(int i=dig;i>=0;i--)
   {
	  tmp = x/bde;
	  ret += tmp*pow(B,i);
	  x=x-tmp*bde;
	  bde/=10;

   }

   return ret;
}

int main()
{
	int T,digs,l,m;
	string cad;
	char cad2[65];

	cin>>T;
	for(int i=0;i<T;i++)
	{
		cin>>cad;
		digs=0;
		for(int j=0;j<cad.size();j++)
		{
			if(j==cad.find_first_of(cad[j]))
				digs++;
		}
		if(digs==1)
			digs++;
		l=2;
		m=0;
		for(int k=0;k<cad.size();k++)
		{
		    if(cad.find_first_of(cad[k])<k)
			{
				cad2[k] = cad2[cad.find_first_of(cad[k])];
			}
			else
			{
				if(m==0)
				{
					cad2[k] = '1';
				}
				else
				{
					if(m==1)
					{
						cad2[k] = '0';
					}
					else
					{
					   cad2[k] = '0' + l;
					   l++;
					}
				}
				m++;
			}
		}
	    cad2[cad.size()]='\0';
		cout<<"Case #"<<i+1<<": "<<Btodec(atoi(cad2),digs)<<endl;
	}

	return 0;
}