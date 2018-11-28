#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <memory.h>
#include <string>
#include <math.h>

using namespace std;

#define fori(i,j,k) for(int i=j;i<k;i++)
#define ford(i,j,k) for(int i=j-1;i>=k;i--)
#define i64 __int64
#define ld long double
#define mp make_pair

const char p[27]="ABCDEFGHIJKLMNOPQRSTUVWXYZ";

int main()
{
    int t;
    scanf("%d\n",&t);
    fori(h,0,t){
        int n;
        map<pair<char,char>,char> x;
        map<char,char> y;
        vector<char> z;
        scanf("%d ",&n);
        char a,b,c;
        fori(i,0,27)
            fori(j,0,27){
                x[mp(p[i],p[j])]=' ';
                y[p[i]]=' ';
            }
        fori(i,0,n){
            scanf("%c%c%c ",&a,&b,&c);
//            printf("%c%c%c ",a,b,c);
            x[mp(a,b)]=c;
            x[mp(b,a)]=c;
        }
        scanf("%d ",&n);
        fori(i,0,n){
            scanf("%c%c ",&a,&b);
            y[a]=b;
            y[b]=a;
        }
        scanf("%d ",&n);
        fori(i,0,n){
            scanf("%c",&a);
            
            if(!z.empty()){
                char d=z.back();
                if(x[mp(a,d)]!=' ') {z.pop_back(); z.push_back(x[mp(a,d)]);}
                else{
                    int r=0;
                    for(vector<char>::iterator it=z.begin();it!=z.end();it++){
                        //printf("%c %c %c|",*it,a,y[a]);
                        if(y[a]==*it) {z.clear(); r=1;break;}
                    }
                    if(r==0) z.push_back(a);
                }    
            }
            else z.push_back(a);
        }
        printf("Case #%d: [",h+1);
        vector<char>::iterator it=z.begin();
        while(it!=z.end()){
            printf("%c",*it);
            it++;
            if(it!=z.end()) printf(", ");
        }
        
        printf("]\n");
    }
    
    return 0;
}
