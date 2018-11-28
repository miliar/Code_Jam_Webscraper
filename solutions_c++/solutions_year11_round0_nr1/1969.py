#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>

#define MP make_pair
#define ST first
#define ND second
#define PB push_back
#define LL long long
#define VII vector<int>
#define PII pair<int, int>

#define MAXN 105

using namespace std;

int t, n;

int dist[MAXN];
bool first[MAXN];
int next1[MAXN], next2[MAXN];
int n1, n2;

int main(){
    scanf("%d", &t);
    for(int testcase = 0; testcase < t; testcase++){
	scanf("%d", &n);
	char cin[2];
	n1 = n2 = 0;

	for(int i = 0; i < n; i++){
	    scanf("%s %d", cin, &dist[i]);
	    if(cin[0] == 'O'){
		first[i] = true;
		next1[n1] = dist[i];
		n1++;
	    }
	    else{
		first[i] = false;
		next2[n2] = dist[i];
		n2++;
	    }
	}
	int res = 0;
	int p1 = 0, p2 = 0;
	int d1 = 1, d2 = 1;
	int pos = 0;
	bool pressed = false;
	
	while(pos < n){
	    res++;
	    if(p1 < n1){
		if(d1 != next1[p1]){
		    if(d1 > next1[p1]) d1--;
		    else d1++;
		}
		else{
		    if(first[pos]){
			pressed = true;
			p1++;
		    }
		}
	    }

	    if(p2 < n2){
		if(d2 != next2[p2]){
		    if(d2 > next2[p2]) d2--;
		    else d2++;
		}
		else{
		    if(!first[pos]){
			pressed = true;
			p2++;
		    }
		}
	    }

	    if(pressed){
		pressed = false;
		pos++;
	    }
	}

	printf("Case #%d: %d\n", testcase+1, res);
    }
    return 0;
}