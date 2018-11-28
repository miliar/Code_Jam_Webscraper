#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	int t,n,k,m;
	fstream in,out;
	in.open("c:\\A-small-attempt1.in");
	if(in.fail())
		cout<<"asdf"<<endl;
	out.open("c:\\aaa.out");
	in>>t;
	for(int i=1;i<=t;i++)
	{
		in>>n>>m;
		bool *a=new bool[n];
		for(k=0;k<n;k++)
			a[k]=0;
		int j=0,cnt=0;
		while(true)
		{
			if(!a[0])
			{
				a[0]=true;
				cnt++;
				for(k=0;a[k]&&k<n;k++);
				if(k==n)
					break;
			}
			else
			{
				for(k=0;a[k]&&k<n;k++);
				if(k==n)
					break;
				else
				{
					for(j=0;j<k;j++)
						a[j]=false;
					a[k]=true;
					cnt++;
				}
			}
		}
		out<<"Case #"<<i<<": ";
		if(m%(cnt+1)==cnt)
			out<<"ON";
		else
			out<<"OFF";
		out<<endl;
	}
	return 0;
}
