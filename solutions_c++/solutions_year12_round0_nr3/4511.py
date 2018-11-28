// Solution for Google Code Jam 2012 Qualification Round C
// Tristram Healy, trissylegs@gmail.com
// 14 Apr 2012

//#define DEBUG

#include <cstdio>
#include <cstdlib>
#include <cassert>

#include <vector>

using namespace std;

#define MAX_LEN 11

int test(int n, int A, int B);
int ilog10(int x);
int contains(vector <int>, int n);

int main(void)
{
    int T,A,B,i,n;
    int result;

    scanf("%d", &T);
    for(i = 1; i <= T; i++)
    {
	result = 0;
	scanf("%d %d", &A, &B);
	for(n = A; n < B; n++)
	{
#ifdef DEBUG
	    printf("%d (%d):\n", n, ilog10(n));
#endif
	    result += test(n, A, B);
#ifdef DEBUG	    
	    printf("\n");
#endif
	}
	printf("Case #%d: %d\n", i, result);
    } 

    return 0;
}

int test(int n, int A, int B)
{
    int i;
    int temp;
    vector <int> m;
    int out = 0;
    int length = ilog10(n);
    char sn[MAX_LEN * 2];


    for(i = 0; i < 2*MAX_LEN; i++)
    {
	sn[i] = '\0';
    }

    sprintf(sn, "%d", n);

    for(i = 0; i < length; i++)
    {
	sn[length + i] = sn[i];
	temp = atoi(sn+i+1);
	if( !contains(m, temp) )
	{
	    m.push_back(temp);
#ifdef DEBUG
	    printf("<%s: %d> ", sn+i+1, m.back());
#endif
	    if(m.back() > n && m.back() <= B)
	    {
#ifdef DEBUG
		printf("* ");
#endif
		out += 1;
	    }
	}
    }
   
    return out;
}

// Returns the floored base 10 logerithm of x
int ilog10(int x)
{
    int out;
    if(x <= 1)
    {
	out = 0;
    } else {
	for(out = 0; x / 10 > 0; out++)
	    x /= 10;
    }
    return out+1;
}

int contains(vector<int> m, int n)
{
    vector<int>::iterator it;
    for(it = m.begin(); it < m.end(); it++)
    {
	if(*it == n)
	{
	    return 1;
	}
    }
    return 0;	
}
