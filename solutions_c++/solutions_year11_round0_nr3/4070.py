#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstring>
#include <algorithm>

#define INF (int)1e9
#define ll long long

using namespace std;

int t, n, a[1011];
int c, counter;
bool flag;

void rec(int x, int set1, int set2, int xx, int yy, int val1, int val2){
//	cout<<x<<" "<<set1<<" "<<set2<<endl;
	if (x==n) {
//		cout<<set1<<" "<<set2<<endl;
		if (set1==set2 && xx!=0 && yy!=0) {c = max(max(val1, val2),c);}
		return;
	}

	rec(x+1, set1^a[x],set2, xx+1, yy, val1+a[x], val2);
	rec(x+1, set1,set2^a[x], xx, yy+1, val1, val2+a[x]);

	return;
}

int main(){
	ios_base::sync_with_stdio();

	ifstream in("in");
	ofstream out("out");

	in>>t;
	counter = 0;
	while (t>0){
		counter++;
		in>>n;
		for (int i=0;i<n;i++) in>>a[i];
		c = -1;
		rec(0,0,0,0,0,0,0);
		if (c!=-1)
			out<<"Case #"<<counter<<": "<<c<<endl;
		else 
			out<<"Case #"<<counter<<": NO"<<endl;
		t--;
	}

	
	return 0;
}
	
