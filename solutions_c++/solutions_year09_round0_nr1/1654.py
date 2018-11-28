#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <fstream>

using namespace std;


int main() 
{
    freopen("A-large.in", "r", stdin);
    ofstream fp("A-large.out");

    int L, D, N;
	cin >> L >> D >> N;
	//cout<< L << D << N << endl;
	vector<string> dic(D);
	int i, j, k;
	for(i = 0; i < D; i++)
	{
		cin >> dic[i];
		//cout << dic[i] <<endl;
	}
	bool exist[26][15] = {};
	string token;
	int cnt = 0;
	for(i = 1; i <= N; i++)
	{
		cin >> token;
		//cout << token << endl;
		k = 0;
		memset(exist, 0, sizeof(exist));
		for(j = 0; j < L; j++)
		{
			if( token[k] == '(' )
			{
				k++;
				char ch;
				while((ch = token[k++]) != ')')
				{
					exist[ch - 'a'][j] = true;
				}
			}
			else
			{
				exist[token[k++] - 'a'][j] = true; 
			}
		}
		cnt = 0;
		for(j = 0; j < D; j++)
		{
			bool mark = true;
			for(k = 0; k < L; k++)
			{
				if(!exist[dic[j][k] - 'a'][k])
				{
					mark = false;
					break;
				}
			}
			if(mark) 
			{
				cnt++;
			}
		}
		fp << "Case #" << i << ": " << cnt <<endl;
	}
    fp.close();
    return 0;
}
