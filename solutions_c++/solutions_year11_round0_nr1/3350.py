#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

#define rei(i,a,b) for(int i=a;i<b;i++)
#define red(i,a,b) for(int i=a;i>=b;i--)
#define ree(i,a,b) for(int i=a;i<=b;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define pb(a,x) a.push_back(x)
#define all(a) a.begin(),a.end()
#define srt(a) sort(all(a))
#define rev(a) reverse(all(a))


int main(){
    int test;
    scanf("%d",&test);
    rei(i,0,test){
        int numOfButtons;
        scanf("%d",&numOfButtons);
        int posA=1,posB=1;
        vector<int> togoA,togoB;
        int aCovered=0,bCovered=0;
        int seq[101][2];
        mem(seq,0);
        rei(j,0,numOfButtons){
            char bot[1];
            int door;
            scanf("%s",bot);
            scanf("%d",&door);
            if(bot[0]=='B'){
                pb(togoB,door);
                seq[j][0]=2;seq[j][1]=door;
            }else{
                pb(togoA,door);
                seq[j][0]=1;seq[j][1]=door;
            }
        }
        int ret=0;
        rei(j,0,numOfButtons){
            if(seq[j][0]==1){
                int timeA=abs(posA-seq[j][1]);
                ret+=(timeA+1);
                int timeB=0;
                if(bCovered<togoB.size())
                    timeB=min(abs(posB-togoB[bCovered]),timeA+1);
                aCovered++;
                posA=seq[j][1];
                if(bCovered<togoB.size())
                    posB=(togoB[bCovered]>posB)?posB+timeB:posB-timeB;
            }else{
                int timeB=abs(posB-seq[j][1]);
                ret+=(timeB+1);
                int timeA;
                if(aCovered<togoA.size())
                    timeA=min(abs(posA-togoA[aCovered]),timeB+1);
                bCovered++;
                posB=seq[j][1];
                if(aCovered<togoA.size())
                    posA=(togoA[aCovered]>posA)?posA+timeA:posA-timeA;
            }
        }
        printf("Case #%d: %d\n",i+1,ret);
    }
}
