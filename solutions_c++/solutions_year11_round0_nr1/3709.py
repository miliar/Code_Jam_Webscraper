#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
using namespace std;

typedef pair<char, int> PCI;
typedef vector<PCI> VPCI;

#define D 1

int mabs(int n) {
	return n<0?-n:n;
}

int main() {
    int N;
    cin >> N;
	for(int i=1; i<=N;i++) {
		int n;
		cin >> n;
		VPCI v;
		for(int j=0;j<n;j++) {
			char c;
			int in;
			scanf(" %c %d ", &c, &in);
			v.push_back(PCI(c, in));
		}
		int O = 1, B = 1, t = 0;
		int mtO = 0, mtB = 0;
		char old = 'f';
		if(v[0].first == 'O') mtB = v[0].second;
		else mtO = v[0].second;
		for(int j=0;j<n;j++) {
			char c = v[j].first;
			int pos = v[j].second;
            if(c == 'O') {
                if(old == 'O') mtO = 0;
                int dt = 1 + max(0, mabs(pos - O) - mtO);
                fprintf(stderr, "O: (%d, %d), pos: %d, mtO: %d, dt: %d, t: %d\n", O, B, pos, mtO, dt, t);
                if(old != 'O') mtB = 0;
                mtB += dt;
                mtO = dt;
                t+=dt;
                O = pos;
            } else {
                if(old == 'B') mtB = 0;
                int dt = 1 + max(0, mabs(pos - B) - mtB);
                fprintf(stderr, "B: (%d, %d), pos: %d, mtB: %d, dt: %d, t: %d\n", O, B, pos, mtB, dt, t);
                if(old != 'B') mtO = 0;
                mtO += dt;
                mtB = dt;
                t+=dt;
                B = pos;
            }
            /*
			if(c == 'O') {
                int oldpos = O;
                if(old == 'B') mtB = 0;// switch
                int dt = mabs(oldpos-pos) + 1 - max(0, mtO - mabs(O-pos));
                mtB += mabs(oldpos-pos) + 1; 
                t += dt;
                O = pos;
			} else {
                int oldpos = B;
                if(old == 'O') mtO = 0;// switch
                int dt = mabs(oldpos-pos) + 1 - max(0, mtB - mabs(B-pos));
                mtB += mabs(oldpos-pos) + 1; 
                t += dt;
                B = pos;
			}*/
			/*
			if(c == 'O') {
				if(old == 'O') {
					mtB += 1 + mabs(pos - O);
					t += 1 + mabs(pos - O);
				} else { //Switch!
					int ma = mabs(pos - O);
					if(D) fprintf(stderr, "switch B -> O: (%d, %d) mtO: %d, t: %d, ma: %d\n", O, B, mtO, t, ma);
					t += 1 + max(0, mabs(pos - O) - mtO);
					mtO = 0;
					mtB = mabs(pos - O)+1;
				}
				O = pos;
			} else { // B:
				if(old == 'B') {
					mtO += 1 + mabs(pos - B);
					t += 1 + mabs(pos - B);
				} else { //Switch!
					int ma = mabs(pos - B);
					if(D) fprintf(stderr, "switch O -> B: (%d, %d) mtB: %d, t: %d, ma: %d\n", O, B, mtB, t, ma);
					t += 1 + max(0, mabs(pos - B) - mtB);
					mtB = 0;
					mtO = mabs(pos - B)+1;
				}
				B = pos;
			}
			*/
			old = c;
		}
		printf("Case #%d: %d\n", i, t);
    }
	return 0;
}
