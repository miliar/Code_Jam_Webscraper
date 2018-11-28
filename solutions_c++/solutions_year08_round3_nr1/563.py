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

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define F(i,a,b) for(int i=(a);i<(b);++i)

using namespace std;

vector <int> v;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.txt", "w", stdout);
	
	int n;
	cin>>n;
	
	for(int i=0; i<n; i++){
        int p, k, l;
		cin>>p>>k>>l;
		
		vector <int> x(l);
		v = x;
		for(int j=0; j<l; j++)
			cin>>v[j];

		sort(rall(v));
		
		int m=1;
		int aux=1;
		long long cant = 0;
		for(int j=0; j<l; j++){
			cant = cant + v[j]*m;
			aux++;
			if(aux>k)
			{
				aux = 1;
				m++;
			}
		}
		
		v.clear();
		cout<<"Case #"<<i+1<<": "<<cant<<endl;
    }
    
	return 0;
}
