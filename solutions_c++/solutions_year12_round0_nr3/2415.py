/* 
 * File:   recyle.cc
 * Author: vivek
 *
 * Created on April 14, 2012, 6:37 PM
 */

#include <cstdlib>
#include <cstdio>
#include <map>
#include <utility>
using namespace std;

/*
 * 
 */
typedef map<pair<int,  int>,int> MapType;
 int main(int argc, char** argv) {
    int t;
    int i,j,temp,k,d,l;
     int a,b;
    int ans=0;
     int mid;
     int p;    
    MapType m;
    scanf("%d", &t);
    i=0;
    while(t--){
        ++i;
        scanf("%d",&a);
        scanf("%d",&b);        
        ans=0; 
        d=1;
        m.clear();
        for(temp=b;temp>10;temp/=10){
            d*=10;
        }        
        if(a < 10 || b < 10){
            ans=0;
        }else{
            for(j=a;j<b;j++){
                for(k=10,l=d;k<=d;k*=10,l/=10){
                    temp=(j%k)*l+(j/k);                    
                    if(temp>b){
                        continue;
                    }
                    if(temp<j){
                        continue;
                    }
                    
                    if(a<=temp && j!=temp && temp>j){                        
                        m[std::make_pair(j,temp)]=1;                                                
                        ans++;                        
                    }                    
                }
                endj:;
            }
        }
        printf("Case #%d: %d\n",i,m.size());                  
    }
    return 0;
}

