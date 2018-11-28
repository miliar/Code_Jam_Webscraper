

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <map>
using namespace std;


map<int,int> m[11];
int trs(int k,int b)
{
	int ret=0;
	while(k)
	{
		ret+=(k%b)*(k%b);
		k/=b;
	}
	return ret;
}
bool ishappy(int k,int b)
{
	if(m[b].find(k)!=m[b].end())
	{
		if(m[b][k]==1)
			return true;
		else
			return false;
	}
	int t=trs(k,b);
	if(t==1)
	{
		m[b][k]=1;
		return true;
	}
	m[b][k]=0;
	if(ishappy(t,b))
	{
		m[b][k]=1;
		return true;
	}
	return false;
}
int main()
{
	ifstream inf("A-small-attempt0.in");
	ofstream outf("out.txt");

	int T;
	inf>>T;
	string str;
	getline(inf,str);

	for(int t=0;t<T;t++)
	{
		int a[10];
		int n=0;
		int k;
		getline(inf,str);
		stringstream ss(str);
		while(ss>>k)
		{
			a[n++]=k;
		}
		for(int r=2;;r++)
		{
			int h=1;
			for(int i=0;i<n;i++)
			{
				if(!ishappy(r,a[i]))
				{
					h=0;
					break;
				}
			}
			if(h)
			{
				outf<<"Case #"<<t+1<<": "<<r<<endl;
				break;
			}
			;
		}
	}
	return 0;
}
