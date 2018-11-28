#include <iostream>
using namespace std;

int N,K,B,T;

int X[50],V[50];


void process_case(int z)
{
	int a,b;
	cin >> N >> K >> B >> T;
	for(int i = 0; i < N; i++)	
		cin >> X[i];
	
	for(int i = 0; i < N; i++)	
		cin >> V[i];

	int not_make = 0;
	int make = 0;
	int swaps = 0;
	for(int i = N-1; i >= 0 && make < K; i--)
	{
		int d = B - X[i];
		if((double)d/(double)V[i] > (double)T)
			not_make++;
		else
		{
			swaps += not_make;		
			make++;
		}
	}
	
	cout << "Case #" << z << ": ";
	if(make < K)
		cout << "IMPOSSIBLE" << endl;
	else
		cout << swaps << endl;
}

int main()
{
	int C;
	cin >> C;
	for(int i = 1; i <= C; i++)
		process_case(i);
	return 0;
}
