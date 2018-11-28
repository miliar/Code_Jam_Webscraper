#include <iostream>
#include <fstream>
#include <math.h>
#include <queue>
using namespace std;
int main()
{
	int cases;
	ifstream in("C-small-attempt0.in");
	ofstream out("out.txt");
	in>>cases;
	//cout<<cases<<endl;
	int count=1;
	while (cases--)	
	{
		out<<"Case #"<<count++<<": ";
		queue<int>q;
		int r,k,n,i;
		in>>r>>k>>n;
		int g;
		for (i=0;i<n;++i)
		{
			in>>g;
			q.push(g);
		}
		int sum=0;
		int temp,j,e;
		for (i=1;i<=r;++i)
		{
			temp=k;
			e=0;
			while (!q.empty()&&e<n)
			{
				j=q.front();
				if (temp>=j)
				{
					temp-=j;
					e++;
				}
				else
				{
					break;
				}
				q.pop();
				q.push(j);
			}
			sum+=k-temp;
		}
		out<<sum<<endl;
	}
}