#include <iostream>
using namespace std;

int _maxvalue = -1;

void combine(int t[], int n, int m)
{   
	int* order = new int[m + 1];    
	for (int i = 0; i <= m; i++)
		order[i] = i - 1;
	
	int k = m;
	bool flag = true;
	while (order[0] == -1)
	{
		if (flag)
		{   
			int patcount1 = -1, patcount2 = -1, seancount1 = -1, seancount2 = -1;
			for (int i = 0; i < n; i++)
			{
				int found = 0;
				for (int j = 1; j <= m; j++)
				{
					if (i == order[j])
					{
						found = 1;
						break;
					}
				}
				
				if (found) {
					if (patcount1 != -1)
						patcount1 = patcount1 ^ t[i];
					else
						patcount1 = t[i];
					
					if (seancount1 != -1)
						seancount1 += t[i];
					else
						seancount1 = t[i];
					
				}
				else
				{
					if (patcount2 != -1)
						patcount2 = patcount2 ^ t[i];
					else
						patcount2 = t[i];
					
					if (seancount2 != -1)
						seancount2 += t[i];
					else
						seancount2 = t[i];
				}
			}
			if (patcount1 == patcount2) {
				_maxvalue = max(seancount2, max(seancount1 , _maxvalue));
			}
			flag = false;
		}
		
		order[k]++;            
		if (order[k] == n)      
		{
			order[k--] = 0;
			continue;
		}     
		
		if (k < m)              
		{
			order[++k] = order[k-1];
			continue;
		}
		
		if (k == m)
			flag = true;
	}
	
	delete[] order;
}

int main (int argc, char * const argv[]) 
{
	freopen("input3.txt", "rt", stdin);
	freopen("output3.txt", "wt", stdout);
	
	int T; 
	cin >> T;
	
	int target[1000];
	for(int i = 0; i < T; i++) {

		int N;
		cin >> N;
		for (int j = 0; j < N; j++) {
			cin >> target[j];
		}
		
		_maxvalue = -1;
		
		for (int j = 1; j < N; j++) {
			combine(target, N, j);
		}
		
		cout << "Case #" << i+1 << ": ";
		
		if (_maxvalue == -1)
			cout << "NO" << endl;
		else {
			cout << _maxvalue << endl;
		}

	}
	
	return 0;
}

