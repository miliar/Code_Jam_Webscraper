#include <iostream>
#include <cstdio>
#include <map>
#include <cstring>
#include <string>

using namespace std;

int  main(){
     string str[3],str1[3];
     str[0]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
     str[1]="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
     str[2]="de kr kd eoya kw aej tysr re ujdr lkgc jv";
     str1[0]="our language is impossible to understand";
     str1[1]="there are twenty six factorial possibilities";
     str1[2]="so it is okay if you want to just give up";
     map <char,char> mymap;
     int c=3;
     while(c>0){
                      for(int i=0;i<str[c-1].size();++i){
                              mymap[str[c-1][i]]=str1[c-1][i];
                              }
                      c--;
              }
     mymap['q']='z';
     mymap['z']='q';
     
     /*map <char,char>::iterator it;
     it=mymap.begin();
     while(it!=mymap.end()){
                            cout<<(*it).first<<" "<<(*it).second<<endl;
                            it++;
                            }*/
    
     int t;
     scanf("%d",&t);
     char s[101];
     getchar();
     for(int i=1;i<=t;++i){
             gets(s);
             printf("Case #%d: ",i);
             for(int j=0;j<strlen(s);++j){
                     cout<<mymap[s[j]];
                     }
             printf("\n");
             }               
             
     //system("pause");
     return 0;
     }
     
                      
                      
