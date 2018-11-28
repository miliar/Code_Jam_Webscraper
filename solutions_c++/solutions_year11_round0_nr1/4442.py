#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstring>
#include <algorithm>

#define INF (int)1e9
#define ll long long

using namespace std;

int orange[101], blue[101], xx, yy,x,y;
int t, n, m, tt, counter, mm;
char c[101];
int push;

int main(){
	ios_base::sync_with_stdio();

	ifstream in("in");
	ofstream out("out");

	in>>t;
	counter = 0;
	while (t>0){
		counter++;n = 0;m = 0;
		in>>mm;
		for (int i=0;i<mm;i++){
			in>>c[i];
			if (c[i]=='O') in>>orange[n++]; else in>>blue[m++];
		}
		x = 1;y = 1;xx = 0;yy = 0;
		tt = 0;
		while (xx<n || yy<m){
			push = 0;
			tt ++;
			if (xx<n){
				if (c[xx+yy]=='O' && x == orange[xx]) {xx++; push=1;}
				if (x != orange[xx] && push!=1)
				if (x < orange[xx]) x++; else x--;
			}
			if (yy<m){
				if (c[xx+yy]=='B' && y == blue[yy] && push!=1) {yy++;  push=2;}
				if (y != blue[yy] && push!=2)
				if (y < blue[yy]) y++; else y--;
			}
		}
		out<<"Case #"<<counter<<": "<<tt<<endl;
		t--;
	}

	
	return 0;
}
	
