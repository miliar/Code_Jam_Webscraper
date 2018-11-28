#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;

int sign(int x)
{
	if(x > 0) return 1;
	else return -1;
}

int main(void)
{
	int T;
	
	cin >> T;
	for(int numCase = 1; numCase <= T; numCase++)
	{
		vector<int> o, b;
		vector<char> next;
		int N;
		
		cin >> N;
		for(int i = 0; i < N; i++)
		{
			char robot;
			int number;
			
			cin >> robot >> number;
			if(robot == 'O') o.push_back(number);
			else b.push_back(number);
			
			next.push_back(robot);
		}
		
		int op = 1, bp = 1, ob = 0, bb = 0, tt = 0;
		for(size_t i = 0; i < next.size(); i++)
		{
			if(next[i] == 'O')
			{
				int t = abs(op - o[ob]) + 1;
				op = o[ob++];
				if((unsigned int)bb < b.size()) bp = (abs(bp - b[bb]) <= t ? b[bb] : bp + sign(b[bb] - bp) * t);
				tt += t;
			}
			else
			{
				int t = abs(bp - b[bb]) + 1;
				bp = b[bb++];
				if((unsigned int)ob < o.size()) op = (abs(op - o[ob]) <= t ? o[ob] : op + sign(o[ob] - op) * t);
				tt += t;
			}
		}
		
		cout << "Case #" << numCase << ": " << tt << endl;
	}
}
