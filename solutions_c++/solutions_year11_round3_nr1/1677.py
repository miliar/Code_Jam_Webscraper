#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstring>
#include <algorithm>

#define INF (int)1e9
#define ll long long

using namespace std;

string a[60];
int n,t,m,counter;
bool impossible;

int main(){
	ios_base::sync_with_stdio();

	ifstream in("in");
	ofstream out("out");

	in>>t;
	counter = 0;
	while (t>0){
		counter++;
		in>>n>>m;getline(in,a[0]);
		for (int i=0;i<n;i++)
			getline(in,a[i]);
		impossible = false;
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++)
				if (a[i][j]=='#'){
					if (i==n-1 || j==m-1 || a[i][j+1]!='#' || a[i+1][j]!='#' || a[i+1][j+1]!='#') {impossible = true; goto ka;}
					a[i][j] = '/';
					a[i][j+1] = '\\';
					a[i+1][j] = '\\';
					a[i+1][j+1] = '/';
				}

		ka:;
		if (impossible) out<<"Case #"<<counter<<":"<<endl<<"Impossible\n"; else {
			out<<"Case #"<<counter<<":"<<endl;
			for (int i=0;i<n;i++) out<<a[i]<<endl;
		}
		t--;
	}

	
	return 0;
}
	
