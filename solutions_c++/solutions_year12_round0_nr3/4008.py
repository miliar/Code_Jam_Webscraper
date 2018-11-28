#include <iostream>
#include <vector>
#include <stdio.h>
using namespace std;

#define DEBUGN(x) cout << #x << ": " << x << endl;

int digits(int number){
    int cont = 0;
    while (number > 0){
	number /= 10;
	++cont;
    }
    return cont;
}

int brokenInt(int number, int s, int st){
    int shift = 1, shiftt = 1;
    for (int i = 0; i < s; ++i) shift *= 10;
    for (int i = 0; i < st; ++i) shiftt *= 10;
    int recycled = (number % shift);
    number /= shift;
    recycled *= shiftt/shift;
    return recycled+number;
}

int main(){
    vector< int > mark;
    int t, a, b;
    scanf("%d", &t);
    
    for (int i = 0; i < t; ++i){
	int r = 0, s, recycled;
	scanf("%d %d", &a, &b);
	s = digits(b);

	for (int j = a; j <= b; ++j){
	    mark.clear();
	    for (int k = 1; k < s; ++k){
		bool mark_use = false;
		recycled = brokenInt(j, k, s);
		for (int m = 0; m < mark.size(); ++m){
		    if (mark[m] == recycled){
			mark_use = true;
			break;
		    }
		}
		if (recycled > j && recycled <= b && !mark_use){
		    mark.push_back(recycled);
		    ++r;
		}
	    }
	}
	printf("Case #%d: %d\n", i+1, r);
    }
    return 0;
}
