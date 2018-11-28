#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <set>
#include <sstream>

using namespace std;

int main (void) {
	ofstream OUT;
	OUT.open ("OU.txt");
	ifstream FILE("IN.txt");
	int Num;
	FILE>>Num;
	for (int z=1; z<=Num; z++) {
		int N,M,A;
		FILE>>N>>M>>A;
		int x1=0,x2,x3,y1=0,y2,y3=10000000;
		int x,y,X,Y;
		for (X=0; X<=N; X++) for (Y=0; Y<=M; Y++) for (x=0; x<=X; x++) for (y=0; y<=Y; y++) {
			if (X*Y==A+x*y) {
				x2=x;
				y2=Y;
				x3=X;
				y3=y;
				x=100;
				y=100;
				X=70;
				Y=70;
				}
			}
		if (y3<10000) OUT<<"Case #"<<z<<": "<<x1<<" "<<y1<<" "<<x2<<" "<<y2<<" "<<x3<<" "<<y3<<"\n";
		else OUT<<"Case #"<<z<<": "<<"IMPOSSIBLE"<<"\n";
		}
	FILE.close();
	OUT.close();
	system("PAUSE");
	return 0;
	}
