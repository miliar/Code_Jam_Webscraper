#include <iostream>
#include <string>
#include <vector>
#include <math.h>

using namespace std;

int getDigits (int a) {
    int count = 0;
    while (a!=0 && ++count) a /= 10;
    return count;
}

int myPow(int x, int p)
{
  if (p == 0) return 1;
  if (p == 1) return x;

  int tmp = myPow(x, p/2);
  if (p%2 == 0) return tmp * tmp;
  else return x * tmp * tmp;
}


int main() {
    int T,A,B,num,dig,a,b,maxa,minb,n,m,k,l;
    k=l=0;
    cin >>T;
    for (int t=0; t < T; t++) {
        num = 0;
        cin >>A >>B;
        dig = getDigits(A);
        for (int d = 1; d < dig; d++) {
            a = A/myPow(10,d);
            maxa = B/myPow(10,d);
            b = B/myPow(10,(dig-d));
            minb = A/myPow(10,(dig-d));
            for (int i = maxa; i >= a; i--) {
                for (int j = minb; j <= b; j++) {
                    n = (i*myPow(10,d))+j;
                    m = (j*myPow(10,(dig-d)))+i;
                    if (d > 2) {
                          k = ((m/myPow(10,d-2)) + ((m%myPow(10,d-2))*myPow(10,dig-d+2)));
                          l = ((m/myPow(10,d)) + ((m%myPow(10,d))*myPow(10,dig-d)));
                    }
                    if (A<=n && n < m && m <= B && (d <= 2 || k != l)) {
                        num++;
                    } 
                }
            }
        }
        cout <<"Case #" <<t+1 <<": " <<num <<endl;
    }
}
