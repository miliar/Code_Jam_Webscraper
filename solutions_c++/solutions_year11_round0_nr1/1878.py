#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
using namespace std;

int oq[101],bq[101];
int op[101],bp[101];

int main() {
    int t,n,p;
    string s;
    cin>>t;
    for(int tc=1; tc<=t; ++tc) {
        cin>>n;
        memset(oq, -1, sizeof(oq));
        memset(bq, -1, sizeof(bq));
        memset(op, 0x7f, sizeof(op));
        memset(bp, 0x7f, sizeof(bp));
        int bs=0,os=0;
        for(int i=0; i<n; ++i) {
            cin>>s>>p;
            if(s == "O") {
                op[os] = i;
                oq[os++] = p;
            }else if(s == "B") {
                bp[bs] = i;
                bq[bs++] = p;
            }
        }

        int bpos = 1, opos = 1, ans = 0, bd = 0, od = 0;
        while(true) {
//            cout<<ans<<" "<<bpos<<" "<<opos<<endl;
            if(oq[od] == -1 && bq[bd] == -1) break;
            int oneed = abs(oq[od] - opos) + 1;
            int bneed = abs(bq[bd] - bpos) + 1;
            if(op[od] < bp[bd]) {
                ans += oneed;
                opos = oq[od];
                od++;
                if(abs(bq[bd]-bpos) <= oneed) bpos = bq[bd];
                else bpos = (bpos > bq[bd])?bpos-oneed:bpos+oneed;
            }else{
                ans += bneed;
                bpos = bq[bd];
                bd++;
                if(abs(oq[od]-opos) <= bneed) opos = oq[od];
                else opos = (opos > oq[od])?opos-bneed:opos+bneed;
            }
        }
        cout<<"Case #"<<tc<<": "<<ans<<endl;
    }
}

