using namespace std;
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>

int main()
{
      int t, testcase=0;
      string str;
      scanf("%d\n",&t);
      while(t--)
      {
              testcase++;
              char s[]="yhesocvxduiglbkrztnwjpfmaq";  
              string message="";
              getline(cin, str);
              int leng=str.length();
              
              for(int i=0;i<leng;i++) 
              {
                 if(str[i]==' ') 
                     message.append(1,' ');
                 else 
                     message.append(1,s[str[i]-'a']);
              }
                 
              cout<<"Case #"<<testcase<<": "<<message<<endl;
              
      }
      return 0;
}
