#include <algorithm>
#include <iostream>
#include <sstream>
#include <string.h>
#include <string>
#include <queue>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <vector>
#include <map>
#include <math.h>
#include <stdio.h>
using namespace std;

int main(){
    int T;
    scanf("%d",&T);
    for (int c=0;c<T;c++){
        double mint;
        int x,n,s,r,t;
        scanf("%d %d %d %d %d",&x,&s,&r,&t,&n);
        vector<pair<int,pair<int,int> > > v;
        vector<pair<pair<int,int> ,int> > v1;
        for (int i=0;i<n;i++){
            int b,e,dv;
            scanf("%d %d %d",&b,&e,&dv);
            v.push_back(make_pair(dv,make_pair(b,e)));
            v1.push_back(make_pair(make_pair(b,e),dv));
            }
        sort(v1.begin(),v1.end());
        int st=0;
        for (int i=0;i<v1.size();i++){
            if (v1[i].first.first>st) v.push_back(make_pair(0,make_pair(st,v1[i].first.first)));
            st=v1[i].first.second;
            }
        if (st<x) v.push_back(make_pair(0,make_pair(st,x)));

        sort(v.begin(),v.end());
        for (int i=0;i<v.size();i++) {
            //printf("%d %d %d\n",v[i].first,v[i].second.first,v[i].second.second);

            }

        double T=t;
        mint=0;
        for (int i=0;i<v.size();i++){
            if (T-(double)(v[i].second.second-v[i].second.first)/(double)(r+v[i].first)>0){
                mint=mint +(double)(v[i].second.second-v[i].second.first)/(double)(r+v[i].first);
                T=T-(double)(v[i].second.second-v[i].second.first)/(double)(r+v[i].first);
                } else {
                   if (T>0) {mint = mint+T+(double)(v[i].second.second-v[i].second.first-(r+v[i].first)*T)/(double)(s+v[i].first); T=0;} else mint=mint+(double)(v[i].second.second-v[i].second.first)/(double)(s+v[i].first);
                    }
            //printf("%.7f %f\n ",mint,T);
            }
        printf("Case #%d: %.8f\n",c+1,mint);
        }
    return 0;
    }
