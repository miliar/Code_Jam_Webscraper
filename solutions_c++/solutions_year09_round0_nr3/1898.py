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

VI w , e , l , c , o , m , t , d , j , a , sp;
int ans;
string s;


void count_seq (int p , int nxt)
{
	if (nxt == 20)	
	{
		ans ++;
		ans %= 10000;
		return;
	}
	
	VI possible_next;
	if (nxt == 2)	
	{
		FORZ (i , e.sz)	
			if (e[i] > p)	possible_next.PB (e[i]);
	}
	else if (nxt == 3)	
	{
		FORZ (i , l.sz)	
			if (l[i] > p)	possible_next.PB (l[i]);
	}
	else if (nxt == 4)
	{
		FORZ (i , c.sz)	
			if (c[i] > p)	possible_next.PB (c[i]);
	}
	else if (nxt == 5)	
	{
		FORZ (i , o.sz)	
			if (o[i] > p)	possible_next.PB (o[i]);
	}
	else if (nxt == 6)	
	{
		FORZ (i , m.sz)	
			if (m[i] > p)	possible_next.PB (m[i]);
	}
	else if (nxt == 7)	
	{
		FORZ (i , e.sz)	
			if (e[i] > p)	possible_next.PB (e[i]);
	}
	else if (nxt == 8)	
	{
		FORZ (i , sp.sz)	
			if (sp[i] > p)	possible_next.PB (sp[i]);
	}
	else if (nxt == 9)	
	{
		FORZ (i , t.sz)	
			if (t[i] > p)	possible_next.PB (t[i]);
	}
	else if (nxt == 10)	
	{
		FORZ (i , o.sz)	
			if (o[i] > p)	possible_next.PB (o[i]);
	}
	else if (nxt == 11)	
	{
		FORZ (i , sp.sz)	
			if (sp[i] > p)	possible_next.PB (sp[i]);
	}
	else if (nxt == 12)	
	{
		FORZ (i , c.sz)
			if (c[i] > p)	possible_next.PB (c[i]);
	}
	else if (nxt == 13)
	{
		FORZ (i , o.sz)	
			if (o[i] > p)	possible_next.PB (o[i]);
	}
	else if (nxt == 14)	
	{
		FORZ (i , d.sz)	
			if (d[i] > p)	possible_next.PB (d[i]);
	}
	else if (nxt == 15)	
	{
		FORZ (i , e.sz)	
			if (e[i] > p)	possible_next.PB (e[i]);
	}
	else if (nxt == 16)	
	{
		FORZ (i , sp.sz)	
			if (sp[i] > p)	possible_next.PB (sp[i]);
	}
	else if (nxt == 17)	
	{
		FORZ (i , j.sz)	
			if (j[i] > p)	possible_next.PB (j[i]);
	}
	else if (nxt == 18)	
	{
		FORZ (i , a.sz)	
			if (a[i] > p)	possible_next.PB (a[i]);
	}
	else if (nxt == 19)	
	{
		FORZ (i , m.sz)	
			if (m[i] > p)	possible_next.PB (m[i]);	
	}
	
	if (possible_next.empty())	
		return;
	else 
	{
		FORZ (i , possible_next.sz)	
			count_seq (possible_next[i] , nxt + 1);
	}
	return;
}



string length_four (int x)
{
	char ch[10] = {'\0'};
	sprintf (ch , "%d" , x);
	string ret = ch;
	while (ret.sz < 4)	ret = "0" + ret;
	return ret;
}


int main ()
{	
	int T = GI;
	getchar ();
	FORZ (test , T)
	{
		printf ("Case #%d: " , test + 1);
		s.clear();
		w.clear();e.clear();l.clear();c.clear();o.clear();m.clear();t.clear();d.clear();j.clear();a.clear();sp.clear();
		ans = 0;
		
		getline (cin , s);
		
		FORZ (i , s.sz)	
		{	
			if (s[i] == 'w')	w.PB (i);			if (s[i] == 'e')	e.PB (i);			if (s[i] == 'l')	l.PB (i);			if (s[i] == 'c')	c.PB (i);
			if (s[i] == 'o')	o.PB (i);			if (s[i] == 'm')	m.PB (i);			if (s[i] == 't')	t.PB (i);			if (s[i] == 'd')	d.PB (i);
			if (s[i] == 'j')	j.PB (i);			if (s[i] == 'a')	a.PB (i);			if (s[i] == ' ')	sp.PB (i);
		}

		FORZ (i , w.sz)	
			count_seq (w[i] , 2);	
			
		string ANS = length_four (ans);	
		
		printf ("%s\n" , ANS.c_str());
	}
	return 0;
}

