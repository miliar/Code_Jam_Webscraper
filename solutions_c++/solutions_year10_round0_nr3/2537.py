#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <queue>

using namespace std;


int main()
{
	const char* iFileName = "C-small-attempt0.in";
	//const char* iFileName = "C-large.in";
	const char* oFileName = "out3.txt";

	ifstream iFile(iFileName);
	ofstream oFile(oFileName);
	int N;
	iFile >> N;
	for(int caseNum=1; caseNum<=N; ++caseNum)
	{
		long long round, cap, n;
		iFile >> round >> cap >> n;
		queue<int> q;
		for(long long i=0; i<n; ++i)
		{
			int tmp;
			iFile >> tmp;
			q.push(tmp);
		}

		long long res = 0;
		for(long long i=0; i<round; ++i)
		{
			long long cnt = 0;
			for(long long j=0; j<n; ++j)
			{
				if(cnt + q.front() <= cap)
				{
					cnt += q.front();
					res += q.front();
					q.push(q.front());
					q.pop();
				}
				else
				{
					break;
				}
			}
		}
		oFile << "Case #" << caseNum << ": ";
		oFile << res << endl;
	}
	return 0;
}