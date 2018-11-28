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

typedef long long ll;



int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
    int cases;
	scanf("%d",&cases);
	int i,j,k,P,K,L;
	for (int cas = 0; cas < cases; cas++)
    {
		scanf("%d %d %d",&P,&K,&L);
		vector<int> Dic;
		for(i=0;i<L;i++)
		{
			int a;
			scanf("%d",&a);
			Dic.push_back (a);
		}
		sort(Dic.begin(),Dic.end());
		reverse(Dic.begin(),Dic.end());
		ll res=0;

		for(i=0;i<L;i++)
		{
			int mul=i/K;
			mul++;
			res+=(ll)Dic[i]*(ll)mul;
		}

		       
        cout << "Case #" << cas + 1 << ": " << res << "\n";
    }
    return 0;
}
