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



//0 add
//1 mul
//2 sub
int isugly(ll a)
{
	return (a%2==0) ||(a%3==0)||(a%5==0)||(a%7==0);
}
ll ans=0;
int N;
string S;

ll get(string S)
{
	ll res=0;
	for(int i=0;i<S.size();i++)
		res=res*10+S[i]-'0';

	return res;
}

void rec(int index, ll sum, string current)
{
       if (index==S.length())
       {
           if (current.length()> 0)
                 sum += get(current);
		   if (isugly(sum))
                   ans++;
               return;
        }
        if (current.length() > 0)
        {
              rec(index,sum+get(current), "");
              rec(index, sum-get(current), "");
        }
        rec(index+1,sum,current+S[index]);
}

int main()
{
	freopen("B-small.in","r",stdin);
	freopen("A-smallch.out","w",stdout);
    int cases;
	scanf("%d\n",&cases);
	int i,j,k,P,K,L;
	for (int cas = 0; cas < cases; cas++)
    {
		char s[50];
		scanf(" %[^\n]",s);
		N=strlen(s);
		string str(s,s+N);
		S=str;
		ans=0;
		rec(0,0,"");
        cout << "Case #" << cas + 1 << ": " << ans << "\n";
    }
    return 0;
}
