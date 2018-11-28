#include <stdio.h>
#include <iostream>
#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <math.h>
#include <stdlib.h>
#include <list>

using namespace std;

/*
bool isPrime[];

void prime(int n)
{
    int i,j,end;

    memset(isPrime,true,sizeof(isPrime));

    end = sqrt(n) +1;
    for (i=2; i<end; i++)
        if (isPrime[i]) {
            for(j=i*2; j<1001; j+=i)
                isPrime[j] = false;
        }
}
*/

#define for0(i,n)  for ((i)=0; (i)<(n); (i++))
#define for1(i,n)  for ((i)=1; (i)<=(n); (i++))
#define foriter(i,v)  for ((i)=(v).begin(); (i)!=(v).end(); (i)++)

char done[2000001];
int ans;
set< pair<int,int> > have;

int main()
{
    int i,j,k,T,tt;
    int A,B,n,x;
    char temp[10];

    scanf("%d", &T);

    for0(tt,T) {
        scanf("%d %d", &A, &B);

        //memset(done, 0, sizeof(done));
        have.clear();
        ans = 0;

        itoa(B, temp, 10);
        string sB(temp);
        n = sB.length();
        //printf("n= %d\n", n);

        for (i=A; i<B; i++) {
            sprintf(temp, "%0*d", n, i);
            //printf("%s", temp);
            string s(temp);

            for0(j,n) {
                x = atoi(s.c_str());
          //      if (!done[x]) {
            //        done[x] = 1;
                    if (x >i && x<=B) {

                        if (have.find(make_pair(i,x)) == have.end()) {
                            have.insert(make_pair(i,x));
                            ans++;
                        }

                        /*
                        else
                            printf("the same: %d %d\n", i,x);
                            */
                    }
              //  }
                s = s.substr(1,n-1) + s[0];
            }
        }

        printf("Case #%d: %d\n", tt+1, ans);
    }
}
