#include <iostream>
#include <string>
#include "stdio.h"
using namespace std;




int main(){


    int t,n,s,p,res,min,max,inp;
    scanf("%d\n",&t);
    for (int i=0;i<t;i++){
        res=0;
        scanf("%d %d %d",&n,&s,&p);
        min=3*p-4;
        max=3*p-3;
        if (p<2) {min=10;max=p-1;};
        for (int j=0;j<n;j++){
            scanf("%d",&inp);
            if (inp > max) res++;
            else if (inp >=min && s>0) {res++;s--;}
        }
        printf("Case #%d: %d",(i+1),res);
        if (i<t-1) cout << endl;
    }

    return 0;
}
