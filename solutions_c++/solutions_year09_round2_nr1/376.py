#include <iostream>
#include <algorithm>
#include <sstream>
#include <set>
using namespace std;
struct node 
{
	double prob;
	string st;
	
	node *ok, *notok;
	node ()
	{
		st = "";
		ok = NULL; notok = NULL;
	}	
};

double change (string q)
{
	istringstream in (q);
	double ret;
	in >> ret;
	return ret;
}
void build (node *temp, string &s, int &pos)
{
	while (1){ //cout << pos << endl; getchar ();
		while (pos < s.size () && (s[pos] == ' ' || s[pos] == '\n')) pos ++;
	if (pos == s.size ()) return;
	if (s[pos] == ')'){ pos ++; return;}
	if (isdigit(s[pos]) || s[pos] == '.')
	{
		string s2;
		while (isdigit(s[pos]) || s[pos] == '.')s2 += s[pos++];
	temp -> prob = change (s2);
	};
	
	if (isalpha(s[pos]))
	{
		string s2;
		while (isalpha(s[pos]))s2 += s[pos++];
		temp -> st = s2;
	}
	
	if (s[pos] == '(')
	{
		if (temp -> ok == NULL)
		{
			temp -> ok = new node;
			pos ++;
			build (temp -> ok, s, pos);
		}
		else
		{
			temp -> notok = new node;
			pos ++;
			build (temp -> notok, s, pos);
		}		
	
	}
	}
	
}
set <string> m;

double trav (node *temp, double prob)
{
	
	if (temp == NULL) return prob;
	
	//cout << temp -> prob << endl; getchar();
	
	prob *= (temp-> prob);
	//cout << temp -> st << " " << *m.find (temp -> st) << endl; getchar();
	if (m.find (temp -> st) != m.end()) {
		if (temp -> ok == NULL) return prob;
		return trav(temp -> ok ,prob );}
	  
		if (temp -> notok == NULL) return prob;
	return trav(temp -> notok , prob);
}

void solve()
{
	string s = "", s1;
	int k , i ;
	scanf ("%d\n", &k);
	for (i =0; i < k; i++)
	{
		getline (cin, s1);
		s+= s1;
	}
	//cout << s << endl;
	node opa;
	int pos = 1;
	build(&opa, s, pos);
	
	int q, r;
	scanf ("%d", &q);
	for (i = 0; i< q ; i ++)
	{
		m.clear();
		cin >>s1;
		cin >> r;
		while (r--)
		{
			cin >> s1; m.insert (s1);
		}
		double ret = trav (&opa, 1.0);
	printf ("%.7lf\n", ret);
		//cout << ret << endl;
	}
	
} 

int main ()
{
	int o, i;
	scanf ("%d\n", &o);
	for (i = 1; i <= o; i++)
	printf ("Case #%d:\n", i), solve ();
	
	return 0;
}