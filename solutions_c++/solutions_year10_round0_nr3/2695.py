#include<iostream.h>
#include<fstream.h>
#include<list>
#include<functional>   

typedef __int64 longint;

int main()
{
	ifstream is;
	ofstream os;
	
	is.open("C-small-attempt0.in");
	os.open("outC");
	
	int t, n, in;
	longint r, k, y;

	is>>t;
	for(int rc=1; rc<=t; rc++)
	{
		list<int> g;
	
		is>>r;
		is>>k;
		is>>n;
		
		for(int i=0; i<n; i++)
		{
			is>>in;
			g.push_back(in);	
		}
		y = 0;
		for(int j=0; j<r; j++)
		{
			int nc = 1;
			longint& f = g.front();
			longint val = 0;
			while((val + f) <= k && nc <= n)
			{	
				val += f;
				g.pop_front();
				g.push_back(f);
				f = g.front();
				nc++;
			}
			y += val;
		}
		os<<"Case #"<<rc<<": "<<y<<endl;
		//cout<<"Case #"<<rc<<": "<<y<<endl;
	}

	os.flush();

	is.close();
	os.close();
	
	return 0;
}

