#include<iostream>

using namespace std;



int main()
{
    char ch1[102],ch[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    int c,i,a;
    char cs;
    
    cin>>c;
    gets(ch1);
    for(i=1;i<=c;i++)
    {
                     gets(ch1);
                    // cout<<ch1;
                     cout<<"Case #"<<i<<": ";
                     int j;
                     for(j=0;ch1[j]!='\0';j++)
                     {
                                              if(ch1[j]!=' ')
                                              {
                                                           a=ch1[j]-'a';
                                                           cout<<ch[a];
                                              }
                                              else cout<<ch1[j];
                     }
                     cout<<endl;
    }
}
