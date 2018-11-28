#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<iostream>
#include<string>
#include<sstream>
#include<ctype.h>
#include<vector>
#include<map>
#include<queue>
#include<math.h>
#include<algorithm>
#include<set>

#define pb push_back
#define PI acos(-1.0)
#define SZ(a) (int)a.size()
#define csprnt printf("Case #%d: ", cas++);
#define EPS 1e-9
#define MAX 100010
#define ll long long
#define INF (1<<30)
#define pii pair<int, int>
#define MP make_pair

using namespace std;

map<char, char>mp;

int main()
{
	freopen("small.in", "r", stdin);
	freopen("output.out", "w", stdout);
    int t, cas=1;
    scanf("%d ", &t);
    mp['a']='y', mp['b']='h', mp['c']='e', mp['d']='s', mp['e']='o', mp['f']='c', mp['g']='v', mp['h']='x', mp['i']='d', mp['j']='u',
    mp['k']='i', mp['l']='g', mp['m']='l', mp['n']='b', mp['o']='k', mp['p']='r', mp['q']='z', mp['r']='t', mp['s']='n', mp['t']='w',
    mp['u']='j', mp['v']='p', mp['w']='f', mp['x']='m', mp['y']='a', mp['z']='q';
    while(t--)
    {
    	string inp;
    	getline(cin, inp);
    	int len, i, j, k;
    	len = SZ(inp);
    	for(i=0;i<len;i++)
    	{
    		if(inp[i]>='a' && inp[i]<='z')
				inp[i] = mp[inp[i]];
    	}
    	csprnt;
    	cout<<inp<<endl;
    }
    return 0;
}

