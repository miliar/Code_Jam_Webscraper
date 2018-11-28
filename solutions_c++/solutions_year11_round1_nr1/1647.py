#include <iostream>
#include <fstream>
#include <math.h>
#define For(I,A,B) for(int I = A; I < B; ++I)
using namespace std;

int main(){
	ifstream cin ("A-small-attempt0.in");
	ofstream cout ("output.txt");
	int T,t=0;
	cin >> T;
	while(t < T) {
		++t;
		int N,pd,pg;
		cin >> N >> pd >> pg;
		bool isPos = false;
		cout << "Case #" << t << ": ";
		if (pg == 0 || pg == 100)
			isPos = ( pg == pd);
		else
		For(i,1,N+1){
			int wd = pd * i;
			if (wd % 100) continue;
			else{
				isPos = true;
				break;
			}
		}
		if (isPos)
			cout <<  "Possible"<<endl;
		else
			cout << "Broken"<<endl;
	}
}