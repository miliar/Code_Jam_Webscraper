#include<iostream>
using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    char arr[26]= {'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};
    char arr1[26];
    for (int j=0;j<26;j++)
        arr1[arr[j]-'a']=  j +'a';
    int N,cases=0;
    cin>>N;
    string str="";
    getline(cin,str);
    while(N--)
    {
              cases++;
              getline(cin,str);
              for(int i=0;i<str.length();i++)
              {
                      if(str[i] != ' ')
                      str[i]=arr1[ str[i]- 'a' ];
              }
              cout<<"Case #"<<cases<<": "<<str<<"\n";
              str="";
    }
}
