#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <fstream>

using namespace std;

#define ll long long

int main () {
	fstream cin("C-small-attempt0.in");
	ofstream cout("output.txt");
	int T;
	cin>>T;
	for (int run=1;run<=T;++run) {
		int N,L,H;
		cin>>N>>L>>H;
		int a[N+1];
		for (int i=0;i<N;++i) {
			cin>>a[i];	
		}
		int x;
		for (x=L;x<=H;++x) {
			bool found = true;
			for (int i=0;i<N;++i) 
				if (x%a[i]==0||a[i]%x==0) continue;
				else {
					found = false;
					break;	
				}
			if (found) break;
		}
		if (x>H) cout<<"Case #"<<run<<": NO"<<endl;
		else cout<<"Case #"<<run<<": "<<x<<endl;
	}
	cin>>T;
	return 0;
}
