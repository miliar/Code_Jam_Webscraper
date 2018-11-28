/*
 by messiah
 * 2010/5/8

 */
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <queue>
//ri
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <cmath>
using namespace std;

int t,i;

void solve(){
    int po, l, aa[111] = {0}, bb[100] = {0};
        char a[100];
        int O = 1, good = 0, bug = 1, abc = 0, bbb, to, temp, bushu = 0;
        cin >> l;
        /////////////////init()
        for (po = 0; po < l; po++) {
            cin >> a[po] >> temp;
            if (a[po] == 'B')
                aa[abc++] = temp;
            else
                bb[good++] = temp;
        }
        /*
  /////////////////////////////////////////

         */
        good = 0;
        abc=0;
        for (po = 0; po < l; po++) {
            if (a[po] == 'B') {
                if (bug < aa[abc])
                    bbb = 1;
                else//ijijiji
                    bbb = -1;
                if (O < bb[good])
                    to = 1;
                else {
                    to = -1;
                    //to=1;
                }
                while(1){
                    break;
                }
                for (; bug != aa[abc]; bug += bbb) {
                    bushu++;
                    if (O != bb[good])
                        //hihihi
                        O += to;
                    //huihi
                }
                bushu++;
                if (O != bb[good])
                    O += to;
                abc++;
            } else
                if (a[po] == 'O') {
                if (bug < aa[abc])
                    bbb = 1;
                else
                    bbb = -1;
                while(1)break;
                ////////////////////////////////////////////
                if (O < bb[good])
                    to = 1;
                else
                    to = -1;
                /////////////////////////////////////////////////////////
                for (; O != bb[good]; O += to) {
                    bushu++;
                    if (bug != aa[abc])
                        bug =bug+ bbb;
                }
                bushu++;
                if (bug != aa[abc])
                    bug =bug+ bbb;
                good++;
            }
        }
        cout << "Case #" << i << ": " << bushu << endl;

}
int main() {
   freopen("A-large (1).in","r",stdin);
   freopen("ltj2.txt","w",stdout);

    //int t, i;
    cin >> t;
    for (i = 1; i <= t; i++) {
        solve();
    }
}