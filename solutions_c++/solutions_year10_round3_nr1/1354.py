# include <iostream>
# include <fstream>
# include <vector>
# include <algorithm>
# include <map>

using namespace std;

int main(int argc,char * argv[])
{
	int cas=0,T;
	ifstream in(argv[1]);
	ofstream out("out");
//	ifstream in("A-small.in");

	in>>T;

	while(T--)
	{
		int N;
		in>>N;

		vector<int> vix;
		vector<int> viy;

		for(int i = 0;i<N;i++)
		{
			int x,y;
			in>>x>>y;
			vix.push_back(x);
			viy.push_back(y);
		}

		int c = 0;

		for(int i = 0;i<vix.size();i++)
		{
			for(int j = i+1;j<viy.size();j++)
			{
				if((vix[j]<vix[i] && viy[j]>viy[i]) || (vix[j]>vix[i] && viy[j]<viy[i]))
					c++;
			}

		}

			out<<"Case #"<<++cas<<": ";
			out<<c;
			out<<endl;
	}

	return 0;
}

