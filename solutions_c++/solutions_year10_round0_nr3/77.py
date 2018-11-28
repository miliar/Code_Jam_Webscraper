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


int main()
{
	int T;
	scanf("%d",&T);
	for(int tcase = 1; tcase <= T; tcase++)
	{
		long long NR, P, NG;
		scanf("%lld %lld %lld",&NR,&P,&NG);
		long long gsz[NG];
		for(int i = 0; i < NG; i++) scanf("%lld",&gsz[i]);
		
		long long hit[NG];
		long long pr[NG];
		memset(hit,-1,sizeof(hit));
		memset(pr,-1,sizeof(pr));
		long long CASHMONEY = 0;
		long long CG = 0;
		for(int cride = 1; cride <= NR; cride++)
		{
			if(hit[CG] != -1)
			{
				if(cride-hit[CG] <= NR-cride+1)
				{
					long long nper = (NR-cride+1) / (cride-hit[CG]);
					long long plus = nper*(CASHMONEY-pr[CG]);
					CASHMONEY += plus;
					cride += nper*(cride-hit[CG])-1;
					continue;
				}
			}
			if(hit[CG] == -1)
			{
				hit[CG] = cride;
				pr[CG] = CASHMONEY;
			}
			
			
			
			long long peeps = gsz[CG];
			long long nextg = (CG+1)%NG;
			while(true)
			{
				if(nextg == CG || peeps+gsz[nextg] > P)
				{
					break;
				}
				else 
				{
					peeps += gsz[nextg];
					nextg = (nextg+1)%NG;
				}
			}
			CASHMONEY += peeps;
			CG = nextg;
		}
		printf("Case #%d: %lld\n",tcase,CASHMONEY);
		
	}
	
	return 0;
}