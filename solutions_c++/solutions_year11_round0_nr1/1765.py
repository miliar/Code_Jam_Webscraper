#include <iostream>
#include <cmath>

using namespace std;

int testNum = 0;
int n;
int result;
char type[10000];
int place[10000];

int pO, timeO;
int pB, timeB;

void read()
{
	cin >> n;
	result = 0; // for next case
	int i;
	for (i=0; i < n; ++i)
	{
		do{
			cin >> type[i];
		}while(type[i] == ' ');
		cin >> place[i];
	}
}

void printOut()
{
	cout << "Case #" << testNum << ": " << result << "\n";
}
void solve()
{
	read();
	pO = pB = 1;
	timeO = timeB = 0;
	int i;
	for (i=0;i<n;++i)
	{
		if (type[i] == 'O')
		{
			result = max(result, timeO + abs(pO - place[i])) + 1; // +1 stands for pressing
			pO = place[i];
			timeO = result;
		}
		else
		{
			result = max(result, timeB + abs(pB - place[i])) + 1;// +1 stands for pressing
			pB = place[i];
			timeB = result;
		}
	}
	printOut();
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	while(t)
	{
		++testNum;
		solve();
		--t;
	}
return 0;
}