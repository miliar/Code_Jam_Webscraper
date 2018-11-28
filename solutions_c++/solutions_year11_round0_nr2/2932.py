//============================================================================
// Name        : B.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main() {
	int t=0,T;
	cin >> T;
	while(t<T){
		t++;
		int c,C,d,D,n,N;
		char Cod[36][4], Del[28][3], Inv[100],I;
		cin >> C;
		for(c=0;c<C;c++){
			cin >> Cod[c];
		}
		cin >>D;
		for(d=0;d<D;d++){
			cin >> Del[d];
		}
		cin >>N;
		n=0;
		while(N--){
			cin >> I;
			if(n>0){
				for(c=0;c<C;c++){
					if(I==Cod[c][1] && Inv[n-1] == Cod[c][0]){
						I = Cod[c][2];
						n--;
						break;
					}
					if(I==Cod[c][0] && Inv[n-1] == Cod[c][1]){
						I = Cod[c][2];
						n--;
						break;
					}
				}
				for(d=0;d<D;d++){
					int cur=-1;
					if(I==Del[d][0]) cur=1;
					if(I==Del[d][1]) cur=0;
					if(cur>=0){
						for(int i=0;i<n;i++){
							if(Inv[i]==Del[d][cur]){
								I=0;
								n=0;
							}
						}
					}
				}
			}
			if(I!=0) Inv[n++]=I;
		}
		cout << "Case #" << t << ": [";
		for(int i=0;i<n;i++){
			if(i>0) cout << ", ";
			cout << Inv[i];
		}
		cout << "]" << endl;

	}
	return 0;
}
