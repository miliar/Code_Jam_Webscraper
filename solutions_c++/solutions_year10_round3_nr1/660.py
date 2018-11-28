#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <algorithm>

using namespace std;

struct point
{
	int a,b;
};

const int nmax = 2000;

point p[nmax];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int nn;
	cin >> nn;
	for (int test = 1;test <= nn; ++test){

		int n;
		cin >>n;
		for (int i = 0;i < n; ++i) cin >> p[i].a >> p[i].b;

		int sum = 0;
		for (int i = 0;i < n; ++i) 
			for (int j = i+1;j < n; ++j) 
				if ((p[i].a-p[j].a) * (p[i].b - p[j].b) < 0) ++sum;
		
		
		printf("Case #%i: %i\n",test,sum);		
	}
	
	return 0;
}