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

//int A[30], B[30];
int num[30];
vector<int> ansa, ansb;
int n;

bool equal(vector<int> A, vector<int> B)
{
int i;
/*
     for0(i, A.size()) {
        printf("%d ", A[i]);
    }
    printf("\n");

    for0(i, B.size()) {
        printf("%d ", B[i]);
    }
    printf("\n");
*/

    if (A.empty() || B.empty())
        return false;

    int ca = 0, cb = 0;

    for0(i, A.size())
        ca += A[i];

    for0(i, B.size())
        cb += B[i];

    if (ca == cb) {
        ansa = A;
        ansb = B;
        return true;
    }
    else
        return false;
}

bool find(vector<int> A, vector<int> B, int x)
{
 /*    printf("\n\nfind");
     int i;
     for0(i, A.size()) {
                if (i != A.size()-1)
                    printf("%d ", A[i]);
                else
                    printf("%d\n", A[i]);
            }
            for0(i, B.size()) {
                if (i != B.size()-1)
                    printf("%d ", B[i]);
                else
                    printf("%d\n", B[i]);
            }
*/
    if (x == n)
        return false;

    vector<int> a = A,b = B;


    if (equal(a,b))
        return true;
    else if (find(a,b,x+1))
        return true;

    a.push_back(num[x]);
   // printf("size: %d %d\n", a.size(), b.size());
    if (equal(a,b))
        return true;
    else if (find(a,b,x+1))
        return true;

    a = A;
    b.push_back(num[x]);
    if (equal(a,b))
        return true;
    else if (find(a,b,x+1))
        return true;

    return false;
}

int main()
{
    int i,j,k,T,tt;
    int total;

    scanf("%d", &T);

    for0(tt,T) {
        scanf("%d", &n);
        for0(i,n) {
            scanf("%d", num+i);
            total += num[i];
        }

        total /= 2;
        total++;
        vector<int> A,B;

        bool ans;
        ans = find(A,B,0);

        printf("Case #%d:\n", tt+1);
        if (ans) {
            for0(i, ansa.size()) {
                if (i != ansa.size()-1)
                    printf("%d ", ansa[i]);
                else
                    printf("%d\n", ansa[i]);
            }
            for0(i, ansb.size()) {
                if (i != ansb.size()-1)
                    printf("%d ", ansb[i]);
                else
                    printf("%d\n", ansb[i]);
            }
        }else
            printf("Impossible\n");
    }
}
