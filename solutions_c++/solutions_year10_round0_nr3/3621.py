#include <bitset>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;
int solve(int r, int k, int n, vector<int>& v)
{
	vector<int> gs; //group start index
//	vector<int> ge; //group end index
	vector<int> gz; //group size		
	
	int cs=0, sumpl=0; //current group index
	bool l = false;	
	for (int i=1; i<=r && !l; ++i )
	{	
		int cp = 0;
		for(int j=cs;;++j)
		{
			if (i!=1 && cs==0)			
			{
				l = true;
				break;
			}
			
			bool reset = false;
			if(j>=v.size())
			{
				j = j % v.size();
				reset = true;
			}

				
			cp += v[j];
			if (cp>k || (j==cs && reset))
			{
				gz.push_back(cp - v[j]);
				gs.push_back(cs);
				cs = j;
				j = j-1;
				if (j<0)
					j += v.size();
				//ge.push_back(j-1);
				break;
			}
		}		
	}
	
	for(int i=0; i<gz.size(); ++i)
		sumpl += gz[i];

	if(!l)
		return sumpl;
	
	sumpl *= r / gz.size();
	for(int i=1; i<=(r % gz.size());++i)
		sumpl += gz[i-1];

	return sumpl;
}


int main(int argc, char* argv[])
{
	ifstream in(argv[1]);
	int r, n, k, t;
	in>>t;

	int c = 0;
	// write to file
	ofstream o("c.out");
	while(t--)
	{
		in>>r>>k>>n;
		
		vector<int> v;
		do{
			int z;
			in>>z;
			v.push_back(z);
		}while(--n);		
	
		int s = solve(r,k,n,v);
		o<<"Case #"<<++c<<": " << s <<endl;
		cout<<"Case #"<<c<<": " << s <<endl;
	}
}
