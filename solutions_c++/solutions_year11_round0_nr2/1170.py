#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
using namespace std;

char com[26][26];
int opp[26][26];

void solve(int t)
{
	int c,d,n;
	int i,j,k;
	string str,ans;
	for(i = 0; i < 26; i++)
		for(j=0; j < 26; j++)
		{
			com[i][j] = '0';
			opp[i][j] = 0;
		}
	cin >> c;
	for(i = 0; i < c; i++)
	{
		cin >> str;
		com[str[0]-'A'][str[1]-'A'] = str[2];
		com[str[1]-'A'][str[0]-'A'] = str[2];
	}
	cin >> d;
	for(i = 0; i < d; i++)
	{
		cin >> str;
		opp[str[0]-'A'][str[1]-'A'] = 1;
		opp[str[1]-'A'][str[0]-'A'] = 1;
	}
	cin >> n;
	cin >> str;
	k = 0;
	for(i = 0; i < n; i++)
	{
		if(k == 0)
		{
			ans[k] = str[i];
			k++;
		}
		else
		{
			if(com[ans[k-1]-'A'][str[i]-'A'] != '0')
			{
				ans[k-1] = com[ans[k-1]-'A'][str[i]-'A'];
			}
			else
			{
				for(j = 0; j < k; j++)
				{
					if(opp[ans[j]-'A'][str[i]-'A'] == 1)
					{
						k=0;
						break;
					}
				}
				if(k != 0) ans[k++] = str[i];
			}
		}
	}

	cout << "Case #" << t << ": [";
    for (i = 0; i < k; i++)
	{
		if (i != 0) cout << ", ";
		cout  << ans[i];
	}
	cout << "]" << endl;
}



int main()
{
    int T,t;
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
	cin >> T;
	for(t = 1; t <= T; t++) solve(t);
}
