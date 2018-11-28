#include<iostream>
#include<vector>
#include<string>

using namespace std;

int main() 
{
    freopen("A-large.in","r",stdin);
    freopen("a-large.out","w",stdout);
    int T;
    cin>>T;
    int Case=1;
    while(T--) {
        int n;
        cin>>n;
        string s;
        getline(cin, s);
        //getline(cin, s);
        //cout<<s<<endl;
        int lpo=1, lpb=1, cpo=1, cpb=1;
        int m=0,mo=0,mb=0,co=0,cb=0;
        int sz=s.size();
        int i=0;
        int sp=i+1;
        char lh='x';
        for(int j=0; j<n; ++j) {
            char c = s[sp];
            sp += 2;
            int bt = 0;
            while(s[sp] != ' ' && sp < sz) {
                bt = bt*10 + s[sp] - '0';
                sp++;
            }
            sp++;
            //cout<<c<<" "<<bt<<endl;
            if(c=='O') {
                if(lh=='O' || j==0) {
                    m = m + abs(bt - lpo) + 1;
                }
                else {
                    int temp = abs(bt - lpo);
                    co = m - mo;
                    temp = temp - co;
                    if(temp<0)
                        temp = 0;
                    m = m + 1 + temp;
                }
                lpo = bt;
                mo=m;
            }
            else {
                if(lh=='B' || j==0) {
                    m = m + abs(bt - lpb) + 1;
                }
                else {
                    int temp = abs(bt - lpb);
                    cb = m - mb;
                    temp = temp - cb;
                    if(temp<0)
                        temp = 0;
                    m = m + 1 + temp;
                }
                lpb = bt;
                mb=m;
            }
            lh = c;
        }
        cout<<"Case #"<<Case++<<": "<<m<<endl;
    }
    //while(true);
    return 0;
}
