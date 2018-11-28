#include <string>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <cstdio>
#include <utility>
#include <cctype>

using namespace std;

#define X first
#define Y second
#define For(A,B) for(int A=0;A<B.size();++A)
#define ll long long

int abs(int a){
    return (a>0)?a:-a;
}

int main(int argc, char *argv[])
{
    freopen("input.txt","r",stdin);
    int tests;
    cin >> tests;
    for(int tt=0;tt<tests;++tt){
        int n,posA=1,posB=1,timeA=0,timeB=0;
        cin >> n;
        char c;
        int pos;
        int time=0;
        for(int i=0;i<n;++i){
            cin >> c >> pos;
            if (c=='O') {
                timeA += abs(posA-pos)+1;
                if (timeA<=timeB) timeA=timeB+1;
                posA=pos;
            } else {
                timeB += abs(posB-pos)+1;
                if (timeA>=timeB) timeB=timeA+1;
                posB=pos;
            }
        }
        cout << "Case #"<<tt+1<<": "<<max(timeA,timeB) << endl;
    }
    return 0;
}
