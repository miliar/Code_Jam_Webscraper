#include<iostream>

/*
 * Reads from stdin and writes to stdout
 *
 * Usage: program < input.txt > output.txt
 */

using namespace std;

const int L = 256;

char comb[L][L];
bool opp[L][L];

int main()
{
	int T;
	cin >> T;
	for(int t = 0 ; t < T ; t++)
	{
		cerr << "Test #" << t + 1 << "...\n";
		int C , D , N;
		char buff[1000] , ret[1000];
		int cnt = 0;
		for(int i = 0 ; i < L ; i++)
			for(int j = 0 ; j < L ; j++)
			{
				comb[i][j] = ' ';
				opp[i][j] = 0;
			}
		cin >> C;
		for(int i = 0 ; i < C ; i++)
		{
			cin >> buff;
			comb[buff[0]][buff[1]] = buff[2];
			comb[buff[1]][buff[0]] = buff[2];
		}
		cin >> D;
		for(int i = 0 ; i < D ; i++)
		{
			cin >> buff;
			opp[buff[0]][buff[1]] = 1;
			opp[buff[1]][buff[0]] = 1;
		}
		cin >> N >> buff;
		for(int i = 0 ; i < N ; i++)
		{
			char cur = buff[i];
			if(cnt > 0 && comb[ret[cnt - 1]][cur] != ' ')
			{
				ret[cnt - 1] = comb[ret[cnt - 1]][cur];
				continue;
			}
			bool flag = 0;
			for(int i = 0 ; i < cnt ; i++)
				if(opp[ret[i]][cur])
					flag = 1;
			if(flag)
				cnt = 0;
			else
				ret[cnt++] = cur;
		}
		cout << "Case #" << t + 1 << ": [";
		for(int i = 0 ; i < cnt ; i++)
		{
			cout << ret[i];
			if(i != cnt - 1)
				cout << ", ";
		}
		cout << "]\n";
	}
}




