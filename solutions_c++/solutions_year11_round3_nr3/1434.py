#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <numeric>

#define fi(n) for(int i=0;i< n;i++)
#define fj(n) for(int j=0;j< n;j++)
#define fk(n) for(int k=0;k< n;k++)

using namespace std;

int main(){
	int players[10000];
	int cases;
	cin >> cases;
	fi(cases){
		int N, L, H;
		cin >> N >> L >> H;
		fj(N){
			cin >> players[j];
		}
		int acc = players[0];
	
		int j;
		bool fail;
		for(j=L;j<=H;j++){
			fail=false;
			fk(N){
				if (players[k]%j != 0 && j%players[k] != 0)
				{
					fail=true;
					break;
				}
			}
			if (fail==false)
				break;
		}	 	 	 
		cout << "Case #" << i+1 <<": ";	
		if (fail == true)
			cout << "NO" << endl;
		else
			cout << j << endl; 
	}
}

