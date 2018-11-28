#include <iostream>
#include <fstream>
#include <queue>
#include <algorithm>
#include <list>

using namespace std;

int main() 
{
	ifstream iff("in.txt");
	int t;
	iff>>t;
	ofstream off("out.txt");
	for(int z=0;z<t;++z)
	{
		int r,k,n;
		iff>>r>>k>>n;
		list<int> g;
		
		int e=0;
		for(int i=0;i<n;++i)
		{
			int l;
			iff>>l;
			g.push_back(l);
		}
		
		list<int>::iterator git=g.begin();

		for(int i=0;i<r;++i)
		{
			int s=0;
			int c=0;

			while(s<=k && c<n)
			{
				s+=*git;
				if(s>k) 
				{
					s-=*git;
					break;
				}
				git++;
				c++;
			}
			

			git=g.begin();
			for(int j=0;j<c;++j)
			{
				g.push_back(*git);
				git++;
			}

			while(c) 
			{
				g.pop_front();
				--c;
			}
			e+=s;
		}

		off<<"Case #"<<z+1<<": "<<e<<endl;
	}
	iff.close();
	off.close();
}