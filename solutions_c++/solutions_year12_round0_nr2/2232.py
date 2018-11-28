#include<iostream>
#include <string.h>
#include<stdlib.h>
using namespace std;
int N, S, p;
int s[10000];


int get(){ int num=0;
    int snum=0;
    for(int i = 0; i < N;i++){
        int t = s[i];
        int k = t/3;
        if (k >= p) num++;
        else if (k >= p-1){
            int rem = t%3;
            if (k+rem >= p){
                num++;
            }
            else if(k && snum<S){ // rem==0
                    snum++;
                    num++;
            }
        }
        else
        {
            int rem = t%3;
            if (k + rem >=p ) {
                if (rem == 1) num++;
                else if(snum <S){
                    snum++; num++;
                }
            }
        }
    }return num;
}
int main(){
    int nu; cin >> nu; int casen=1;
    while (nu--){
        int i;
        cin >> N>>S>>p;
        for (i=0;i < N;i++) cin >> s[i];
        cout <<"Case #"<<casen++ << ": "<<get()<<endl;
    }
}


