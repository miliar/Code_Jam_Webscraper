#include <fstream>
#include <queue>
using namespace std;

void main()
{
	ifstream fin;
	ofstream fout;

	fin.open("A.in");
	fout.open("A.out");

	long long cases;
	fin >> cases;

	long long round, capacity, groups, groupsize;
	long long total, earn, temp;

	queue<long long> groupqueue;
	queue<long long> tempq;

	for(long long i = 1; i <= cases; i++)
	{
		fin >> round >> capacity >> groups;
		for(long long j = 0; j < groups; j++)
		{
			fin >> groupsize;
			groupqueue.push(groupsize);
		}
		total = 0;
		for(long long j = 0; j < round; j++)
		{
			earn = 0;
			temp = groupqueue.front();
			earn += temp;
			while(earn <= capacity)
			{
				groupqueue.pop();
				tempq.push(temp);
				if(groupqueue.empty()) break;
				temp = groupqueue.front();
				earn += temp;
			}
			if(!groupqueue.empty()) earn -= temp;
			total += earn;
			while(!tempq.empty())
			{
				groupqueue.push(tempq.front());
				tempq.pop();
			}
		}
		fout << "Case #" << i << ": " << total << endl;
		while(!groupqueue.empty())
		{
			groupqueue.pop();
		}
	}
}