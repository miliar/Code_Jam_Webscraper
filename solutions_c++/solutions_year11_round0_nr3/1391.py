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
#pragma comment(linker, "/STACK:20000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "C-large(1)";

void init(){
  freopen((problem_name+".in").c_str(),"rt",stdin);
  freopen((problem_name+".out").c_str(),"wt",stdout);
}



int main()
{
	init();



	int tst;
	cin >> tst;
	for (int cas=1;cas<=tst;cas++) {
		int res=0;

		int n;
		cin >> n;
		int mn=1000100;
		int sum=0;
		for (int i=0;i<n;i++)
		{
			int a;
			cin >> a;
			mn=min(a,mn);
			res^=a;
			sum+=a;
		}
		if (res) printf("Case #%d: NO\n",cas,res); else
		printf("Case #%d: %d\n",cas,sum-mn);
	}




	

	return 0;
}

