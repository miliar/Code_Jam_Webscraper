#include <iostream>
#include <fstream>
#include <vector>

#include <algorithm>

using namespace std;

int main(int argc, char* argv[])
{
	int loopCnt, googlerNum, surprising, minScore;

	ifstream ifile("B-large.in");
	ofstream ofile("res.txt");

	ifile >> loopCnt;
	for(int i=0;i<loopCnt;++i)
	{
		int ans = 0;
		vector<int> scores;
		ifile >> googlerNum >> surprising >> minScore;
		for(int j=0;j<googlerNum;++j)
		{
			int tmp;
			ifile >> tmp;
			scores.push_back(tmp);
		}
		sort(scores.begin(), scores.end());

		for(int j=scores.size()-1;j>=0;--j)
		{
			int val = scores[j] / 3;
			int md = scores[j] % 3;
			if(md >= 1)
				val++;
			if(val >= minScore)
			{
				ans++;
				continue;
			}
			else if(scores[j] > 1)
			{
				if(surprising == 0)
					break;
				else
				{
					surprising--;
					if(md == 2 || md == 0)
						val++;
					if(val >= minScore)
					{
						ans++;
					}
				}
			}
		}
		ofile << "Case #" << i+1 << ": " << ans << endl;
	}

	ifile.close();
	ofile.close();

	return 0;
}

