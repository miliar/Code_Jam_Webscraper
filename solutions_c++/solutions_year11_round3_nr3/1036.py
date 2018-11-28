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
#include <cassert>

using namespace std;

typedef vector <string> vs;
typedef vector <int> vi;
#define clr(x) memset((x), 0, sizeof(x))
#define SORT(x) sort(x.begin(),x.end())
#define forn(i, n) for(int i = 0; i< n; i++)
#define all(i, x) for(int i = 0; i< x.size(); i++)
const long double EPS = 1e-11;


int T,N,L,H;
long long a[101];
int main()
{

	freopen("C-small-attempt2.in","r",stdin);freopen("C-small-attempt2.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
//	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
//	freopen("test.txt","r",stdin);
//  freopen("test.out","w",stdout);

//	int i,j;
	cin>>T;
	for(int caseID = 1; caseID <= T; caseID++)
	{	
		cout<<"Case #"<<caseID<<": ";

		cin>>N>>L>>H;
		forn(i,N)
		{
			cin>>a[i];
		}
		int poss = 1;
		long long num = -1;
		for(long long i = L; i<= H; i++)
		{
			poss = 1;
			forn(j,N)
			{
				if((i >= a[j] && i%a[j] == 0) || ((i < a[j] && a[j]%i == 0)))
					poss = 1;
				else
				{
					poss = 0;
					break;
				}
			}
			if(poss)
			{
				num = i;
				break;
			}
		}
		if(num == -1)
			cout<<"NO";
		else
			cout<<num;
		cout<<endl;		
	}
//	while(1);

	return 0;
}