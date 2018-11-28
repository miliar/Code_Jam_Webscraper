#include <iostream>
#include <queue>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	ifstream ifile("D:\\C-small-attempt1.in");
	ofstream ofile("D:\\C-small-attempt1.out");
	int T;
	ifile >> T;
	for(int num = 0; num < T; num++)
	{
		int R,k,N;
		ifile >> R >> k >> N;
		queue<int> q;
		int sumTmp = 0;
		for(int i = 0; i < N; i++)
		{
			int tmp;
			ifile >> tmp;
			q.push(tmp);
			sumTmp += tmp;
		}

		int totalSum = 0;		
		if(sumTmp <= k)
		{
			totalSum = sumTmp*R;
		}
		else
		{
			while(R--)
			{
				int sum = 0;
				while((sum + q.front()) <= k)
				{
					sum += q.front();
					q.push(q.front());
					q.pop();
				}
				totalSum += sum;
			}
		}
		
		ofile << "Case #" << num+1 << ": " << totalSum << endl;
	}

	ifile.close();
	ofile.close();
	return 0;
}