#include <algorithm>
#include <iomanip>
#include <iostream>
#include <string>
using namespace std;
#define _USE_MATH_DEFINES	
#define s(n)                scanf("%d",&n)
#define sl(n)               scanf("%lld",&n)
#define sf(n)               scanf("%lf",&n)
#define ss(n)               scanf("%s",n)

#define FOR(i,a,b)          for(i=a; i<b; ++i)

#define REP(i,n)            for((i)=0;(i)<(int)(n);++(i))

struct debugger
{
    template<typename T> debugger& operator, (const T& v)
    {
        cerr<<v<<" ";
        return *this;
    }
} dbg;
template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
typedef long long 		   LL;



 double round(double x)
{
	const double sd = 100; 
	return int(x*sd + (x<0? -0.5 : 0.5))/sd;
}

const int MAXN=1000, MAXLEN=4;
int cc,T;
LL i,j,A,B,n,num,reformed_num,offset,multiplier,pos,answer;
char sz_num[MAXLEN];
bool used[MAXN];
int main()
{
  

	scanf("%d", &T);
	REP(cc,T)
	{
	
		scanf("%lld %lld", &A,&B);

		if ( A<=10 && B<=10 )
		{
			printf("Case #%d: 0\n", cc+1);
			continue;
		}

		answer = 0;
		memset(used, false, MAXN);
		FOR(i, A, B+1)
		{
			if (used[i])
				continue;

			used[i] = true;
			memset(sz_num, '\0', MAXLEN);

		
			num = i;
			pos = 0;
			while (num > 0)
			{
				sz_num[pos++] = num % 10;
		        num /= 10;
		    }

		
			int first_digit = -1;
			bool do_nothing = true;
			REP(j,pos)
			{
				if (j == 0)
					first_digit = sz_num[j];
				else if (sz_num[j] != first_digit)
					do_nothing = false;
			}
			if (do_nothing)
				continue;

		
			n = 0;
			REP(offset,pos)
			{
				reformed_num = 0;
				multiplier = 1;
				FOR(j,offset,offset+pos)
				{
					reformed_num += sz_num[j%pos] * multiplier;
					multiplier *= 10;
				}
				if (reformed_num >= A && reformed_num <= B)
				{
					used[reformed_num] = true;
					n++;
				}
			}
			answer += (n * (n-1)) / 2;
		}
		printf("Case #%d: %lld\n", cc+1,answer);
	}

    return 0;
}
