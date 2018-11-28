#include <stdio.h>
#include <string.h>
#include <math.h>
#include <iostream>
using namespace std;

void input();
int solve();
int n;
struct Pos	{
    int kind;
    int pos;
    Pos()	{}
    Pos(int _k,int _p):kind(_k),pos(_p)	{}
};

struct Status	{
    int time , pos;
};

Status so , sb;
Pos p[111];
int main()	{

    freopen("C:\\Users\\MadFroG\\Downloads\\A-large.in" , "r" , stdin);
    freopen("C:\\Users\\MadFroG\\Downloads\\A-large.out" , "w" , stdout);
    int T;
    scanf("%d" , &T);
    
    for ( int cas = 1;cas <= T;cas ++ )	{
	input();
	printf("Case #%d: %d\n" , cas , solve());
    }
    return 0;
}

void input()	{
    scanf("%d" , &n);
    char s[2];
    int pos;
    for ( int i = 0;i < n;i ++ )	{
	scanf("%s%d" , s , &pos);
	if ( s[0]=='O' )	{
	    p[i] = Pos( 0 , pos);
	}	else	{
	    p[i] = Pos( 1 , pos);
	}
    }
}

int solve()	{
    so.time = 0;
    so.pos = 1;
    sb.time = 0;
    sb.pos = 1;

    for ( int i = 0;i < n;i ++ )	{
	if ( p[i].kind == 0 )	{
	    so.time += abs(so.pos-p[i].pos)+1;
	    if ( so.time <= sb.time ) so.time = sb.time+1;
	    so.pos = p[i].pos;
	}	else	{
	    sb.time += abs(sb.pos-p[i].pos)+1;
	    if ( sb.time <= so.time ) sb.time = so.time+1;
	    sb.pos = p[i].pos;
	}
    }
    return max(so.time , sb.time);
}
