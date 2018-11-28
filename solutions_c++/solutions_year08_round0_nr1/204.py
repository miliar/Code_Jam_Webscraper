#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <sstream>

using namespace std;

int main (void) {
    ofstream OUT;
    OUT.open ("OU.txt");
    ifstream FILE("IN2.txt");
    int Num;
    FILE>>Num;
	for (int z=1; z<=Num; z++) {
		cout<<"e\n";
		int S, Q;
		FILE>>S;
		vector <string> s(S);
		for (int i=0; i<S; i++) FILE>>s[i];
		FILE>>Q;
		if (Q==0) OUT<<"Case #"<<z<<": "<<0<<"\n";
		else {
		vector <string> q(Q);
		for (int i=0; i<Q; i++) FILE>>q[i];
		vector <vector <int> > a(Q+1, vector <int> (S, 2000000));
		
		vector <int> m(Q+1);
		for (int i=0; i<S; i++) a[0][i]=0;
		
		for (int i=0; i<Q; i++) {
			int y;
			bool f=true;
			for (y=0; y<S&&f; y++) if (s[y]==q[i]) f=false;
			cout<<--y<<"   ";
			a[i][y]=2000000;
			m[i]=4000000;
			for (int j=0; j<S; j++) {
				if (m[i]>a[i][j]) m[i]=a[i][j];
				}
			cout<<m[i]<<"\n";
			for (int j=0; j<S; j++) {
				a[i+1][j]=min(a[i][j], m[i]+1);
				}
			for (int j=0; j<S; j++) cout<<a[i][j]<<" ";
			cout<<"\n";
			}
			for (int j=0; j<S; j++) cout<<a[Q][j]<<" ";
			cout<<"\n";

		int M=4000000;
		for (int i=0; i<S; i++) if (M>a[Q-1][i]) M=a[Q-1][i];
		OUT<<"Case #"<<z<<": "<<M<<"\n";
			}
		}

	cout<<"fasd";
    FILE.close();
    OUT.close();
    system("PAUSE");
    return 0;
    }
