#include <iostream>
#include <cstring>
using namespace std;
int cnt[10];
string s,st;

string them0(void) {
       st="";
       int i;
       for (i=1;i<=9;i++) if (cnt[i]>0) {
           cnt[i]--;
           st.push_back(char(i+48));
           break;
       };
       st.push_back('0');
       for (i=0;i<=9;i++)
           while (cnt[i]>0)
                 {st.push_back(char(i+48)); cnt[i]--;};
       return st;
};

string xuli(void) {
    int i,n;
    memset(cnt,0,sizeof(cnt));
    n=s.length();
    int check=0;
    for (i=0;i<n;i++) {
        cnt[int(s[i])-int('0')]++;
        if (i==1) {
           if ((s[i]!='0')&&(s[i]>s[i-1])) check=i;
        }
        else
        if ((i!=0)&&(s[i]>s[i-1])) check=i;
    };
    if (check==0) return them0();
    char tam;
    int ch,j;
    ch=n-1;
    memset(cnt,0,sizeof(cnt));
    cnt[int(s[n-1])-48]++;
    for (i=n-2;i>=0;i--) {
        ch=0;
        cnt[int(s[i])-48]++;
        for (j=i+1;j<n;j++) {
            if (s[j]<=s[i]) continue;
            if ((ch==0)||(s[j]<s[ch])) ch=j;
        };
        if (ch!=0) {
           cnt[int(s[ch])-48]--;
           tam=s[ch];
           s[ch]=s[i];
           s[i]=tam;
           s.erase(i+1,s.length());
           for (j=0;j<=9;j++)
               while (cnt[j]>0) 
                     { s.push_back(char(j+48)); cnt[j]--;};
           break;
        };
    };
    return s;
};

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,i;
    scanf("%d\n",&t);
    string st;
    for (i=1;i<=t;i++) {
        getline(cin,s);
        st=xuli();
        cout<<"Case #"<<i<<": "<<st<<endl;
    };
    return 0;
};
