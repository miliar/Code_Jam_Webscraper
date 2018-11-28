#include <vector>
#include <cstdio>
#include <set>
#include <map>
#include <ctime>
#include <string>
#include <sstream>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <cstring>
#include <cctype>

#define inputfilename "input"
#define outputfilename "a.out"

using namespace std;

int main ()
{
	/*freopen(inputfilename , "r" , stdin);*/
	/*freopen(outputfilename , "w" , stdout);*/


	int number , times;
	cin >> number;
	for (times = 0 ; times <  number ; times++)
	{
		cout <<"Case #"<<times+1 <<": ";
		string s;
		cin >> s;
		int cnt[10];
		memset(cnt , 0 , sizeof(cnt));
		s = '0' + s;
		int pre  = s[s.length() - 1] - '0';
		int now;
		int i , j;
		for (i = s.length() - 1; i > 0 ; i--)
		{
			now = pre;
			pre = s[i - 1] - '0';
			cnt[now] ++;
			if (pre < now)
			{
				cnt[pre] ++;
				if (i > 2 ) cout << s.substr(1 , i - 2);
				for (j = pre+1 ; j <= 9 ; j++)
				{
					if (cnt[j] > 0 )
					{
						cnt[j] --;
						cout  << j;
						break;
					}
				}
				for (j = 0 ; j <= 9 ; j++)
				{
					while (cnt[j]--)
						cout << j;
				}
				cout << endl;
				break;
			}
		}
	}


	return 0;
}

 
