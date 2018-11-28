#include<iostream>
#include<map>
#include<algorithm>
#include<string>
#include<cstdio>
using namespace std;
int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    char convert[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    int T,c=1;
    scanf("%d\n",&T);
    while(T--){
        string s;
        getline(cin,s);
        int i,l;
        cout << "Case #"<<c<<": ";
        c++;
        for(i=0;i<s.size();i++){
            if(s[i]>='a' && s[i]<='z') cout << convert[s[i]-'a'];
            else cout << s[i];
        }
        cout << endl;
    }
    return 0;
}
