#include  <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int field[64][64];

typedef vector<string> VS;

void output(VS v) {
    cout << endl;
    for(int i=0;i<v.size();i++) cout << v[i] << endl;
}

int doit(int kase) {
    for(int i=0;i<64;i++)
        for(int j=0;j<64;j++) field[i][j] = 0;
    int N,K;
    cin >> N >> K;
    string s;
    VS v;
    for(int i=0;i<N;i++) {
        cin >> s;
        v.push_back(s);
    }
//    output(v);
    for(int col=0;col<N;col++) {
        int h = N-1;
        for(int j=N-1;j>=0;j--) 
            if(v[col][j]!='.') {
                swap(v[col][h], v[col][j]);
//                v[col][j] = '.';
                h--;
            }
    }
//    output(v);
    int who = 0;
    int red = 1,blue = 2;
    for(int i=0;i<N;i++) {
        for(int j=0;j<N;j++) {
            int ok=1;
            int what = v[i][j];

            ok=1;
            //y:
            for(int k=0;k<K;k++) {
                if((i+k)<N && v[i+k][j] == what) ok = 1;
                else{
                    ok = 0;
                    break;
               }
            }
            if(ok) {
                if(what == 'B') who |= blue;
                if(what == 'R') who |= red;
            }

            ok=1;
            //x:
            for(int k=0;k<K;k++) {
                if((j+k)<N && v[i][j+k] == what) ok = 1;
                else{
                    ok = 0;
                    break;
               }
            }
            if(ok) {
                if(what == 'B') who |= blue;
                if(what == 'R') who |= red;
            }

            ok=1;
            //x,y:
            for(int k=0;k<K;k++) {
                if((i+k)<N && (j+k) < N&& v[i+k][j+k] == what) ok = 1;
                else{
                    ok = 0;
                    break;
               }
            }
            if(ok) {
                if(what == 'B') who |= blue;
                if(what == 'R') who |= red;
            }

            ok=1;
            //x,y:
            for(int k=0;k<K;k++) {
                if((i-k)>=0 && (j+k) < N&& v[i-k][j+k] == what) ok = 1;
                else{
                    ok = 0;
                    break;
               }
            }
            if(ok) {
                if(what == 'B') who |= blue;
                if(what == 'R') who |= red;
            }
        }
   }
   //cout << "foo: " <<  who << endl;
   printf("Case #%d: ",kase);
   if(who==0) puts("Neither");
   if(who==1) puts("Red");
   if(who==2) puts("Blue");
   if(who==3) puts("Both");
   return 0;
}

int main(){
    int N;
    cin >> N;
    for(int i=0;i< N;i++) doit(i+1);
    return 0;
}
