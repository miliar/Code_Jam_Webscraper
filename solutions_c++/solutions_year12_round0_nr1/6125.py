#include<iostream>
#include<string>
using namespace std;
char Google[27] = "yhesocvxduiglbkrztnwjpfmaq";

int main()
    {
          int i,j,t;
          char ch[201];
         freopen("A.in","rt",stdin);
          freopen("A.out","wt",stdout);
          cin >> t;
          cin.getline(ch,201);
          for(j=0;j<t;j++){
                     char out[201];
                     cin.getline(ch,201);
                     for(i=0;ch[i]!='\0';i++){
                                         if(isspace(ch[i]))
                                                        out[i] = ch[i];
                                         else
                                             out[i]=Google[ch[i]-'a'];
                                         }
                     out[i] ='\0';
                     cout<<"Case #"<<j+1<<": "<<out<<endl;
                     }
          return 0;
    }