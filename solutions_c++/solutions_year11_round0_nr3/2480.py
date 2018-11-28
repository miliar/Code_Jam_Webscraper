#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<string>
#include<vector>
#include<sstream>
#include<algorithm>
#include<map>
#include<queue>
using namespace std;
void print ( int kase ,  long long yes )
{
	cout <<"Case #"<<kase<<": ";
	if (yes == -1) cout <<"NO";
	else cout << yes;
	cout <<"\n";
 	return ;
}
int main ()
{
 	freopen ("C-large.in","r",stdin);
 	freopen("C-large_1.out","w",stdout);
 	int T ,kase = 0; 
 	for ( scanf("%d",&T) ; T ;T-- ) {
		long long  N, c; cin >> N;
		vector <long long> candies;
		for (int i = 0; i < N; i++) cin >> c, candies.push_back(c);
		c = 0;
		for (int i = 0; i < N; i++)  c ^= candies [i];
		if (c !=0) print(++kase, -1);
		else {
			sort(candies.begin(), candies.end());
			long long sum = 0;
			for (int i = 1; i < N; i++) sum += candies [i];
			print (++kase, sum);
		}
	}
	return 0;
}
