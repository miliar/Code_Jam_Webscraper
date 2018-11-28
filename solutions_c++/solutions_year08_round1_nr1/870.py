#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <vector>
#include <queue>


using namespace std;

fstream fin("A-small-attempt1.in.txt",ios::in);
fstream fout("A-small-attempt1.out.txt",ios::out);

//#define fout cout

int main() {
	int t, n, i, j, k;
	int x[1001], y[1001];
	__int64 res;
	fin>>t;
	for (k=1; k<=t; k++) {
		fout<<"Case #"<<k<<": ";
		res = 0;
		fin>>n;
		for (i=0; i<n; i++) 
			fin>>x[i];
		for (i=0; i<n; i++)
			fin>>y[i];
		sort(x,x+n);
		sort(y,y+n);
		for (i=0; i<n; i++)
			res += x[i]*y[n-1-i];
		int r[100], cnt;
		bool flag = (res>=0)?true:false;
		if ( !flag )
			res = -res;
		cnt = 0;
		while (res) {
			r[cnt] = res % 10;
			res /= 10;
			cnt++;
		}
		if (!flag)
			fout<<'-';
		for (i=cnt-1; i>=0; i--)
			fout<<r[i];
		if ( cnt == 0 )
			fout<<0;
		fout<<endl;
	}
	return 0;
}