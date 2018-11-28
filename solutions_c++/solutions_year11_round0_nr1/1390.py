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

string problem_name = "A-large(1)";

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
		int posO=1,posB=1,tmO=0,tmB=0;
		int n;
		cin >> n;
		int curtime=0;
		for (int i=0;i<n;i++)
		{
			char c;
			int b;
			cin >> c >> b;
			int add;
			if (c=='O')
			{
				add = max(0,abs(b-posO)-(curtime-tmO)) +1 ; 
				res+= add;
				curtime+=add;
				tmO=curtime;
				posO=b;
			} else
			{
				add = max(0,abs(b-posB)-(curtime-tmB)) +1 ; 
				res+= add;
				curtime+=add;
				tmB=curtime;
				posB=b;
			} 
		}
	
		printf("Case #%d: %d\n",cas,res);
	}




	

	return 0;
}

