#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main()
{

fstream In("c-large.in", ios::in);
fstream Out("c-large.out", ios::out);

int tests;

In >> tests;

for(int h=0; h<tests; h++)
{
cout << h << endl;
int R, N, K;

In >> R >> K >> N;

vector<int> riders(N), money(N), nextride(N);

for(int i=0; i<N; i++) In >> riders[i];

for(int i=0; i<N; i++)
{
	int j=i, cur = 0;
	
	for(int m=0; cur + riders[j] <= K && m<N; j=(j+1)%N,m++) cur += riders[j];
	
	money[i] = cur;
	nextride[i] = j;
}

vector<int> visited(N, 0);
int cur = 0, onecount = 0;
int secondvisit=1e9, thirdvisit=1e9;
long long ret = 0;
for(int i=0; R; R--, i++)
{
	if(visited[cur]==2 && thirdvisit > 1e8) thirdvisit = i-secondvisit;
	else if(visited[cur]==1 && secondvisit > 1e7) secondvisit = i;

	if(R % thirdvisit == 0) break;
	visited[cur]++;
	ret += money[cur];
	cur = nextride[cur];
}

for(int i=0; i<N; i++)
	if(visited[i] > 1)
		ret += ((long long)money[i])*((long long)R/thirdvisit);
	

Out << "Case #" << h+1 << ": " << ret << endl;

}

In.close();

Out.close();

return 0;

}
 
