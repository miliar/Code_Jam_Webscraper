#include<iostream>
#include<stdio.h>

using namespace std;

#define _abs(a) ((a)>=0?(a):(-(a)))

int main()
{
//    freopen("in.txt","r",stdin);
//    freopen("out.txt","w",stdout);
    
    int t;
    cin>>t;
    int cas=1;
    while(t--){
        int ot=0,bt=0;
        int oi=1,bi=1;
        int n;
        cin>>n;
        int i;
        for(i=0;i<n;i++){
            char op;
            int ind;
            cin>>op>>ind;
            if(op=='O'){
                if(ot+_abs(ind-oi)+1>bt) ot+=_abs(ind-oi)+1;
                else ot=bt+1;
                oi=ind;
            }
            else{
                if(bt+_abs(ind-bi)+1>ot) bt+=_abs(ind-bi)+1;
                else bt=ot+1;
                bi=ind;
            }
        }
        if(bt>ot) ot=bt;
        printf("Case #%d: %d\n",cas++,ot);
    }
}
