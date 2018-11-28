#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

#define NMAX 110

int n, s, p;
int pt[NMAX];

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int tc;
	cin >> tc;
	for (int tci=0; tci<tc; tci++){
		cin >> n >> s >> p;
		for (int i=0; i<n; i++)
			cin >> pt[i];
		int res = 0;
		for (int i=0; i<n; i++){
			int sp = p*3;
			if (sp - pt[i] <= 2)
				res++;
			else if (sp - pt[i] <= 4 && s>0 && pt[i] > 0){
				res++;
				s--;
			}
		}
		printf("Case #%d: %d\n", tci+1, res);
	}

}