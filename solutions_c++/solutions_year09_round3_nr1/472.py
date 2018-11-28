#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
#include <set>
#include <vector>
#include <map>

#define mn(a,b) ((a<b) ? (a) : (b))
#define mx(a,b) ((a<b) ? (b) : (a))
#define ab(a) ((a<0) ? (-(a)) : (a))
#define fr(a,b) for(int a=0; a<b; ++a)
#define fe(a,b,c) for(int a=b; a<c; ++a)
#define fw(a,b,c) for(int a=b; a<=c; ++a)
#define df(a,b,c) for(int a=b; a>=c; --a)
#define BIG 1000000000
#define SMALL -1000000000

using namespace std;

char buf[100];
bool used[100];
int mas[100];
map<char,int> alpha;

void get_line(string &s)
	{
	gets(buf);
	s.assign(buf);
	}

int main()
{
freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);
int t;
scanf("%d\n", &t);
string s;
fr(x,t)
	{
	alpha.clear();
	memset(used,0,sizeof(used));
	memset(mas,0,sizeof(mas));
	get_line(s);
	int maxim = 1;
	used[1] = true;
	alpha[s[0]] = 1;
	mas[0] = 1;
	if(s.length()==1) 
		{
		printf("Case #%d: %d\n", x+1,1);
		continue;
		}
	int n = s.length();
	fe(i,1,n)
		{
		map<char,int>::iterator it = alpha.find(s[i]);
		if(it==alpha.end())
			{
			int p = 0;
			while(used[p]) p++;
			mas[i] = p;
			alpha[s[i]] = p;
			used[p] = true;
			if(p>maxim) maxim = p;
			}
		else
			{
			pair<char,int> p = *it;
			mas[i] = p.second;
			}
//		cout<<"Symbol analysis: "<<s[i]<<" "<<mas[i]<<endl;
		}		
	int base = maxim+1;	
	long long ans = 0;
	fr(i,n)
		ans = ans*base+mas[i];
	cout<<"Case #"<<(x+1)<<": "<<ans<<endl;	
	}
return 0;
}
