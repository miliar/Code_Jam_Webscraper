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
    freopen("C-large.in", "r", stdin);
    ofstream fp("C-large.out");

	string wel = "welcome to code jam";
	long long memo[19][500] = {};

	int N;
	cin >> N;
	string str;
	getline(cin, str);
	for(int i = 0; i < N; i++)
	{
		//cin >> str;
		getline(cin, str);
		//cout << "Case" << i+1 << ":" << str << endl;
		memset(memo, 0, sizeof(memo));
		int m = str.size();
		if(str[0] == wel[0])
		{
			memo[0][0] = 1;
		}
		for(int k = 1; k < m; k++)
		{
			memo[0][k] = memo[0][k - 1];
			if(str[k] == wel[0])
			{
				memo[0][k] ++;
			}
		}
		for(int j = 1; j < 19; j++)
		{
			for(int k = j; k < m; k++)
			{
				memo[j][k] = memo[j][k - 1];
				if(str[k] == wel[j])
				{
					memo[j][k] += memo[j-1][k-1];
				}
				if(memo[j][k] > 10000) 
				{
					memo[j][k] -= 10000;
				}
				//cout << memo[j][k] << " ";
			}
			//cout << endl;
		}
		long long res = memo[18][m-1] % 10000;
		fp << "Case #" << i+1 << ": ";
		for(int k = 1000; k > 0; k /= 10)
		{
			fp << res / k;
			res %= k;
		}
		fp << endl;
	}

    fp.close();
    return 0;
}
