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
	in.open("input.txt");
	out.open("output.txt",std::ios::app);
	int N;
	int P;
	int K;
	int L;
	int tmp;
	vector<int> frequency;
	in>>N;
	for(int i=1;i<=N;++i)
	{
		in>>P;
		in>>K;
		in>>L;
		for(int j=0;j<L;++j)
		{
			in>>tmp;
			frequency.push_back(tmp);
		}
		sort(frequency.begin(),frequency.end(),greater);
		int tmp1=0;
		int tmp2=L/K+1;
		for(int j=0;j<tmp2;++j)
		{
			for(int m=0;m<K;++m)
			{
				if((j*K+m)<(int)frequency.size())
				tmp1=tmp1+frequency.at(j*K+m)*(j+1);
			}
		}
		out<<"Case #"<<i<<": "<<tmp1<<endl;
		frequency.clear();
	}
	in.close();
	out.close();
	return 0;
}