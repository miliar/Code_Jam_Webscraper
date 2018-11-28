/* *************************
 * Author: xg1990
 * Created Time:  
 * LastModified:  Sat 28 Apr 2012 10:50:55 AM CST
 * C File Name: 
 * ************************/
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
#define out(v) cerr << #v << ": " << (v) << endl

int main() {

    freopen("A-small-attempt0.in","r",  stdin);
    freopen("A-small-attempt0.out","w",  stdout);

    int T;
    scanf("%d", &T);
    for( int t = 0 ; t < T ; ++t )
    {
        int A,B;
        vector<double> p;
        vector<double> pAllRight;
        vector<double> E;
        scanf("%d%d", &A, &B);
        //out(A);
        //out(B);
        p.resize(A + 1);
        pAllRight.resize(A + 1);
        E.resize(A);
        pAllRight[0] = 1;
        for(int i = 0; i < A; ++i)
            scanf("%lf", &p[i]);
        p[A] = 0;

        for(int i = 0; i <= A; ++i){
            if(i == 0)pAllRight[i] = 1;
            else pAllRight[i] = pAllRight[i - 1] * p[i - 1];
            //if(i)printf("pAllRight[%d] = %f * %f\n", i, pAllRight[i - 1], p[i - 1]);
            for(int j = 1; j <= A; ++j){
                if(A - j <= i){
                    E[j - 1] += pAllRight[i] * (1 - p[i]) * ( B - A + 2 * j + 1);
                    //printf("E[%d] += %f * %d\n", j - 1,pAllRight[i] * (1 - p[i]),( B - A + 2 * j + 1) );
                }
                else{
                    E[j - 1] += pAllRight[i] * (1 - p[i]) * ( 2*B - A + 2 * j + 2);
                    //printf("E[%d] = %f * %d\n", j - 1,pAllRight[i] * (1 - p[i]),( 2*B - A + 2 * j + 2));
                }
            }
        }
        double E1 = 0,  E3 = 0, ans = B * B;
        E1 = pAllRight[A] * (B - A + 1) + (1 -pAllRight[A]) * (2*B - A + 2);
        E3 = 2 + B;
        //out(E1);
        //out(E3);
        //out(ans);
        ans = min(ans, E1);
        //out(ans);
        ans = min(ans, E3);
        //out(ans);
        for(int j = 0; j < A; ++j){
            ans=min(ans, E[j]);
        //out(ans);
        }
        printf("Case #%d: %.6f\n", t + 1, ans);
    }
    
    return 0;
}


