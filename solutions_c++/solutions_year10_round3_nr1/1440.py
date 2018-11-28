#include <iostream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <sstream>
using namespace  std;
struct wind
{
	int left;
	int right;
};
wind d[1005];
int cmp(const wind&a,const wind&b)
{
	if (a.left!=b.left)
	{
		return a.left>b.left;
	}
	else
		return a.right>b.right;
}
int main()
{
	ifstream in("A-large.in");
	ofstream out("out.txt");
	int cases,count=1;
	in>>cases;
	while (cases--)
	{
		out<<"Case #"<<count++<<": ";
		int i,j,n;
		in>>n;
		for (i=0;i<n;++i)
		{
			in>>d[i].left>>d[i].right;
		}
		sort(d,d+n,cmp);
		int res=0;
		for (i=0;i<n;++i)
		{
			for (j=i+1;j<n;++j)
			{
				if (d[j].right>d[i].right)
				{
					res++;
				}
			}
		}
		out<<res<<endl;
	}
}