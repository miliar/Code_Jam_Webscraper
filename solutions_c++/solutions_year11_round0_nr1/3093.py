#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#define REP(i,t) for(i=0;i<t;i++)


int main(void){

int nCases, i,j;
int total,N, a[100], p[2], f[100];
char c;
int ant, antp;
scanf("%i\n", &nCases);

REP(i,nCases){
total = 0;

scanf("%i ", &N);

REP(j,N){
scanf("%c %i ", &c, a+j);
if(c=='B')f[j] = 0;
else f[j] = 1;


}
ant =0;

p[0] = p[1] = 1;
int alt = 0;
REP(j, N){
    if(j==0){antp = f[j];alt = (f[j]==0 ? 1 : 0);}


    if(antp!=f[j]){

        if(a[j]>p[f[j]]){
            if(p[f[j]]+ant<a[j])
            p[f[j]] += ant;
            else  p[f[j]]= a[j];
            }else{
        if(p[f[j]]-ant > a[j])

        p[f[j]] -= ant ;
        else p[f[j]] = a[j];
            }


ant = 0;
        }

    total+=abs(a[j]-p[f[j]])+1;


ant += (abs(a[j]-p[f[j]])+1);


 p[f[j]] = a[j];

antp = f[j];
}









printf("Case #%i: %i\n", i+1, total);
}


}
