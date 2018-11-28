#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <math.h>

using namespace std;

int T;
fstream	fin;
fstream fout;
long long R, K, N;
long long groupSize[1010];
long long euros[1010];
int visited[1010];
int period;
int beginPeriod, endPeriod;

void main()
{
	fin.open("z:\\input.txt", ifstream::in);
	fout.open("z:\\output.txt", ifstream::out);


	fin >> T;

	for(int t = 1; t <= T; t++) {
		fin >> R >> K >> N;
		for(int i=0; i<N; i++)
			fin >> groupSize[i];

		memset(visited, -1, sizeof(visited));
		period = 0;
		int startGroup = 0;
		while(visited[startGroup]==-1){
			period++;
			visited[startGroup]=period;
			
			int next=startGroup;
			long long seats = K;
			while(seats >= groupSize[next]){
				seats -= groupSize[next];
				next = (next+1)%N;
				if(next == startGroup)
					break;
			}
			euros[period] = K-seats;
			startGroup = next;
		}

		beginPeriod = visited[startGroup];
		endPeriod = period;
		period = endPeriod - beginPeriod + 1;

		long long totalEuros = 0;
		if(R < beginPeriod){
			for(int i=1; i<=R; i++)
				totalEuros += euros[i];
		}
		else{
			R = R - beginPeriod + 1;
			for(int i=1; i<beginPeriod; i++)
				totalEuros += euros[i];
			long long eurosInAPeriod=0;
			for(long long i=beginPeriod; i<=endPeriod; i++)
				eurosInAPeriod += euros[i];
			totalEuros += (R/period)*eurosInAPeriod;
			for(long long i=(R%period); i>0; i--)
				totalEuros += euros[i+beginPeriod-1];
		}
		fout << "Case #" << t <<": " << totalEuros << endl;
	}

	fin.close();
	fout.close();
}