#include<iostream>
#include<cmath>
#include<fstream>
using namespace std;

int main()
{
	char inp;
	int taso[105],tasb[105],limt[105];
	int sto,stb,i,k=0,n,t,tao,tab,timus;
	int os,bs,temp;
	ifstream cin("A-large.in");
	ofstream cout("A-large.out");
	cin>>t;
	while(t--)
	{
		cin>>n;
		tao=tab=-1;
		for(i=0;i<n;++i)
		{
			cin>>inp;
			if(inp=='O')
			{
				cin>>taso[++tao];
				limt[i]=1;
			}
			else
			{
				cin>>tasb[++tab];
				limt[i]=0;
			}
		}
		timus=0;
		sto=stb=1;
		os=bs=0;
		i=0;
		while(n--)
		{
			//if(os>tao||bs>tab)
			//	break;
			if(limt[i]==1)
			{

				temp=abs(taso[os]-sto)+1;
				timus+=temp;
				if(abs(tasb[bs]-stb)<=temp)
				{
					stb=tasb[bs];
				}
				else if(tasb[bs]-stb>0)
				{
					stb+=temp;
				}
				else stb-=temp;
				sto=taso[os];
				++os,++i;
			}
			else
			{
				temp=abs(tasb[bs]-stb)+1;
				timus+=temp;
				if(abs(taso[os]-sto)<=temp)
				{
					sto=taso[os];
				}
				else if(taso[os]-sto>0)
				{
					sto+=temp;
				}
				else sto-=temp;
				stb=tasb[bs];
				++bs,++i;
			}
		}
		cout<<"Case #"<<++k<<": "<<timus<<endl;
	}
    return 0;
}
