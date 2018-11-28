#include <iostream>
#include <vector>
#include <utility>
#include <string>
#include <algorithm>

#define vi vector<int>
#define pb push_back

using namespace std;

int main() {
	int T; cin >> T;
	for(int iter=0;iter<T;iter++) {
		int N;
		cin >> N;
		vi a1,a2;
		vi b1,b2;
		for(int i=0;i<N;i++) {
			char ch; int b;
			cin >> ch >> b;
			if (ch == 'O') {
				a1.pb(b);a2.pb(i);		
			} else {
				b1.pb(b);b2.pb(i);
			}
		}
		int todo = 0;
		int loc1,loc2;
		loc1 = loc2 = 1;
		int m1, m2;m1 = m2 = 0;
		int t = 0;
		while(todo!=N) {
			//cout<<"time = "<<t<<" A at "<<loc1<<" and seq "<<m1<<" B at "<<loc2<<" and seq "<<m2<<"\n";
			++t;
			if(m1<a1.size() && m2<b1.size() && a1[m1]==loc1 && a2[m1]==todo && b1[m2]==loc2 && b2[m2]==todo+1) {m1++;todo++;}
			else if(m1 < a1.size() && m2 < b1.size() && a1[m1]==loc1 && a2[m1]==todo+1 && b1[m2]==loc2 && b2[m2]==todo) {m2++;todo++;}
			else { 
				if (m1<a1.size()) {
					if(a1[m1]==loc1 && a2[m1]==todo) {todo++;m1++;}
					else if(a1[m1]<loc1) loc1--;
					else if(a1[m1]>loc1) loc1++;
				}
				if (m2<b1.size()) {
					if(b1[m2]==loc2 && b2[m2]==todo) {todo++;m2++;}
					else if(b1[m2]<loc2) loc2--;
					else if(b1[m2]>loc2) loc2++;
				}
			}
			
		}
		cout<<"Case #"<<(iter+1)<<": "<<t<<"\n";
	}
}
