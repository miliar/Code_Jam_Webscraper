#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

void main()
{
	ifstream inp("Input.txt");
	ofstream out("Output.txt");

	int T;
	inp>>T;
	for (int i=0;i<T;++i)
	{
		__int64 R,K;int N;__int64 sum=0;
		vector <int>g;int li=0;
		inp>>R>>K>>N;
		for(int j=0;j<N;++j)
		{
			int gi;
			inp>>gi;
			g.push_back(gi);
		}
		__int64 j=0;
		while(j<R)
		{
			__int64 rsum=0;int sli=li;
			while(rsum<=K &&(rsum==0||sli!=li))
			{
				__int64 temprsum=rsum+g[li];				
				if(temprsum>K)goto mm;
				rsum=temprsum;
				if(li==g.size()-1)li=0;
				else li++;
			}
mm:
			
			sum=rsum+sum;
			++j;
		}
		
		out<<"Case #"<<i+1<<": "<<sum<<"\n";
	}
	
}