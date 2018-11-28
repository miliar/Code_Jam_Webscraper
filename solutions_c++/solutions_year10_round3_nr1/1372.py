#include <iostream>
#include <set>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <map>
using namespace std;

// POR EL HONOR!!! ERASMUS 2 THE POWER!

int main ()
{
	set<int> ss;
	set<int>::iterator it;
	set<int>::iterator it2;
	map<int,int> vv;
	pair<map<int,int>::iterator,bool> ret;


	int i,j;
	int T;
	int N;
	int x,y;
	int cx = 0;

	cin >> T;

	for (i = 1; i <= T; i++){
		cin >> N;

		for (j = 1; j <= N; j++){
			scanf("%d %d",&x,&y);
			ss.insert(x); 
			vv.insert(pair<int,int>(x,y)); 
		}

		for (it=ss.begin(); it!=ss.end(); it++){
			it2 = it;
			
			for (it2++; it2!=ss.end(); it2++){
				if (vv[*it] > vv[*it2])
					cx++;	
				
			}
		}
		
		cout << "Case #" << i << ": " << cx << endl;

		cx = 0;
		vv.clear();
		ss.clear();
	}
  return 0;
}
