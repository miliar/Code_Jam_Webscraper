#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;
char ans[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main()
{
    int t;
    cin>>t;
    getchar();
    int cases=0;
    while(t--)
    {
              
              char ar[110];
              
              cin.getline(ar,110);
              //cout<<ar;
              int i;
              cout<<"Case #"<<++cases<<": ";
              for(i=0;ar[i]!='\0';i++)
              {
                                      if(ar[i]!=' ')
                                      cout<<ans[ar[i]-97];
                                      else
                                      cout<<" ";
              
              }
              cout<<endl;
}
}
