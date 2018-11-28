#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <stack>
#include <set>
#define sz size()
#define MP make_pair
#define eps (1e-9)
using namespace std;
typedef unsigned long long int64;
int main() {	   
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int L, D, N;
	scanf("%d", &L); scanf("%d", &D); scanf("%d", &N);
	vector <string> s;
	string a;
	for (int i=1; i<=D; i++){
		cin >> a;
		s.push_back(a);
	};
	vector <vector <char>> p(L);
	int y;
	for (int i=1; i<=N; i++){
		cin >> a;
		for (int j=0; j<L; j++){p[j].clear();}
		y=0;
		for (int j=0; j<L; j++){
			if (a[y]!='('){
				p[j].push_back(a[y]);
			} else {
				y++;
				while (a[y]!=')'){
					p[j].push_back(a[y]);
					y++;
				};
			};
			++y;
		};
		bool w, z;
		int co=0;

		for (int j=0; j<s.size(); j++){
		w=true;
			for (int k=0; k<L; k++){
				z=false;
				for (int r=0; r<p[k].size(); r++){
					if (s[j][k]==p[k][r]) z=true;
				};
				if (!z) w=false;
			};
		if (w) co++;
		};
		printf("Case #%d: %d\n", i, co);
	};
	
	return 0;
}