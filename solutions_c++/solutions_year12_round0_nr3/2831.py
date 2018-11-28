/*
ID: mkagenius1
LANG: C++
TASK:
*/

#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<map>
#include<string.h>
#include<string>
#include<vector>
#include<math.h>
#include<set>
#include<queue>

using namespace std;
int b;
int getfront(int x){
    while(x >= 10) x/=10;
    return x;
}
int oneless(int a){
    int f = getfront(a);
    while(a){
        f*=10;
        a/=10;
    }
    return f/10;
}
int getcount(int a){
    if(a < 10) return 0;
    int copy_a = a;
    int copy_a_again = a;
    int zz = oneless(a)/getfront(a);
    int ret = 0;
    //copy_a/=10;
    set<pair<int, int> > vec;
    while(copy_a){
        //cout << oneless(a) << "----";
        a = (a-oneless(a))*10 + getfront(a);
        //cout << a << "\n";
        //system("pause");
        while(a < zz) a*=10;
        if(a > copy_a_again && a <= b){
            //cout << copy_a_again << " -- " << a << endl;
            vec.insert(make_pair(copy_a_again, a));
        }
        copy_a/=10;
    }
    //system("pause");
    return vec.size();
}
/* Main Code goes Here-after */
int main()
{
    int t; cin >> t;
    int kase = 0;
    while(t--){
        kase ++;
        
        int a; cin >> a >> b;
        int ans = 0;
        for(int i = a; i < b; i++){
            ans += getcount(i);
        }
        
        cout << "Case #" << kase <<": " << ans << endl;
    }
    return 0;
}
