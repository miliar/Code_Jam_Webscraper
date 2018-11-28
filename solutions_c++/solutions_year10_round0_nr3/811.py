#include <iostream>
#include <fstream>
#include <vector>
#include <map>

using namespace std;

int g[1000];
bool e[1000]; //exist
int s[1000]; 
int h[1000]; 

int main()
{
	int T, R, k, N;
	long long result;
	ifstream ifs("C-large.in");
	ofstream ofs("C-large.out");
	
	ifs >> T;
	for(int i=0;i<T;i++)
	{
		ifs >> R >> k >> N;
		for (int j=0;j<N;j++)
		{
			ifs >> g[j];
			e[j] = false;
		}
		int c = 0;
		int money;
		result=0;
		int r=0;
		while (!e[c] && r<R)
		{
			e[c]=true;
			s[c]=r;
			money=0;
			int count=0;
			while (money+g[c]<=k && count<N)
			{
				money += g[c];
				c = (c+1)%N;
				count++;
			}
			h[r]=money;
			result+=money;
			r++;
		}
		if (r<R)
		{
			int circle = r-s[c];	
			int re=(R-r)%circle;
			int qu=(R-r)/circle;
			long long a=0;
			long long b=0;
			for (int j=s[c];j<r;j++)
			{
				a+=h[j];
				if (j<s[c]+re)
					b+=h[j];
			}
			result+=a*qu;
			result+=b;
		}

		ofs << "Case #" << i+1 << ": " << result << endl;

	}

	ifs.close();
	ofs.close();
	return 0;
}
