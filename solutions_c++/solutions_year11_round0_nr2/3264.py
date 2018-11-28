#include <iostream>
#include <fstream>
#include <vector>
#include <deque>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <functional>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <memory>
#include <sstream>

using namespace std;

int t, c, d, n, t1, c1, d1, n1, i, j, len, charIndex;

char Com[26][26], result[100];

bool Opo[26][26], isFind;

int CharCnt[26];

string str;

int main()
{
	freopen("D://1.in", "rb", stdin);
	freopen("D://1.out", "wb", stdout);
	cin >> t;
	for(t1 = 1; t1 <= t; t1++)
	{
		len = 0;
		memset(Com, -1, sizeof(Com));
		for(i = 0;i < 26;i++) for(j = 0;j < 26;j++) Opo[i][j] = false;
		memset(CharCnt, 0, sizeof(CharCnt));
		cin >> c;
		for(c1  = 1; c1 <= c;c1++)
		{
			cin >> str;
			Com[str[0] - 'A'][str[1] - 'A'] = Com[str[1] - 'A'][str[0] - 'A'] = str[2];
		}

		cin >> d;
		for(d1 = 1; d1 <= d; d1++)
		{
			cin >> str;
			Opo[str[0] - 'A'][str[1] - 'A'] = Opo[str[1] - 'A'][str[0] - 'A'] = true;
		}

		cin >> n, cin >> str;
		
		for(n1 = 0; n1 < n; n1++)
		{
			charIndex = str[n1] - 'A';
			if(n1 == 0 || len == 0) 
			{
				CharCnt[charIndex]++;
				result[0] = str[n1];
				len++;
				continue;
			}
			if(Com[charIndex][result[len - 1] - 'A'] != -1)
			{
				CharCnt[result[len - 1] - 'A']--;
				result[len - 1] = Com[charIndex][result[len - 1] - 'A'];
				CharCnt[result[len - 1] - 'A']++;
				continue;
			}
			isFind = false;
			for(i = 0;i < 26;i++)
			{
				if(Opo[charIndex][i] && CharCnt[i] > 0) 
				{
					memset(CharCnt, 0, sizeof(CharCnt));
					len = 0, isFind = true;
					break;
				}
			}
			if(isFind) continue;
			len++,result[len - 1] = str[n1],CharCnt[charIndex]++;
		}
		cout << "Case #" << t1 << ": [";
		for(i = 0; i< len;i++)
		{
			if(i == len - 1) cout << result[i];
			else cout << result[i] << ", ";
		}
		cout << "]" << endl;
	}
	//while(1);
};


