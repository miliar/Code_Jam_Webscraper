#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>

#include <set>
#include <map>

#include <queue>
#include <deque>
#include <stack>
#include <list>

#include <cstdio>
#include <cmath>
#include <cstdlib>

using namespace std;
vector <int> y;
vector <int> z;

int por(int a, int b){
	int aux = 1;
	int k = 0;
	while(k < b){
		aux = aux *a;
		k++;
	}
	return aux;
}

int tobase(vector <int> x, int bas){
	int t = x.size() - 1;
	int c = 0;
	for(int i = 0; i < x.size(); i++){
		c += x[i]*por(bas, t);
		t--;
	}
	return c;
}

int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.txt", "w", stdout);
	
	int T;
	cin>>T;
	
	for(int i = 0; i < T; i++){
		string N;
		cin>>N;
		
		int k = 0;
		int m = 0;
		string xa = "";
		cout<<"Case #"<<i+1<<": ";
		for(int j = 0; j < N.size(); j++){
			if(j == 0){
				xa = xa + N[j];
				y.push_back(1);
				z.push_back(1);
			}else{
				int b = xa.find(N[j]);
				if( b == -1){
					if(k == 0){
						xa = xa + N[j];
						y.push_back(0);
						z.push_back(0);
						k = 2;
					}else{
						xa = xa + N[j];
						y.push_back(k);
						z.push_back(k);
						k++;
					}
				}else{
					z.push_back(y[b]);
				}
			}
		}
		if(k == 0) k = 2;
		int tot = tobase(z, k);
		cout<<tot<<endl;
		y.clear();
		z.clear();
	}
	return 0;
}
