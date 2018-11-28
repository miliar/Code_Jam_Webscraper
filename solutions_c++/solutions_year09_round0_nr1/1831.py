#include <vector>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <set>
#include <cmath>
using namespace std;

#define GI ({int t ;scanf("%d",&t);t;})
#define FORZ(i,n) for(typeof(n)i=0;i<n;i++)
#define all(x) (x).begin(),(x).end()
#define PB push_back
#define sz size()
#define FF first
#define SS second
typedef vector<int> VI;
typedef pair<int,int> pII;
typedef vector<string> VS;


VS tokenize (string s)
{
	VS ret;
	int i = 0 , j;
	while (i < s.sz)
	{
		string t;
		for (j = i ; j < s.sz && s[j] != '(' ; j ++)
		{
			t = "";
			if (s[j] >= 'a' && s[j] <= 'z')	
				t += s[j];
			if (!t.empty())	
				ret.PB (t);
		}
		
		t = "";
		for ( ; j < s.sz && s[j] != ')' ; j ++)	if (s[j] >= 'a' && s[j] <= 'z')	t += s[j];
		if (!t.empty())	ret.PB (t);
		i = j + 1;
	}
	
	FORZ (k , ret.sz) sort (all(ret[k]));	
	return ret;	
}


int main ()
{
	int L = GI , D = GI , N = GI;
	vector <VS> pat(N);
	VS dic(D);
	
	FORZ (i , D)	cin >> dic [i];
	FORZ (i , N)	
	{
		string s;
		cin >> s;
		pat[i] = tokenize (s);
	}
		
	
	FORZ (i , N)
	{
		printf ("Case #%d: " , i + 1);
		int c = 0;
		
		//FORZ (k , pat[i].sz)	cout << pat[i][k] << " ";
		//cout << "\n";
		
		FORZ (j , D)
		{
			string s = dic[j];
			int p = 0;
			while (p < s.sz)
			{
				if ( binary_search ( all(pat[i][p]) , s[p] ) )	p ++;
				else break;
			}
			if (p >= s.sz)	
			{
				//cout << s << "\n";
				c ++;
			}
			//cout << "\n";
		}
		printf ("%d\n" , c);	
	}
	
	return 0;
}

