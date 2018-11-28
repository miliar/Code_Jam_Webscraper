//--BY--©--PROKSIK----------------------------------------------------------------------
#include<iostream>

#include<algorithm>
#include<vector>
#include<string>
#include<queue>
#include<stack>
#include<map>
#include<set>

#include<stdio.h>
#include<ctype.h>
#include<math.h>
#include<stdlib.h>

using namespace std;

#define FOR(i,a,b) for(int i=a; i<=b; i++)
#define FORD(i,a,b) for(int i=a; i>=b; i--)
#define REP(i,a,b) for(int i=a; i<b; i++)

#define PB push_back
#define PII pair<int, int>
#define MP make_pair
#define fi first
#define se second

#define SIZE(s) (s).size()

#define INF 123456789
#define ll long long int
//--------------------------------------------------------------------------------------

#define MAX_BIN 30

typedef vector<bool> tBin;

void write(tBin B)
{
	FORD(i,SIZE(B)-1,0)
		putchar( (B[i]) ? '1' : '0');
	putchar('\n');
}


tBin toBin(int c)
{
	tBin B = vector<bool>(MAX_BIN,false);
	int i = 0; 
	while(c > 0)
	{
		B[i] = (c%2);
		i++;
		c/=2;
	}
	return B;
}

int toInt(tBin B)
{
	int res = 0;
	int m = 1;
	
	//write(B);
	
	FOR(i,0,MAX_BIN-1)
	{
		res+= m*(B[i]);
		m*= 2;
	}
	return res;
}



tBin sum(int a, int b)
{
	tBin A = toBin(a);
	tBin B = toBin(b);
	tBin res = vector<bool>(MAX_BIN,0);
	FOR(i,0,MAX_BIN-1)
		res[i] = (A[i] + B[i]) % 2;
	return res;
}




int A[16];


int main()
{
	//write( sum(4, 5) );
	//cout << toInt( toBin(10) ) << endl;
	
	int T;
	scanf("%d", &T);
	
	FOR(t,1,T)
	{
		int N;
		scanf("%d", &N);
		FOR(i,0,N-1)
			scanf("%d", A+i);
		
		int best = -1;
		
		//rozdleime na dve polky
		FOR(c,1,(int) pow(2.0,N)-2)
		{
			//cout << i << endl;
			
			int sum_orig[2] = {0,0};
			int sum_bin[2]  = {0,0};
			
			FOR(i,0,N-1)
			{
				int index = (c & (1 << i)) == (1 << i);
				//cout << "pre " << c << " je " << i << " - " << index << endl;
				sum_orig[index] += A[i];
				sum_bin[index] =  toInt( sum(sum_bin[index], A[i]) );
			}
			
			if (sum_bin[0] == sum_bin[1])
			{
				best = max( best, max( sum_orig[0], sum_orig[1]) );
			}
		}
		
		if (best == -1)
			printf("Case #%d: NO\n", t);
		else
			printf("Case #%d: %d\n", t, best);
	}
	
	return 0;
}
