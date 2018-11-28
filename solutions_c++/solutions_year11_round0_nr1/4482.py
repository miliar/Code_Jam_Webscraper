#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

inline int abs(int a){
    return a<0?-1*a:a;
}


int main(){
    int time = 0, n, last,tlast, p, m;
    char c;
    scanf("%d", &m);
    for(int l=0; l<m; ++l){
        vector<int> order, t[2];
        time=0;
        scanf("%d", &n);
        for(int i=0; i<n; ++i){
            cin >> c >> p;
            t[c=='O'?0:1].push_back(p);
            order.push_back(c=='O'?0:1);
        }
        last= 1;
        for(vector<int>::iterator it=t[0].begin(); it!=t[0].end(); ++it){
            tlast = *it;
            *it = abs(last - *it);
            last = tlast;
        }
        last= 1;
        for(vector<int>::iterator it=t[1].begin(); it!=t[1].end(); ++it){
            tlast = *it;
            *it = abs(last - *it);
            last = tlast;
        }
        
        vector<int>::iterator it0 = t[0].begin(), it1 = t[1].begin(), ord = order.begin();
        while(ord!=order.end()){
            if(*ord){
                *it1=*it1+1;
                time+=*it1;
                if(it0!=t[0].end()){
                    *it0-=*it1;
                    *it0=max(*it0, 0);
                }
                it1++;
            }
            else{
                *it0=*it0+1;
                time+=*it0;
                if(it1!=t[1].end()){
                    *it1-=*it0;
                    *it1=max(*it1, 0);
                }
                it0++;
            }
            ord++;
        }
        printf("Case #%d: %d\n",l+1, time);
    }
    return 0;
}
