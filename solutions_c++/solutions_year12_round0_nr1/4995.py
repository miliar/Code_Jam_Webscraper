#include<iostream>
#include<string>
#include<cstdio>
using namespace std;

char T[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};



int main()
{
   int Z;
   scanf("%d\n",&Z);
   for(int z=1;z<=Z;z++)
   {
      string S;
      getline(cin,S);
      for(int i=0;i<S.size();i++){(S[i]!=' ')?S[i]=T[S[i]-'a']:S[i]=S[i];}
      cout<<"Case #"<<z<<": "<<S<<endl;
   }
   return 0;
}
