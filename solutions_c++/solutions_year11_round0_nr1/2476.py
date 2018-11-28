#include <iostream>
#include <deque>
using namespace std;
void result(int t, int r) {
    cout<<"Case #"<<(t+1)<<": "<<r<<endl; 
}
int sign(int a) {
    if(a == 0) return 0;
    if(a < 0) return -1;
    return 1;
}
int main() {
	int T;
	cin>>T;
	for(int t = 0; t < T; ++t) {
		int N;
        cin>>N;
        deque<int> turns;
        deque<int> h1;
        deque<int> h2;

        for(int n = 0; n < N; ++n) {
        	char l;
        	int p;
        	cin>>l>>p;
        	if(l == 'O') {
                h1.push_back(p);
                turns.push_back(0);
            } else {
                h2.push_back(p);
                turns.push_back(1);
            }
        }
        int l1 = 1, l2 = 1;
        int dn = N;
        int r = 0;
        while(dn != 0) {
            while(true) {
                ++r;
            	bool p1 = false, p2 = false;
                if(!h1.empty() && !turns[0] && l1 == h1[0]) {
                    p1 = true;
                    h1.pop_front();
                    turns.pop_front();
                    --dn;
                } else if(!h2.empty() && turns[0] && l2 == h2[0]) {
                    p2 = true;
                    h2.pop_front();
                    turns.pop_front();
                    --dn;
                }
                if(h1.empty()) p1 = true;
                if(h2.empty()) p2 = true;

                if(!p1) l1 += sign(h1[0] - l1);
                if(!p2) l2 += sign(h2[0] - l2);
            	if(turns.empty()) break;
            }
        }
        result(t,r);
    }
    return 0;
}
