#include<iostream>
using namespace std;
#include<cstring>

int main(){
    int t,k=1;cin>>t;
    char ch;while((ch=getchar())!='\n') ;
    while(t--){
               string s;
               getline(cin,s);
               char aa[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
               for(int i=0;i<s.size();i++)
               {if(s[i]==' ') ;
               else s[i]=aa[s[i]-'a'];
                  }
                  cout<<"Case #"<<k<<": ";
               cout<<s<<endl;k++;
               }
               //system("pause");
    return 0;
}
