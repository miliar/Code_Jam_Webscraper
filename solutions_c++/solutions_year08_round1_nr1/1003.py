#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <map>
#include <string>
#include <queue>

using namespace std;

#define DIST(x1, y1, x2, y2) (float)((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
#define SORT(x) sort(x.begin(),x.end());

ifstream fin("d:\\gcj\\q.in");
ofstream fout("d:\\gcj\\sol.out");
#define cin fin
#define cout fout

void Solution()
{
	int n = 0, j = 0;
	cin >> n;

	vector<int> X(n);
	vector<int> Y(n);
	for(j=0;j<n;++j)
	{
		cin >> X[j];
	}
	for(j=0;j<n;++j)
	{
		cin >> Y[j];
	}
	
	SORT(X);
	SORT(Y);
	reverse(Y.begin(), Y.end());

	int sum = 0;

	while(X.size() && X[0] < 0)
	{
		sum += X[0]*Y[0];
		X.erase(X.begin());
		Y.erase(Y.begin());
	}

	while(X.size())
	{
		sum += X[0]*Y[0];
		X.erase(X.begin());
		Y.erase(Y.begin());
	}

	cout << sum;


}

int main(int argc, TCHAR* argv[])
{
    int N = 0;
	cin >> N;

	vector<float> len(3,0);
	
	for(int i=0;i<N;++i)
	{
		cout << "Case #" << i+1 << ": ";
		Solution();
		cout << endl;
	}

	return 0;
}
