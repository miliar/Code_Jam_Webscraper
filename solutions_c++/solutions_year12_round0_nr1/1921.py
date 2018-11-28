#include <stdio.h>
#include <sstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <list>
#include <iomanip>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <cassert>
#include <string.h>
using namespace std;
#pragma comment(linker, "/STACK:50000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "A-small-attempt0";

void init(){
	freopen((problem_name+".in").c_str(),"rt",stdin);
	freopen((problem_name+".out").c_str(),"wt",stdout);
}

int m[256];
int u[256];

int f(string s, string s2)
{
	for (int i=0;i<sz(s);i++) {
		m[s[i]]=s2[i];
		u[s2[i]]=1;
	}
	return 0;
}


int main() {

	//init();

	f("ejp mysljylc kd kxveddknmc re jsicpdrysi","our language is impossible to understand");
	f("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","there are twenty six factorial possibilities");
	f("de kr kd eoya kw aej tysr re ujdr lkgc jv","so it is okay if you want to just give up");
	m['y']='a';
	m['e']='o';
	m['q']='z';
	m['z']='q';
	for (int i='a';i<='z';i++) {
		//if (!m[i]) cout << (char)i << endl;
	//	if (!u[i]) cout << (char)i << endl;
	}

	int tst;
	scanf("%d\n",&tst);

	for (int cas=1;cas<=tst;cas++)
	{
		char s[111];
		gets(s);
		int len = strlen(s);
		for (int i=0;i<len;i++)
			s[i]=m[s[i]];

		printf("Case #%d: %s\n",cas,s);	
	}


	

	

	return 0;
}