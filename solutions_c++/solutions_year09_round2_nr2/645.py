#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<queue>
#include<deque>
#include<set>
using namespace std;

//double PI =  3.14159265358979323846;
#define dd long double
#define ll long long
#define VI vector<int>
#define PI pair<int,int>
#define MP make_pair
#define PB push_back
#define VVI vector<VI >

int main() {
    int t;
    cin>>t;
    for (int tt=0;tt<t;tt++) {
        cout<<"Case #"<<tt+1<<": ";
        string s;
        cin>>s;        
        VI a=VI(s.size(),0);
        for (int i=0;i<s.size();i++) a[i]=s[i]-'0';
        
        if (next_permutation(a.begin(),a.end()))
         {
            for (int i=0;i<a.size();i++) cout<<a[i]; cout<<endl;
        } else {

            VI c;
            int nul=1;
            for (int i=0;i<a.size();i++) {
                if (a[i]==0) nul++;
                else c.PB(a[i]);
            }
            sort(c.begin(),c.end());
            cout<<c[0];for (int i=0;i<nul;i++) cout<<0;
            for (int i=1;i<c.size();i++) cout<<c[i];
            cout<<endl;
            
        }
    
    }

}
