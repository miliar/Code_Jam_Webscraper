#include<cstring>
#include<cstdio>
#include<iostream>

using namespace std;

#define FOR(i,a,b) for(int i = (a);i<(b);i++)
#define max_n 105


int n,s,p;


int main(){
    int tC; scanf("%d\n",&tC);
    FOR(nrT,1,tC+1){
        int res = 0;
        int res2 = 0;
        scanf("%d %d %d",&n,&s,&p);
        FOR(i,0,n){
            int k; scanf("%d",&k);
            if((k+2) >= 3*p) res++;
            else if(k+3==3*p || k==3*p-4 ){
                if(k!=0) res2++;
            }
        }
        res = res+min(s,res2);

        printf("Case #%d: %d\n",nrT,res);
    }
    return 0;
}
