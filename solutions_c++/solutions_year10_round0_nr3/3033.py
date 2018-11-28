#include <fstream>
#include <vector>

using namespace std;

int main()
{
	ifstream in("in.txt");
	ofstream out ("out.txt");
	int t;
	in >> t;
	vector <long long> g;
	long long r,k,n,temp,sum;
	long long kol,pos;
	for(int i=0;i<t;i++)
	{
		pos=0;
		in >> r>> k >> n;
		g.resize(n);
		sum=0;
		kol=0;
		for(int j=0;j<n;j++)
		{
			in >> g[j];
			sum+=g[j];
		}
		if(sum<=k)
		{
			out << "Case #" << i+1 << ": "<< sum*r <<endl;
			continue;
		}
		for(int j=0;j<r;j++)
		{
			temp=0;
			while(temp+g[pos]<=k)
			{
				temp+=g[pos];
				pos++;
				pos%=n;
			}
			kol+=temp;
		}
		out << "Case #" << i+1 << ": "<< kol <<endl;
	}
	return 0;
}