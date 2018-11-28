#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;

//convert string to integer
int toInteger(string s)
{
	const char* r = s.c_str();
	return atoi(r);
}


int main()
{
	ifstream fin("B-large.in");
	ofstream fout("3x.out");

	int T=0;
	string s;
	getline(fin, s);
	T=toInteger(s);

	for(int t=1; t<=T; t++)
	{
		int N=0, S=0, p=0;
		fin>>N>>S>>p;

		vector<int> score;int x=0;
		bool* surprising = new bool[N];
		for (int i=0;i <N;i ++)
		{
			surprising[i]=false;
			fin>>x;
			score.push_back(x);
		}

		sort(score.begin(), score.end());

		int number=0;
		for(int i=score.size()-1; i>=0; i--)
		{
			int q=score[i]/3;
			int r=score[i]%3;

			if (q>=p)
			{
				number++;
				continue;
			}

			if (r==0 && score[i]!=0)
			{
				if (q+1>=p && S>0)
				{
					number++;
					S--;
					continue;
				}
			}
			if (r==1)
			{
				if (q+1>=p)
					number++;
				continue;
			}
			if (r==2)
			{
				if (q+1>=p)
				{
					number++;
					continue;
				}
				else
				if (q+2>=p && S>0)
				{
					number++;
					S--;
					continue;
				}
			}
		}

		fout<<"Case #"<<t<<": "<< number <<"\n";

	}

	return 0;
}