#include <iostream>
#include <map>
#include <string>
using namespace std;
int l,d,n;
string b[20];
string pk;
map<string,bool> a;
int ans;
void recur(int p){
     if (p==l){
 //        cout << pk <<endl;
         if (a.find(pk)!=a.end())
             ++ans;
     }else{
     for (unsigned i = 0; i < b[p].length(); ++i){
         pk[p] = b[p][i];
         if (a.find(pk.substr(0,p+1))!=a.end())
             recur(p+1);
     }
     }
}
int main(){
    cin >> l >> d >> n;

    string s;
    for (int i = 0; i < d; ++i){
        cin >> s;
        a[s] = true;
  //      cout << s <<endl;
        for (int i = 1; i < l; ++i){
            a[s.substr(0,i)] = true;
        //    cout << s.substr(0,i) << endl;
        }
    }
    int cas = 0;
    while (n--){
        ++cas;
        string x;
        cin >> x;
//        cout << x <<endl;
        int ll = 0;
        for (int k = 0; k < l; ++k){
            b[k]="";
            if (x[ll]=='('){
                ++ll;
                while (x[ll]!=')'){
                    b[k]+=x[ll];
                    ++ll;
                }
            } else{
               b[k] = x[ll];
            }
            ++ll;
         //   cout << b[k] << endl;
        }
        pk=s;
        ans = 0;
        recur(0);
        cout << "Case #" << cas << ": "<< ans <<endl;
    }
}
