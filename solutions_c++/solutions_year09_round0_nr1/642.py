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

string dic[5000];

int main ()
{
	/*freopen(inputfilename , "r" , stdin);*/
	/*freopen(outputfilename , "w" , stdout);*/

	int l, d, n;
	cin >> l >> d >> n;

	int i, j;
	for (i = 0; i < d ; i++)
		cin >> dic[i];
	//sort(dic , dic+d);

	for (i = 0; i < n ; i++)
	{
		cout << "Case #"<<i+1<<": ";
		string s;
		cin >> s;
		int a[15][30];
		memset(a , 0 , sizeof(a));
		int pos;
		for (j =0 , pos = 0 ; j< l ; j++ , pos++)
		{
			if (s[pos] == '(')
			{
				pos++;
				while(s[pos] !=')')
				{
					a[j][s[pos]-'a'] = 1;
					pos++;
				}
			}
			else a[j][s[pos]-'a'] = 1;
		}
		int ans = 0 ;
		for (j= 0; j < d; j++)
		{
			for( pos = 0; pos < l; pos++)
			{
				if (a[pos][dic[j][pos]-'a'] == 0) break;
			}
			if (pos == l) ans++;
		}
		cout << ans << endl;
	}
	return 0;
}

 
