#include <iostream>
#include <fstream>
#include <set>
using namespace std;

ifstream in("C.in");
ofstream out("C.txt");

int main()
{
	int C, R;
	in>>C;
	for (int c=1; c<=C; c++)
	{
		set<long long> bacterias;
		
		in>>R;
		for (int r=0; r<R; r++)
		{
			int x1, y1, x2, y2;
			in>>x1>>y1>>x2>>y2;
			for (int x=x1; x<=x2; x++)
				for (int y=y1; y<=y2; y++)
					bacterias.insert(x*1000000+y);
		}

		int second=0;
		while (!bacterias.empty())
		{
			set<long long> bacterias2;
			
			set<long long>::iterator it;
			for (it=bacterias.begin(); it!=bacterias.end(); it++)
			{
				int x=(*it)/1000000;
				int y=(*it)%1000000;
				
				if (bacterias.find((x-1)*1000000+y)!=bacterias.end()
				|| bacterias.find(x*1000000+y-1)!=bacterias.end())
					bacterias2.insert(*it);
				
				if (bacterias.find(x*1000000+y+1)==bacterias.end()
				&& bacterias.find((x-1)*1000000+(y+1))!=bacterias.end())
					bacterias2.insert(x*1000000+y+1);
			}
			
			bacterias=bacterias2;
			second++;
		}
		
		out<<"Case #"<<c<<": "<<second<<endl;
	}
    return 0;
}
