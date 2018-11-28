// g1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <list>
#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <map>
#include <algorithm>
using namespace std;

#define rep(i,n) for(int i=0; i<n; i++)
#define forr(i,a,b) for (int i=a; i<=b; i++)
#define ford(i,a,b) for (int i=a; i>=b; i--)
#define mset(a,b) memset(a,b,sizeof(a))
#define sz(a) int( a.size() )
#define all(A) A.begin(),A.end()
#define sqr(q) q*q
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)
#define X first
#define Y second

typedef long long i64;
typedef vector<int> VI;
typedef vector< VI > VVI;
typedef pair<int,int> PII;
typedef vector<string> VS;

string s[4][2] = { 
	"ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","there are twenty six factorial possibilities",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv","so it is okay if you want to just give up",
	"qz","zq"
};
int code[30];

void preprocess(){
	rep(i,30) code[i]=-1;

	rep(i,4){
		string s1 = s[i][0];
		string s2 = s[i][1];
		rep(j, sz(s1))
			if (isalpha(s1[j]))
		{
			int ind = s1[j]-'a';
			int cod = s2[j]-'a';

			if (-1 == code[ind]) code[ind]=cod;
			if (code[ind] != cod) printf("SHIIT\n");
		}
	}
}

int main()
{
	preprocess();	
	freopen("g1.in","r",stdin);
	freopen("g1.out","w",stdout);	
	int n;
	char temp[1000];
	scanf("%d\n",&n);
	rep(testNum,n){
		gets(temp);
		string st = string(temp);
		printf("Case #%d: ",testNum+1);
		rep(i,sz(st)){
			if (isalpha( st[i] )){
				int ch = code[ st[i]-'a' ]+'a';
				printf("%c",(char)ch);
			} else printf("%c",st[i]);
		}
		printf("\n");
	}
	return 0;
}

