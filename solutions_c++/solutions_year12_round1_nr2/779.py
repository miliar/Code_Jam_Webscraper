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

struct node{
    int x;
    int index;
} a[1002], b[1002];

bool done[2][1002];

int mycmp (const void* x, const void* y) {
    node* i = (node*)x;
    node* j = (node*)y;
    return (i->x - j->x);
}

int A[1002], B[1002];


int main()
{
    int i,j,k,T,tt;
    int n,start,complete,times,index_a, index_b;
    bool possible;

    scanf("%d", &T);

    for0(tt,T) {
        scanf("%d", &n);

        for0(i,n) {
            scanf("%d %d", A+i, B+i);
            a[i].x = A[i];
            b[i].x = B[i];
            a[i].index = i;
            b[i].index = i;
        }

/*
        for0(i,n) {
            printf("%d ", b[i].x);
        }
        printf("\n");
*/
        qsort(a, n, sizeof(node), mycmp);
        qsort(b, n, sizeof(node), mycmp);
/*
        for0(i,n) {
            printf("%d ", b[i].x);
        }
        printf("\n");
*/
        start = complete = times = 0;
        possible = true;
        index_a = index_b = 0;
        memset(done, 0, sizeof(done));

        while (index_b != n) {
/*
            for0(i,n) {
                printf("%d %d\n", done[0][i], done[1][i]);
            }
            printf("start = %d\n", start);


            printf("BB%d\n", b[index_b].x);
  */          if (b[index_b].x <= start) {
                done[1][b[index_b].index] = true;
                start++;

                if (done[0][b[index_b].index] == false) {
                    done[0][b[index_b].index] = true;
                    start++;
                }
                index_b++;
                times++;
                continue;
            }

            int max = -1;
            index_a = -1;
            for0(i,n) {
                if (!done[0][i] && A[i] <= start && max< B[i]) {
                    max = B[i];
                    index_a = i;
                }
            }
            if (index_a == -1) {
                possible = false;
                break;
            }else {
                start++;
                done[0][index_a] = true;
                times++;
            }

        }

        if (possible)
            printf("Case #%d: %d\n", tt+1, times);
        else
            printf("Case #%d: Too Bad\n", tt+1);
    }
}
