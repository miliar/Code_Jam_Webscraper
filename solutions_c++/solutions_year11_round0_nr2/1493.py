#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <map>
#include <vector>
using namespace std;

struct pp{
    char ch1, ch2, ch3;
    pp(){}
    pp(char _ch1, char _ch2, char _ch3):
            ch1(_ch1), ch2(_ch2), ch3(_ch3){}
}  que1[50];

struct qq{
    char ch1, ch2;
    qq(){}
    qq(char _ch1, char _ch2):
            ch1(_ch1), ch2(_ch2){}
}  que2[50];

char str[150];
int main()
{
    int cas;
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &cas);
    int T=0;
    while(cas--)
    {
       int c, d, n;
       char ch1, ch2, ch3;
       T++;
       char c1, c2;
       scanf("%d", &c);
       for(int i=0; i<c; ++i)
       {
         scanf(" %c %c %c", &ch1, &ch2, &ch3);
         que1[i] = pp(ch1, ch2, ch3);
       }
       scanf("%d", &d);
       for(int i=0; i<d; ++i)
       {
         scanf(" %c %c", &c1, &c2);
         que2[i] = qq(c1, c2);
       }
       scanf("%d", &n);
       for(int i=0; i<n; ++i)
       {
          scanf(" %c", &str[i]);
       }
       str[n] = '\0';
       
       string ss="";
       ss += str[0];
       for(int i=1; i<n; ++i)
       {
          ss += str[i];
          bool flag = false;
          int len = ss.length();
          for(int i=0; i<c; ++i)
          {
              if(ss[len-1]==que1[i].ch1 && ss[len-2]==que1[i].ch2 ||
                  ss[len-1]==que1[i].ch2 && ss[len-2]==que1[i].ch1)
              {
                 ss = ss.substr(0, len-2)+que1[i].ch3;
                 flag = true;
                 break;
              }
          }
          for(int i=0; i<d; ++i)
          {
              if(flag)
                 break;
              if(ss[len-1]==que2[i].ch1 && ss.rfind(que2[i].ch2)!=string::npos)
              {
                 int tmp=ss.rfind(que2[i].ch2);
                // clog << tmp <<" kirk\n";
                 //if(ss.rfind(que2[i].ch2)==0)
                    ss.clear();
                // else
                //    ss = ss.substr(0,tmp);
                 break;
              }
              if(ss[len-1]==que2[i].ch2 && ss.rfind(que2[i].ch1)!=string::npos)
              {
                 //clog << ss.rfind(que2[i].ch1) <<" 22kirk\n";
                // int tmp=ss.rfind(que2[i].ch1);
                // if(ss.rfind(que2[i].ch1)==0)
                    ss.clear();
                // else
                //    ss = ss.substr(0,tmp);
                 break;
              }
             // clog<<endl<<ss<<endl;
          }
       }
       printf("Case #%d: ", T);
       if(ss=="")
       {
          cout<<"[]"<<endl;
          continue;
       }
       cout<<"["<<ss[0];
       for(int i=1; i<ss.length(); ++i)
       {
           cout<<", "<<ss[i];
       }
       cout<<"]\n";
            
    }
   // while(1);
    return 0;
} 
/*
1 EWV 1 AD 10 RDSFFWRAEW
*/
