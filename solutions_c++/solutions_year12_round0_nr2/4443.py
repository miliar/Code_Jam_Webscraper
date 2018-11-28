#include <iostream>
#include <map>
#include <set>
using namespace std;

set<int> num[40];
void fill();
int* check(int point, int p);

int main() {
    fill();
    int test;
    cin >> test;
    
    for(int i = 1; i <= test; ++i) {
        int N, S, p;
        cin >> N >> S >> p;
        int t[150];
        for(int j = 0; j < N; ++j) {
            cin >> t[j];
        }
        
        int result = 0;
			//int high[] = new int[N], strict[] = new int[N], nons[] = new int[N];
			int high = 0, strict = 0, nons = 0;
			for(int j = 0; j < N; ++j) {
				int *temp = check(t[j], p);
				high += temp[0];
				nons += temp[1];
				strict += temp[2];
			}
//			System.out.println(N + " " + S + " " + p);
//			System.out.println(high + " " + nons + " " + strict);
			if(nons < S) {
				result = 0;
			}
			else {		
				if(strict > S) {
					result = high + S -strict;
				}
				else {
					result = high;
				}
			}
			cout << "Case #" << i << ": " << result << endl;
			
    }
}

void fill() {
    for(int i = 0; i <= 10; ++i) {
        for(int j = i; j <= i+2; ++j) {
            for(int k = j; k <= i+2; ++k) {
                int sum = i+j+k;
                int d1 = k-i, d2 = j-i;
                if(d1 == 2) {
                    if(d2 < 2) {
                        num[3*k+2].insert(sum);
                    }
                    else {
                        num[3*k+1].insert(sum);
                    }
                }
                else {
                    num[3*k].insert(sum);
                }
            }
        }
    }
}

int* check(int point, int p) {
    int* r = new int[3];
    
    for(int i = 0; i < 33; ++i) {
        if(num[i].find(point) != NULL) {
            if(i/3 >= p) {
				r[0] = 1;
				if(i%3 == 2 && r[2] >= 0) {
					r[2] = 1;
				}
				else {
					r[2] = -1;
				}
			}
			if(i%3 != 0) {
				r[1] = 1;
			}
        }
    }
    
    if(r[2] < 0) {
		r[2] = 0;
	}
    
    return r;
}
