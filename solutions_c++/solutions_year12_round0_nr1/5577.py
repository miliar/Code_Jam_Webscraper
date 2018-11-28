#include <iostream>

using namespace std;

char a[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main()
{
    int n;
    char x;
    string s;
    cin>>n;
    int c=1;
    getline(cin,s);
    while(n--){
        getline(cin,s);
        cout<<"Case #"<<c<<": ";
        for(int i=0;i<s.length();i++){
            if(s[i]==' ') cout<<' ';
            else cout<<a[int(s[i])-'a'];
        }
        cout<<endl;
        c++;
    }
    return 0;
}
