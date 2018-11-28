#include<cstdio>
#include<algorithm>
#include<cmath>
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<string>
#include<climits>
#include<fstream>

using namespace std;

#define s(n)					scanf("%d",&n)
#define sf(n) 					scanf("%lf",&n)
#define ss(n) 					scanf("%s",n)
#define pb						push_back
#define mp	 					make_pair
#define fill(a,v) 				memset(a, v, sizeof(a))
#define SZ(v)					((int)(v.size()))
#define all(x)					x.begin(), x.end()
#define foreach(v,c)            for( typeof((c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define INDEX(arr,ind)			(lower_bound(all(arr),ind)-arr.begin())
#define FF						first
#define SS						second
#define T(t)           			int t;scanf ("%d",&t);while (t--)
#define INF						(int)1e9
#define LINF					(long long)1e18
#define FOR(i,a,b)				for(int i=a;i<b;i++)
#define REP(i,n)				FOR(i,0,n)

void debugarr(int * arr,int n)
{
	cout<<"[";
	for(int i=0;i<n;i++)
		cout<<arr[i]<<" ";
	cout<<"]"<<endl;
}

typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef long long LL;
typedef vector<LL> VLL;
typedef pair<int,int> PII;
typedef pair<LL,LL> PLL;
typedef vector<pair<int,int> > VPII;
typedef pair<double,double> PDD;

int main()
{
    int i;
    string str;
    string str1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string str2 = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	map<char, char> dict;
	for(i=0;i<str1.length();i++)
		dict[str1[i]] = str2[i];
	dict['q'] = 'z';
	dict['z'] = 'q';
    int n; s(n);
	getline (cin,str);
	REP(i,n)
	{
		getline (cin,str);
		cout << "Case #" << i+1<<": ";
		REP(j,str.length())
			printf("%c", dict.find(str[j])->SS);
		printf("\n");
	}
    return 0;
}
