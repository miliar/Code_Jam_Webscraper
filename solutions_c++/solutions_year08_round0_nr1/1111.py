#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <set>
#include <stack>
#include <queue>
#include <map>
#include <strstream>
#include <cstdio>
#include <cstdlib>
#include <iomanip>

using namespace std;

ifstream in("a2.in");
ofstream out("a2.out");

string s[110];
string qu[1100];
char c[1100];
bool b[110];
int n,answer,q;
int hamar[1100];

int gtnel(string x)
{
	int L=0,R=n-1,m;
	while(L<=R)
	{
		m=(L+R)/2;
		if (s[m]==x)
			return m;
		if (s[m]>x)
			R=m-1;
		else
			L=m+1;
	}
	cout <<" EEE" << endl;
	return -1;
}

void anel()
{
	int i;
	sort(s,s+n);
	for (i=0;i<q;i++)
		hamar[i] = gtnel(qu[i]);
}

int find(int k)
{
	int i;
	for (i=0;i<n;i++)
		b[i] = false;
	int num = 0;
	for (i=k;i<q;i++)		
		if (b[hamar[i]] == false)
		{
			b[hamar[i]] = true;
			num++;
			if (num == n)
				return i;
		}
	return q;
}

void solve()
{
	int index = 0;
	answer = 0;
	while (index < q)
	{
		answer ++;
		index = find(index);		
	}
	answer--;
	if (q==0)
		answer = 0;
}

int main()
{
	int Test,i,j,num = 0,k;	
	in >> Test;
	while (Test>0)
	{
		num++;
		Test--;		
		in >> n;
		in.getline(c,1000);
		for (i=0;i<n;i++)
		{
			in.getline(c,1000);
			k = strlen(c);
			s[i] = "";
			for (j=0;j<k;j++)
				s[i] = s[i] + c[j];
		}
		in >> q;
		in.getline(c,1000);
		for (i=0;i<q;i++)
		{
			in.getline(c,1000);
			k = strlen(c);
			qu[i] = "";
			for (j=0;j<k;j++)
				qu[i] = qu[i] + c[j];
		}
		/*cout << "-------------S--------" << endl;
		for (i=0;i<n;i++)
			cout << s[i] << endl;
		cout << "-------------QU--------" << endl;
		for (i=0;i<q;i++)
			cout << qu[i] << endl;
		cout << endl;*/
		anel();		
		solve();
		out << "Case #" << num << ": " << answer << endl;
	}
	return 0;
}