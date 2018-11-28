#include<iostream>
#include<set>
#include<string>
#include<algorithm>
using namespace std;
#define forn(i,n) for(int i = 0; i < n; i++)

int tset[1000];
int ti;

int main()
{
	freopen("C:\\1.txt","rt",stdin);
	freopen("C:\\2.txt","wt",stdout);
	int T;
	cin >> T;
	for(int test = 0; test < T; test++)
	{
		int rev = 0;
		string s;
		cin >> s;
		int n = s.length();
		ti = 0;
		for(int i = n - 1; i >= 0; i--)
		{
			if ( s[i] < s[i+1] ) 
			{
				int j, tmp, k;
				for(j = 0; j < ti; j++) if ( tset[j] > s[i] ) break;
				tmp = s[i];
				s[i] = tset[j];
				tset[j] = tmp;
				sort(tset,tset+ti);
				for(j = i + 1, k = 0; k < ti ; j++,k++) s[j] = tset[k]; 
				rev = 1;
				break;
			}
			else tset[ ti++] = s[i];
		}
		cout << "Case #" << test + 1 << ": ";
		if ( rev == 1 ) cout << s;
		else
		{
			int mini = '9' + 1, minr;
			for(int i = 0; i < n; i++) if ( s[i] > '0' && s[i] < mini ) 
			{
				mini = s[i];
				minr = i;
			}
			cout << char(mini);
			cout << '0';
			s.erase(minr,1);
			sort(s.begin(),s.end());
			cout << s;
		}
		cout << endl;
	}
		return 0;
}