#include<iostream>
#include<map>
#include<algorithm>
#include<string>
#include<cstdio>
using namespace std;
string convert(int N){
    string s="";
    while(N>0){
        s = s + char((N%10)+'0');
        N/=10;
    }
    reverse(s.begin(), s.end());
    return s;
}
int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T,c=1;
    cin >> T;
    while(T--){
        int a,b,i,j,co=0;
        string s1="",s2="";
        cin >> a >> b;
        cout << "Case #"<<c<<": ";
        c++;
        for(i=a;i<=b;i++){
            s1 = convert(i);
            s1 = s1 + s1;
            for(j=a;j<i;j++){
                s2 = convert(j);
                int found=s1.find(s2);
                if(found!=string::npos) co++;
            }
        }
        cout << co << endl;
    }
    return 0;
}
