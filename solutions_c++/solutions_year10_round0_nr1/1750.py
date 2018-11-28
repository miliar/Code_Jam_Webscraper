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
#include <windows.h>
using namespace std;
#pragma comment(linker, "/STACK:20000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "A-large";

void init(){
  freopen((problem_name+".in").c_str(),"rt",stdin);
  freopen((problem_name+".out").c_str(),"wt",stdout);
}



int main()
{
	init();


	int t;
	scanf("%d",&t);

	int tst=0;
	while (t--)
	{
		tst++;
		int n,k;
		scanf("%d%d",&n,&k);
		if (((k+1)%(1<<n))==0)
			printf("Case #%d: ON\n",tst); else
			printf("Case #%d: OFF\n",tst); 	
	}
	


  return 0;
}
