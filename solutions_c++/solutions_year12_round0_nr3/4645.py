#include <iostream>
#include <fstream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <ctime>
#include <cctype>

using namespace std;
int main()
{
 	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t,r=0;
	cin >> t;
	while (t){
	r++;
	int a, b;
	cin >> a >> b;
	int cnt = 0;
	int n, m;
	for (int i = a; i <= b; i++){
	n = i;
	vector <int> p, q;
	while (n){
		p.push_back(n % 10);
		n /= 10;
	}	
	reverse(p.begin(), p.end());
	
		for (int j = i + 1; j <= b; j++){
		q.clear();
			m = j;	
			while (m){
				q.push_back(m % 10);
				m /= 10;
			}	
		reverse(q.begin(), q.end());	
		for (int k = 0; k < p.size(); k++){
		int y = 0;
		for (int l = 0; l < p.size(); l++) y = y * 10 + q[l];
		if (y == i) {cnt++; break;}
			int u = q[q.size() - 1];
			for (int l = q.size() - 1; l > 0; l--)
				q[l] = q[l - 1];
			q[0] = u;
		}
		}                     
	}
	cout << "Case #" << r << ": "<< cnt << endl;
	t--;
	}	
	return 0;
}