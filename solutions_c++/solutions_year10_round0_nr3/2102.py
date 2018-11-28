#include<queue>
#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	ifstream in;
	ofstream out;
	in.open("C-small-attempt1.in");
	out.open("out.txt");
	int T,n,k,r,s=0;
	in>>T;
	while (T--)
	{
		int i,j,a;
		queue<int> g;
		long long sum=0;
		long long total=0;
		in>>r>>k>>n;
		s++;
	    for (i=0;i<n;i++)
		{
			in>>a;
			g.push(a);
		    total+=a;
		}
		if (total<=k) {
			total*=r;
			out<<"Case #"<<s<<": "<<total<<endl;
			continue;
		}
		total=0;
		while (r>0)
		{
			int front=g.front();
			while (sum+front<=k) {
				sum+=front;
				g.pop();
				g.push(front);
				front=g.front();
			}
		 r--;
		 total+=sum;
		 sum=0;
		}
	out<<"Case #"<<s<<": "<<total<<endl;	
	}	
	return 0;
}
