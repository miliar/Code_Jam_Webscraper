#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int arr[41];
int N;

void swap(int i, int j)
{
	int temp = arr[j];
	arr[j] = arr[i];
	arr[i] = temp;
}

int solve()
{
	int count = 0;
	for (int i = 0; i < N; ++i)
	{
		int j = i;
		while (arr[j] > j)
		{
			int t = j+1;
			while (arr[t] > j)
				t++;
			while (t != (j+1))
			{
				swap(t,t-1);	count++;
				--t;
			}
			swap(j,j+1);	count++;			
		}
	
		// cout << i << " target is " << target << endl;
				
	}
	return count;
}

int main()
{
	int T; cin >> T;
	for (int test = 1; test <= T; ++test)
	{
		cin >> N;		
		string s;
		getline(cin,s);
		for (int i = 0; i < N; ++i)
		{
			getline(cin,s);
			int m = 0;
			for (int j = 0; j < N; ++j)
				if (s[j] == '1')
					m = j;
			arr[i] = m;
		}
			
		cout << "Case #" << test << ": " << solve() << endl;
	}
	return 0;
}
