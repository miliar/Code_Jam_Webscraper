#include<fstream>
#include<vector>
#include<algorithm>
using namespace std;
ifstream in("recycled.in");
ofstream out("recycled.out");

int t, a, b, nrc, pw, sol;

vector<int>v;
vector<int>::iterator it;

void solve(int index)
{
	sol = 0;
	
	int uc;
		
	for(int nr = a; nr <= b; nr++)
	{
		int copy = nr;
		
		v.clear();
		
		for(int i=1; i<nrc; i++)
		{	
			uc = copy % 10;
			copy /= 10;
			copy = uc * pw + copy;
			
			v.push_back(copy);
		}
		
		sort(v.begin(), v.end() );
		unique(v.begin(), v.end() );
		
		for(it = v.begin(); it < v.end(); it++)
			if(a <= *it && *it < nr && nr <= b)
				sol++;
		
	}	

	out<<"Case #"<<index<<": "<<sol<<'\n';
}	

int main()
{
	in>>t;
	
	int i;
	
	for(i=1; i<=t; i++)
	{
		in>>a>>b;
		
		int aa = a;
		nrc = 0;
		
		while(aa > 0)
		{
			aa /= 10;
			nrc++;
		}
		
		pw = 1;
		for(int j=1; j<nrc; j++)
			pw *= 10;	

		solve(i);
	}

	in.close();
	out.close();
	return 0;
}	