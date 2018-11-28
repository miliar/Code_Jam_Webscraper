/*
*  Javier Segovia
*  0.016
*/
#include<iostream>
#include<string>
#include<vector>
#include<math.h>
using namespace std;
#define SL size()
#define LE length()
#define PB push_back
#define MP make_pair
#define MAX(a,b) ((a)>(b)?(a):(b))
int main(){
	int kases; cin>>kases;
	for (int k=1;k<=kases; k++) {
		int n; cin>>n;
		int pb=1,tb=0,po=1,to=0,new_pos,moves;
		char c;
		for (int i=0; i<n ; i++) {
			cin>>c>>new_pos;
			if(c == 'O'){
				moves = abs(new_pos-po);
				if(tb>to+moves){ to = tb+1;}
				else{ to = to+moves+1;}
				po = new_pos;
			}
			else {
				moves = abs(new_pos-pb);
				if(to>tb+moves){tb = to+1;}
				else{ tb = tb+moves+1;}
				pb = new_pos;
			}
		}
		cout << "Case #"<<k<<": "<<MAX(to,tb)<<endl;
	}
}