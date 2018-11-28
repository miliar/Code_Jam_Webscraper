#include "stdafx.h"
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>

#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <functional>
#include <map>
#include <set>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define zero(a) memset(a, 0, sizeof(a))
#define pb push_back
#define mp make_pair

int c;
int vv[1000];
int* mem1;
int* mem2;
int calc_taken(int i, int tot);
int calc_notake(int i, int tot){
	if(mem1[i*1048576 + tot]!=0) return mem1[i*1048576 + tot]-2;
	if(i==c-1){
		if(tot==0) return 0;
		return -1;
	}
	int maxwith = calc_notake(i+1, tot ^ vv[i]);
	if(maxwith!=-1) maxwith += vv[i];
	int maxwithout = calc_taken(i+1, tot);
	int best = max(maxwith, maxwithout);
	mem1[i*1048576 + tot] = best+2;
	return best;
}

int calc_taken(int i, int tot){
	if(mem2[i*1048576 + tot]!=0) return mem2[i*1048576 + tot]-2;
	if(i==c-1){
		if(tot==vv[i]) return vv[i];
		if(tot==0) return 0;
		return -1;
	}
	int maxwith = calc_taken(i+1, tot ^ vv[i]) + vv[i];
	int maxwithout = calc_taken(i+1, tot);
	int best = max(maxwith, maxwithout);
	mem2[i*1048576 + tot] = best+2;
	return best;
}

int main()
{
  int tn;
  scanf("%d", &tn);
  for (int tt = 1; tt <= tn; tt++)
  {
    fprintf(stderr, "%d\n", tt);
    printf("Case #%d: ", tt);

	scanf("%d", &c);
	int min=9999999;
	int tot=0;
	int xortot = 0;
    for(int i=0;i<c; i++){
      scanf("%d ", &vv[i]);
	  if(vv[i]<min)min = vv[i];
	  xortot ^= vv[i];
	  tot += vv[i];
	}
/*	mem1 = new int[c*1048575];
	memset(mem1, 0, sizeof(int)*c*1048575);
	mem2 = new int[c*1048575];
	memset(mem2, 0, sizeof(int)*c*1048575);
	
	int best = calc_notake(0, 0);	

	if(best==-1)
		printf("NO\n");
	else
		printf("%d\n",best);
	delete[] mem1;
	delete[] mem2;
*/
	if(xortot!=0)
		printf("NO\n");
	else
		printf("%d\n",tot-min);
	
  }
  return 0;
}

