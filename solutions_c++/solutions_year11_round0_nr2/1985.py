#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>
#include <vector>
using namespace std;



void input();
void output(int);
void init();
void solve();

int N;
char s[111];

vector<string> C;
vector<string> D;
vector<char> ans;

char cb[128][128];
bool op[128][128];

int main()	{

    freopen("C:\\Users\\MadFroG\\Downloads\\B-large.in","r",stdin);
    freopen("C:\\Users\\MadFroG\\Downloads\\B-large.out","w" , stdout);
    int T;

    scanf("%d" , &T);
    for ( int cas = 1;cas <= T;cas ++ )	{
    	init();
	input();
	solve();
	output(cas);
    }
    return 0;
}


void init()	{
    memset( cb , 0 , sizeof(cb));
    memset( op , 0 , sizeof(op));
}
void input()	{
    C.clear();
    D.clear();
    int n;
    scanf("%d" , &n);
    for ( int i = 0;i < n;i ++ )	{
	scanf("%s" , s);
	C.push_back(s);
	cb[s[0]][s[1]] = s[2];
	cb[s[1]][s[0]] = s[2];
    }
    scanf("%d" , &n);
    for ( int i = 0;i < n;i ++ )	{
	scanf("%s" , s);
	D.push_back(s);
	op[s[0]][s[1]] = true;
	op[s[1]][s[0]] = true;
    }
    scanf("%d" , &N);
    scanf("%s" , s);
}

void solve()	{
    ans.clear();
    for ( int i = 0;i < N;i ++ )	{
    	ans.push_back(s[i]);
	while ( ans.size()>=2 )	{
	    int l = ans.size();
	    if ( cb[ ans[l-1] ][ ans[l-2] ]!=0 )	{
		ans.pop_back();
		ans.pop_back();
		ans.push_back(cb[ ans[l-1] ][ ans[l-2] ]);
	    }	else	{
		break;
	    }
	}
	char bk = ans.back();
	for ( int j = (int)ans.size() - 2;j >= 0;j -- )	{
	    if ( op[ ans[j] ][ bk ] )	{
		ans.clear();
		break;
	    }
	}
    }
}

void output(int cas)	{
    printf("Case #%d: [" , cas);
    if ( ans.size()>0 )	{
	printf("%c" , ans[0]);
	for ( int i = 1;i < ans.size();i ++ )	{
	    printf(", %c" , ans[i]);
	}
    }
    printf("]\n");
}
