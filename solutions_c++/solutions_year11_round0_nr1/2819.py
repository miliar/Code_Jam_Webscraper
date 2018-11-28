#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <math.h>
#include <stdio.h>
using namespace std;

int main(){
	//freopen("sample.in","r",stdin);
	//freopen("sample.out","w",stdout);
	//freopen("A-small-attempt0.in","r",stdin);
	//freopen("A-small-attempt0.out","w",stdout);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	cin>>T;
	for (int i=0;i<T;i++){
		int N;
		cin>>N;
		int posO=1;int posB=1;
		int secs=0;
		int timeOtherside=0;
		char c = ' ';
		for (int j=0;j<N;j++){
			char Rbt; int Btn;
			int step=0;
			cin>>Rbt>>Btn;
			if ('O'==Rbt) {
				step =abs(Btn-posO);
			} else {
				step =abs(Btn-posB);
			}
			if (Rbt!=c){
				if (step>timeOtherside){
					int timeElps = step-timeOtherside+1;
					secs+=timeElps;
					timeOtherside=timeElps;
				} else {
					secs++;
					timeOtherside=1;
				}
				c=Rbt;
			} else {
				secs+=step+1;
				timeOtherside+=step+1;
			}
			
			if ('O'==c){
				posO=Btn;
			} else {
			    posB=Btn;
			}
		}
		cout<<"Case #"<<i+1<<": "<<secs<<endl;
		
	}
	
	
}