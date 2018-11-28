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
        int n;
        cin >> n;
        vector<int> m(n);
        for(int i=0;i<n;++i){
            cin >> m[i];
        }
        int r=m[0];
        for(int i=1;i<n;++i){
            r^=m[i];
        }

        if (r!=0){
            cout << "Case #"<<tt+1<<": NO" << endl;
        } else {
            int mx=0;
            for(int i=0;i<n;++i){
                int r=0,xx=0;
                for(int j=0;j<n;++j){
                    if (i!=j){
                        r^=m[j];
                        xx+=m[j];
                    }
                }
                mx=max(mx,xx);
            }
            cout << "Case #"<<tt+1<<": "<< mx << endl;
        }
    }
    return 0;
}
