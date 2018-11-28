#include<iostream>
using namespace std;

int n;
string str;
int a[200];
char ch[100];
long long counter;

int main() {
    cin >> n;
    for (int i=0;i<n;i++) {
        cin >> str;
        counter=0;
        memset(a,0,sizeof(a));
        a[str[0]-'0']++;
        ch[1]=str[0];
        for (int j=1;j<str.length();j++) {
            if (a[str[j]-'0']==0) {
               a[str[j]-'0']++;                                  
               ch[counter]=str[j];
               if (counter==0) {counter=2;}
               else {counter++;};
            }
        }
        long long ans,temp;
        temp=1;
        ans=0;
        if (counter==0) {counter=2;};
        for (int j=str.length()-1;j>=0;j--) {
            for (int k=0;k<counter;k++) {
                if (ch[k]==str[j]) {
                   long long digit=k;
                   ans+=digit*temp;
                }
            }
            temp*=counter;
        }
        cout << "Case #" << i+1 << ": " << ans << endl;
    }
    return 0;
}
