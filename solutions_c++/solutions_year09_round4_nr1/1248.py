#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <cmath>
#define  f(x,y,i) for(int i=x;i<y;i++)
//f(0,M,i){f(0,2,j)printf("%d",C[i][j]); printf("\n");}
using namespace std;

int T,n; char cad[50];

int rec(vector<int> A){
    int m=INT_MAX;
    bool ya=1;
    f(0,A.size(),i)if(A[i]>i+1)ya=0;
    if(ya)return 0;
    f(0,A.size(),i)if(A[i]<=1){
        vector<int> B(A.size()-1,0);
        f(0,A.size()-1,j)if(j>=i)B[j]=A[j+1]-1;else B[j]=A[j]-1;
        m<?=i+rec(B);
    }
    return m;
}

int main()
{
    scanf("%d",&T);
    f(1,T+1,caso){
        scanf("%d\n",&n);
        vector<int> A(n,0);
        f(0,n,i){
            gets(cad);
            f(0,n,j)if(cad[j]=='1')A[i]=j+1;
        }
        printf("Case #%d: %d\n",caso,rec(A));
    }
}
