#include<iostream>
#include<string>
#include<cstdio>
using namespace std;

int a[] = {'y','h','e','s','o','c','v',
           'x','d','u','i','g','l','b',
           'k','r','z','t','n','w',
           'j','p','f','m','a','q'};

int main() {
    //freopen("input.in","r",stdin);
    //freopen("output.txt","w",stdout);
    int num;
    string str;
    cin>>num;
    cin.ignore();
    for(int i = 1; i <= num; ++i) {
        str.clear();
        getline(cin,str);
        for(int j = 0; j != str.size(); ++j) {
            if(str[j] != ' ') {
                str[j]= a[str[j] - 'a'];
            }
        }
        printf("Case #%d: %s\n",i,str.c_str());
        //cout<<str<<endl;
    }
    
    return 0;
}
