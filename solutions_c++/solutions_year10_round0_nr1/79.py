/*
 *  A.cpp
 *  
 *
 *  Created by Nathan David Claus on 4/1/10.
 *  Copyright 2010 __MyCompanyName__. All rights reserved.
 *
 */


// cheburashka, bear-mouse, team template

#include <cstdlib>
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <map>
#include <algorithm>
#include <cstdio>
#include <sstream>
#include <stack>
#include <cmath>
#include <queue>
#include <cstring>
#include <set>
using namespace std;

typedef long long ll;
typedef vector < string > vs;
typedef vector <int> vi;
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define deb(x) cout << #x << ": " << x << endl;
#define debv(x) for(int i = 0; i < (x).size(); i++) cout << x[i] << ' '; cout << endl;

#define pb(x) push_back(x)

#define mp(x, y) make_pair(x, y)

#define PII pair<long long,long long>

const int MAXD = 16;
		
int main()
{
	int T;
	scanf("%d\n",&T);
	for(int tcase = 1; tcase <= T; tcase++)
	{
		int N,K;
		scanf("%d %d\n",&N,&K);
		int ok = 1;
		int mask = ((1<<N)-1);
		K = (K&mask);
		printf("Case #%d: ",tcase);
		if(K != mask) printf("OFF\n");
		else printf("ON\n");
		
						
	}
	
	return 0;
}