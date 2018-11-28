#include <stdio.h>
#include <iostream>
#include <sstream>
#include <stdlib.h>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <math.h>
#include <algorithm>
#include <map>

using namespace std;

typedef pair<int,int>PII;
typedef pair<PII,int>PII2;

double in[205];
int n;
double sum;
bool solve(double score, double mid, int player){
    double minn = 0;
    int out = 1;
    for(int i=0;i<n;i++){
        if(i != player){
            if(in[i] > score) continue;
            else {
                out = 0;
                double diff = score - in[i];
                minn += diff * 100.0 / sum;
            }
        }
    }
    
    if(out)
        return false;
    if(minn + mid < 100.000001){
        return false;
    }
    return true;
        
}

class Solve {
    public:
    void main2(){
        sum = 0;
        scanf("%d",&n);
        for(int i=0;i<n;i++){
            scanf("%lf",&in[i]);
            sum += in[i];
        }
        for(int i=0;i<n;i++){
            double left = 0.0, right = 100.0;
            
            while(right - left >= 0.000001){
                double mid = (right + left) / 2;
                double score = in[i] + mid * sum / 100;
             //   printf("%lf %lf %lf\n", mid, score, sum);
             //   while(1);
                if(!solve(score, mid, i)) left = mid;
                else right = mid;
            }
            
            printf(" %lf", right);
        }
        printf("\n");
    }
};

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int Test;
    scanf("%d",&Test);
    for(int t=1;t<=Test;t++){
        Solve ___test;
        printf("Case #%d:", t);
        ___test.main2();
    }
return 0;
}
