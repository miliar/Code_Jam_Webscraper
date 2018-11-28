/*#include <stdlib.h>
#include <stdio.h>

int comp(const void *p, const void *q)
{
    return (*(int *)p - *(int *)q);
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, i, j, x, y, t, a, b, c;
	char ch[100];
	scanf("%d ", &T);
	for (i = 0; i < T; i++)
	{
		for (j = 0; scanf("%c", &ch[j]) != -1; j++)
		{
			if (ch[j] <'0' || ch[j] > '9')
				break;
		}
		for (t = -1, x = j-1; x > 0; x--)
		{
			for (y = x-1; y>= 0; y--)
			{
				if (ch[x] > ch[y])
				{	
					t = ch[x];
					break;
				}
			}
			if (t > 0)
				break;
		}
		if (t > 0)
		{
			while (y < x)
			{
				ch[x] = ch[x-1];
				x--;
			}
			ch[x] = t;
		}
		else
		{
			ch[j++] = '0';
			ch[j] = 0;
			qsort(ch, j, sizeof(char), comp);
		}
		ch[j] = 0;
		printf("Case #%d: %s\n", i, ch);
	}
	return 0;
}*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

template <class A, class B> void convert(A& x, B& y) {stringstream s; s<<x; s>>y;}

int main() {
	ifstream cin("in.txt");
	//ifstream cin("A-small.in");
	//ifstream cin("A-large.in");
	ofstream cout("out.txt");
	int T, Case;
	int i, j, k;
	string s;
	for (cin>>T, Case=1; T; T--,Case++) {
		cin>>s;
		s = string(21-s.length(),'0') + s;
		next_permutation(s.begin(), s.end());
		cout<<"Case #"<<Case<<": ";
		for (i=0; i<s.size(); i++) {
			if (s[i]!='0') break;
		}
		for (; i<s.size(); i++) {
			cout<<s[i];
		}
		cout<<endl;
	}
}