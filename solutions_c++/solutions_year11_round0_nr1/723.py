#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

const int maxn = 110;

int a[maxn];
int b[maxn];
int t[maxn];
int acnt, bcnt;
char ch[maxn][10];
int n;


void Solve(int k){
    int ret = 0;
    int apos = 1;
    int bpos = 1;
    int aindex = 0;
    int bindex = 0;

    for(int i = 0; i < n; i ++){
        if(ch[i][0] == 'O'){
            int tmp = abs(t[i] - apos) + 1;
            ret += tmp;
            apos = t[i];

            if(tmp < abs(b[bindex] - bpos)){
                if(b[bindex] > bpos)
                    bpos += tmp;
                else
                    bpos -= tmp;
            }
            else
                bpos = b[bindex];
            aindex ++;
        }
        else{
            int tmp = abs(t[i] - bpos) + 1;
            ret += tmp;
            bpos = t[i];
            if(tmp < abs(a[aindex] - apos)){
                if(a[aindex] > apos)
                    apos += tmp;
                else
                    apos -= tmp;
            }
            else
                apos = a[aindex];
            bindex ++;
        }
    }

    cout << "Case #" << k << ": ";
    cout << ret << endl;
}

int main(){
//    freopen("A-large.in", "r", stdin);
//    freopen("out.txt", "w", stdout);

    int T;

    cin >> T;

    for(int k = 1; k <= T; k ++){
        cin >> n;
        acnt = 0;
        bcnt = 0;
        for(int i = 0; i < n; i ++){
            scanf("%s %d", ch[i], &t[i]);
            if(ch[i][0] == 'O')
                a[acnt ++] = t[i];
            else
                b[bcnt ++] = t[i];
        }

        Solve(k);
    }
}
