#include <iostream>
#include <string>
#include "stdio.h"
#include <cmath>
using namespace std;

int getDigit(int num){
    int tot=0;
    while (num > pow(10,tot)) tot++;
    return tot;
}

int getPair(int num,int move,int tot){
    int pa,pb;
    pa=num%(int)pow(10,move);
    pb=(num-pa)/pow(10,move);
    return pa*pow(10,tot-move)+pb;
}



int main(){
    int res,pres,dig,p,n,a,b,z;
    scanf("%d",&n);
    for (int i=0;i<n;i++){
        res=0;
        scanf("%d %d",&a,&b);
        for (int j=a;j<=b;j++){
            dig=getDigit(j);
            for (z=1;z<dig;z++){
                p=getPair(j,z,dig);
                if (p>=a && p<=b && p!=j && p>j) {res++;}
            }
        }
        printf("Case #%d: %d",(i+1),res);
        if (i<n-1) cout << endl;
    }

    return 0;
}
