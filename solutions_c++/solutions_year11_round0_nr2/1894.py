//Magicka
#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <map>
#include <cstring>
#include <set>
#include <algorithm>
#include <cmath>
using namespace std;
int c,d,n,len;
string   s,cur ;
char a['Z'+1]['Z'+1] ,b['Z'+1]['Z'+1] ;
void print(string x){
    if (!x.length()) {cout << "[]" << endl;return ;}
    cout << "[" << x[0];
    for(int i = 1;i<x.length()  ; i++)
        cout << ", " << x[i];
    cout << "]" << endl;
}

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int ntest;
    cin >> ntest;
    for(int r = 0;r<ntest;r++){
        memset(a,'#',sizeof(a));
        memset(b,'#',sizeof(b));
        cin >> c;
        while (c--){
            string st;
            cin >> st;
            a[st[0]][st[1]]= st[2];
            a[st[1]][st[0]]= st[2];
        }
        cin >> d;
        for(int i = 0; i<d ; i++) {
            string st;
            cin >> st;
            b[st[0]][st[1]]= '@';
            b[st[1]][st[0]]= '@';
        }
        cin >> n;
        cin >> s;
        cur = "";
        for(int i = 0;i<n;i++){
            cur = cur + s[i];
            //cout << cur << endl;
            len = cur.length();
            if (len < 2) continue;
            char tmp = a[cur[len-2]][cur[len-1]];
            if (tmp != '#')
                cur.replace(len-2,2,1,tmp);
            len = cur.length();;
            bool found = false;
            for(int ii = 0;ii<len; ii++){
                for(int jj = ii+1 ; jj<len;jj++)
                 if (b[cur[ii]][cur[jj]] == '@'){
                    cur = "";
                    found = true;
                    break;
                }
                if (found) break;
            }

        }
        cout << "Case #"<<r+1<<": ";
        print(cur);
    }
    //cout << "Hello world!" << endl;
    return 0;
}
