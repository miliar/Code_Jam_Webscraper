#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>

#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
using namespace std;
typedef long long LL;
typedef pair<LL,LL> PII;
typedef pair<LL,LL> PI;
typedef vector<PII> VPI;
typedef vector<PI> VI;

const int MAXN = 1010;
LL roundIndex[MAXN][MAXN];
queue<PII> myQ;
VI roundData;
vector<LL> roundValue;
int toCell()
{
}

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int T;cin>>T;

    for(int tc=1;tc<=T;tc++) {
        memset(roundIndex,-1,sizeof(roundIndex));
        LL ret = 0;
        while(!myQ.empty())myQ.pop();
        LL rounds, capacity, groups;
        cin>>rounds>>capacity>>groups;
        for(LL i=0;i<groups;i++) {
            LL v;cin>>v;
            myQ.push(PII(i,v));
        }

        //clear roundData
        roundData.clear();
        roundValue.clear();
        for(LL i = 0; i < rounds; i++) {
            LL first = 0, last = 0, flag = 1, taken=0;
            LL sum = 0;
            while(taken<groups) {
                PII p = myQ.front();
                LL v = p.second;
                if(v>capacity-sum) break;
                myQ.pop();
                myQ.push(p);
                if(flag) {
                    first = last = p.first;
                    flag=0;
                }
                last = p.first;
                sum=sum+v;
                taken++;
            }
            ret+=sum;

            if(roundIndex[first][last]==-1) {
                roundIndex[first][last]=roundData.size();
                roundData.push_back(PI(first,last));
                roundValue.push_back(sum);
            }
            else {
  //              cout<<first<<" d "<<last<<endl;
                rounds-=i;
                ret-=sum;
                LL size = roundData.size();
                LL total = size-roundIndex[first][last];
                LL value = 0;
                for(LL k = roundIndex[first][last]; k < size; k++) {
                    value+=roundValue[k];
                }
                LL q = rounds/total;
                LL qsum = q * value;
                LL r = rounds%total;
                LL rsum=0;

                for(LL k=roundIndex[first][last]; k < roundIndex[first][last] + (int)r;k++) {
                    rsum+=roundValue[k];
                }
                ret+=qsum+rsum;


                break;
            }


        }

        cout<<"Case #"<<tc<<": "<<ret<<endl;
    }
    return 0;
}
