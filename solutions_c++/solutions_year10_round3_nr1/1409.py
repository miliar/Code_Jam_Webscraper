/* -*- c++ -*-
   ID: dirtysalt
   PROG: ???
   LANG: C++
   copy[write] by dirlt(dirtysalt1987@gmail.com) */
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstring>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <set>
#include <map>
#include <algorithm>
using namespace std;
int L[1000],R[1000];
int N;

int gcd(int a,int b){
    while(b){
        int tmp=a%b;
        a=b;
        b=tmp;
    }
    return a;
}

int go(){
    set< vector<int> >s;
    int res=0;
    for(int i=0;i<N-1;i++){
        for(int j=i+1;j<N;j++){
            int a=L[i],b=R[i],c=L[j],d=R[j];
            if((a-c)*(b-d)>0)
                continue;
            int u=(c-a);
            int v=(b*c-a*d);
            int w=(b+c-a-d);
            if(w<0){
                w=-w;
                v=-v;
                u=-u;
            }
            int g=gcd(gcd(u,v),w);
            u/=g;
            v/=g;
            w/=g;
            vector<int>vec;
            vec.push_back(u);
            vec.push_back(v);
            vec.push_back(w);
            if(s.find(vec)==s.end()){
                res++;
                s.insert(vec);
            }
        }
    }
    return res;
}

int main()
{
    int casn;
    cin>>casn;
    for(int t=1;t<=casn;t++){
        printf("Case #%d: ",t);
        cin>>N;
        for(int i=0;i<N;i++){
            cin>>L[i]>>R[i];
        }
        printf("%d\n",go());
    }
    return 0;
}
