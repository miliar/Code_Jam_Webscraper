
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<string.h>
using namespace std;
int main()
{

	int t;
	cin >> t;
	map<char,char> lang;
	lang['y']='a';
	lang['n']='b';
	lang['f']='c';
	lang['i']='d';
	lang['c']='e';
	lang['w']='f';
	lang['l']='g';
	lang['b']='h';
	lang['k']='i';
	lang['u']='j';
	lang['o']='k';
	lang['m']='l';
	lang['x']='m';
	lang['s']='n';
	lang['e']='o';
	lang['v']='p';
	lang['z']='q';
	lang['p']='r';
	lang['d']='s';
	lang['r']='t';
	lang['j']='u';
	lang['g']='v';
	lang['t']='w';
	lang['h']='x';
	lang['a']='y';
	lang['q']='z';


	char c;
	scanf("%c",&c);
	for(int i=0;i<t;i++)
	{
		char g[110];
		int a=scanf("%[^\n]",g);
		scanf("%c",&c);
		int j;
		for(j=0;j<strlen(g);j++)
		{
			if(lang.find(g[j])!=lang.end())	
				g[j]=lang[g[j]];
		}
		cout << "Case #" << i+1 << ": " << g << endl;
	}

	return 0;
}
