#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
#define sz(x) ((int)(x).size())
#define len(x) ((int)(x).length())
#define all(x) (x).begin(),(x).end()
#define mp make_pair
#define fori(x,a,b) for(int x = (a) ; x < (b) ; (x)++)
#define forr(x,a,b) for(int x = (a)-1 ; x >= (b) ; (x)--)
#define fill(x,v) memset((x),(v),sizeof(x));
#define inRangeI(x,L,U) (x)>=(L)&&(x)<=(U)
#define inRangeE(x,L,U) (x)>(L)&&(x)<(U)

typedef unsigned long long ull;
typedef long long ll;

const double pi = acos(-1.0);

#define MAX 1001

void solution()
{
	int n;
	cin>>n;

	vector<long long> a(n),b(n);

	for (int i = 0; i < n ; i++)
	{
		cin>>a[i]>>b[i];
	}

	vector< vector<int> > flag( MAX , vector<int>(MAX) );
	for (int i = 0; i < n ; i++)
	{
		for (int j = 0; j < n ; j++)
		{
			flag[i][j] = 0;
		}
	}

	vector<long long> slope(n);

	for (int i = 0; i < n ; i++)
	{
			slope[i] = b[i]-a[i];
	}

	
	long long ans = 0;
	for (int i = 0; i < n ; i++)
	{
		for (int j = 0; j < n ; j++)
		{
			if( i != j && slope[i] != slope[j] && !flag[i][j])
			{
				//Point p1(0.0,1.0*a[i]),p2(1000.0,1.0*b[i]),p3(0.0,1.0*a[j]),p4(1000.0,1.0*b[j]);
				bool f = false;

				if( (a[i] > a[j] && b[i] < b[j]) || ( a[i] < a[j] && b[i] > b[j] ))
					f = true;

				//bool f = Point::SegmentsIntersect(p1,p2,p3,p4);
				if(f == true)
					ans += 1;

				flag[i][j] = 1;
				flag[j][i] = 1;
			}
		}
	}

	cout<<ans<<endl;
}

int main()
{
	//freopen("input.txt" , "r" , stdin);
	//freopen("A-small-attempt0.in" , "r", stdin);
	freopen("A-large.in" , "r" , stdin);
	//freopen("A-small-attempt2.in" , stdin);
	freopen("output.txt" , "w" , stdout);

	long long t;
	cin >> t;
	for (long long caseID = 1; caseID <= t ; caseID++)
	{
		cout<<"Case #"<<caseID<<": ";
		solution();	
	}
	return 0;
}
