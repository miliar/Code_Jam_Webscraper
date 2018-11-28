#include <fstream>
#include <iostream>
#include <queue>
using namespace std;

int main()
{
	//ifstream inFile("input.txt");
	ifstream inFile("C-small-attempt0.in");
	ofstream outFile("output.txt");
	int caseNum;
	inFile>>caseNum;
	for (int i = 0; i < caseNum; i++)
	{
		int R, K, N;
		queue<int> visitorQueue;
		inFile>>R>>K>>N;
		for (int j = 0; j < N; j++)
		{
			int g;
			inFile>>g;
			visitorQueue.push(g);
		}
		long long amount = 0;
		for (int j = 0; j < R; j++)
		{
			int remainSeat = K;
			int remainGrpNum = N;
			int nextGrpNum = visitorQueue.front();
			while ((nextGrpNum <= remainSeat) && (remainSeat > 0) && (remainGrpNum > 0))
			{
				remainSeat -= nextGrpNum;
				amount += nextGrpNum;
				visitorQueue.pop();
				remainGrpNum--;
				visitorQueue.push(nextGrpNum);
				nextGrpNum = visitorQueue.front();
			}
		}
		outFile<<"Case #"<<i+1<<": "<<amount<<endl;
	}
	return 0;
}