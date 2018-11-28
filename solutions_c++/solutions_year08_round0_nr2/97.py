#include <stdio.h>
#include <vector>
#include <algorithm>
#define ARR 0
#define DEP 1
using namespace std;
char buffer[10000];

int main(){
    int ntc, ttc=0;
    scanf("%d", &ntc);
    while (ntc--){
        int t;
        scanf("%d", &t);
        vector<pair<int,int> > ardepA;
        vector<pair<int,int> > ardepB;
        
        int n,m;
        scanf("%d%d", &n,&m);
        gets(buffer);
        for (int i=0;i<n;i++){
            gets(buffer);
            int a=(buffer[0]-'0')*10+(buffer[1]-'0'),
                b=(buffer[3]-'0')*10+(buffer[4]-'0'),
                c=(buffer[6]-'0')*10+(buffer[7]-'0'),
                d=(buffer[9]-'0')*10+(buffer[10]-'0');

            int t1 = a*60+b;
            int t2 = c*60+d+t;
            
            ardepA.push_back(make_pair(t1, DEP));            
            ardepB.push_back(make_pair(t2, ARR));            
        }
        for (int i=0;i<m;i++){
            gets(buffer);
            int a=(buffer[0]-'0')*10+(buffer[1]-'0'),
                b=(buffer[3]-'0')*10+(buffer[4]-'0'),
                c=(buffer[6]-'0')*10+(buffer[7]-'0'),
                d=(buffer[9]-'0')*10+(buffer[10]-'0');

            int t1 = a*60+b;
            int t2 = c*60+d+t;
            
            ardepB.push_back(make_pair(t1, DEP));            
            ardepA.push_back(make_pair(t2, ARR));            
        }
        sort(ardepA.begin(), ardepA.end());
        sort(ardepB.begin(), ardepB.end());
        int maxa=0;
        int maxb=0;
        int cur=0;
        for(int i=0;i<ardepA.size();i++){
            if (ardepA[i].second == DEP) cur++;
            else cur--;
            
            maxa>?=cur;
        }
        cur=0;
        for(int i=0;i<ardepB.size();i++){
            if (ardepB[i].second == DEP) cur++;
            else cur--;
            
            maxb>?=cur;
        }
        printf("Case #%d: %d %d\n", ++ttc, maxa, maxb);
    }
    
    return 0;
}
