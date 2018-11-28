#include <iostream>
#include <cstdio>
#include <cmath>
#include <sstream>
#include <algorithm>

using namespace std;

string rot(string s)
{
    string r="";
    r+=s[s.size()-1];
    for(int i=0; i<s.size()-1; i++) {
        r+=s[i];
    }    
    return r;
}

string i2s(int n)
{
    string s;
    stringstream str;
    str << n;
    str >> s;
    return s;
}

int s2i(string s)
{
    int n;
    stringstream str;
    str << s;
    str >> n;
    return n;
}

int main()
{
    bool flag[2000001];
    int T,A,B;
    cin >> T;
    for(int t=1; t<=T; t++) {
        cin >> A >> B;
        for(int i=A; i<=B; i++) {
            flag[i]=1;
        }
        
        int ans=0;
        
        for(int i=A; i<=B; i++) {
            string p=i2s(i);
            string n=rot(p);
            int ctr=0;
            while(n!=p) {                
                int x=s2i(n);
                if(n[0]!='0' && x>i && x<=B) {
                    int k=s2i(n);
                    ctr++;
                }
                n=rot(n);
            }
            ans+=ctr;
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}
