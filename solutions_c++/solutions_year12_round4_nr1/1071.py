#include<iostream>
#include<fstream>
using namespace std;
#define maxn 90000
int min(int a,int b)
{
	if (a>b) 
		return b;
	else
		return a;
}

int max(int a,int b)
{
	if (a>b) 
		return a;
	else
		return b;
}
	int d[maxn],p[maxn],t[maxn];
int main()
{
	int i,j,ta,tt,n,last;

	ifstream in;
	ofstream out("d:/A-large.out");

	in.open ("d:/A-large.in");
    in>>ta;
	for (tt=1;tt<=ta;tt++)
	{
		in>>n;
		for (i=1;i<=n;i++)
		{
			in>>d[i]>>t[i];
			p[i]=0; 
		}
		in>>last;
		p[0]=min(d[1],t[1]);d[0]=0;
		for (i=1;i<=n;i++)
		{
			for (j=0;j<i;j++)
			{
				if (p[j]>=d[i]-d[j])
				{
					p[i]=max(	min(t[i],d[i]-d[j]),p[i]	);
				}
			}
		}
		int get=0;
		for (i=0;i<=n;i++)
			if (last-d[i]<=p[i])
			{
				get=1;
				break;
			}

		if (get==1) out<<"Case #"<<tt<<": YES"<<endl;
		else out<<"Case #"<<tt<<": NO"<<endl;
	}
}