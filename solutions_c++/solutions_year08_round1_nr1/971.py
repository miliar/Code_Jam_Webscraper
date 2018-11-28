#include<fstream>
#include<vector>
#include<string>
#include<algorithm>
using std::ifstream;
using std::ofstream;
using std::vector;
using std::sort;
using std::endl;
ifstream in;
ofstream out;
bool greater(const int &a,const int &b)
{
	return a>b;
}
int main()
{
	int T;
	int n;
	vector<int> x,y;
	in.open("input.txt");
	out.open("output.txt",std::ios::app);
	in>>T;
	for(int i=1;i<=T;++i)
	{
		int result=0;
		in>>n;
		for(int j=0;j<n;++j)
		{
			int temp;
			in>>temp;
			x.push_back(temp);
		}
		for(int j=0;j<n;++j)
		{
			int temp;
			in>>temp;
			y.push_back(temp);
		}
		sort(x.begin(),x.end(),greater);
		sort(y.begin(),y.end());
		for(int j=0;j<n;++j)
		{
			result=result+x.at(j)*y.at(j);
		}
		out<<"Case #"<<i<<": "<<result<<endl;
		x.clear();
		y.clear();
	}
	return 0;
}