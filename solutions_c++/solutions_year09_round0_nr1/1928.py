#include<iostream>
#include<string>

using namespace std;
long l,d,n,ans;
string str[5000],s;
char ch[20][20];
bool v[20][30];
bool flag;

int main() {
    cin >> l >> d >> n;
    for (int i=0;i<d;i++) {
        cin >> str[i];
    }
    for (int i=0;i<n;i++) {
        cin >> s;
        memset(v,false,sizeof(v));
        bool flag=false;
        long counter=0;
        for (int j=0;j<s.length();j++) {
            if (s[j]=='(') {flag=true;}
            else if (s[j]==')') {flag=false;counter++;}
            else {
                 v[counter][s[j]-'a']=true;
                 if (!flag) {counter++;}
            }
        }
        ans=0;        
        for (int j=0;j<d;j++) {
            bool f=true;
            for (int k=0;k<l;k++) {
                if (!v[k][str[j][k]-'a']) {f=false;}
            }
            if (f) {ans++;}
        }
        cout << "Case #" << i+1 << ": " << ans << endl;
    }
    //system("pause");
    return 0;    
}
