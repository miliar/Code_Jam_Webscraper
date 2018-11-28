#include <string>       
#include <vector>       
#include <set>       
#include <map>       
#include <algorithm>       
#include <math.h>       
#include <sstream>       
#include <ctype.h>       
#include <queue>       
#include <stack>       
#include <iostream> 
#include <gmp.h>	// if GMP is not allowed, I apologize
#include <fstream>
using namespace std;

int N, K;

int check(vector<string> v, char c)
{

for(int i=0; i<N; i++)
for(int j=0; j<N; j++)
{
	int cur=0;
	for(int k=0; j+k < N && v[i][j+k]==c; k++)cur++;
	if(cur >= K) return 1;
}

for(int i=0; i<N; i++)
for(int j=0; j<N; j++)
{
	int cur=0;
	for(int k=0; i+k < N && v[i+k][j]==c; k++)cur++;
	if(cur >= K) return 1;
}


for(int i=0; i<N; i++)
for(int j=0; j<N; j++)
{
	int cur=0;
	for(int k=0; i+k < N && j+k < N && v[i+k][j+k]==c; k++)cur++;
	if(cur >= K) return 1;
}


for(int i=0; i<N; i++)
for(int j=0; j<N; j++)
{
	int cur=0;
	for(int k=0; i-k >-1 && v[i-k][j+k]==c; k++)cur++;
	if(cur >= K) return 1;
}

return 0;

}


int main()
{

fstream In("a-large.in", ios::in);
fstream Out("a-large.out", ios::out);

int tests;

In >> tests;

for(int h=0; h<tests; h++)
{



In >> N >> K;
vector<string> v(N), rot(N, string(N, '.'));

for(int i=0; i<N; i++) In >> v[i];

for(int i=0; i<N; i++) for(int j=0; j<N; j++)
{
	rot[j][N-i-1]= v[i][j];
}

for(int i=0; i<N; i++)
{	int cur = N-1;
	for(int j=N-1; j>-1; j--)
	{
		if(rot[j][i]!='.')
		{	char c = rot[j][i];
			rot[j][i] = '.';
			rot[cur--][i] = c;
			
		}
	}
}

int B=check(rot, 'B'), R = check(rot, 'R');


Out << "Case #" << h+1 << ": " << (B&R ? "Both" : B ? "Blue" : R ? "Red" : "Neither") << endl;

}

In.close();

Out.close();

return 0;

}
 
