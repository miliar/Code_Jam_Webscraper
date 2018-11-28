#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
#include <set>

#define For(i,n) for(int i = 0;i<n;i++)
#define Fors(var,start,finish) for(int var = start, var <=finish, var++)

using namespace std;

const int maxn = 1000;
int t,a,b;

int small(){
    int res = 0;
    ostringstream oa;
    oa << a;
    ostringstream ob;
    ob << b;
    
    string astr = oa.str();
    string bstr = ob.str();
    
    for(int i = a;i<b;i++){
        ostringstream o;
        o<<i;
        string n = o.str();
     //  cout<<"CHECKING: "<<n<<endl;
        string m = n;
        int l = n.size();
        For(i,l){
            if (i==0) continue;
            For(j,l){
                m[j] = n[(j+i)%l];
            }
          //  cout<<m<<endl;
            if (m[0] != '0' && m > n && m <= bstr){
                res++;
          //      cout<<res<<": ";
           //     cout<<n<<" "<<m<<endl;

            }
        }
    }
    return res;
}

int main(){
    cin>>t;
    For(i,t){
        cin>>a>>b;
        cout<<"Case #"<<i+1<<": "<<small()<<endl;
    }
}
