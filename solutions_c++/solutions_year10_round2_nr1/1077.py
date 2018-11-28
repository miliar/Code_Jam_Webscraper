#include "iostream"
#include "string"
#include "map"

using namespace std;
map<string , bool> v; 
char str[1001];
string st;
int main()
{
     freopen("A-large.in","r",stdin);
     freopen("A-large.out","w",stdout);
     int test , N ,M;
     scanf("%d",&test);
     for(int t = 1 ; t <= test;t++)
     {
          int cunt = 0;
          v.clear();
          scanf("%d%d",&N,&M);
          v["/"] = true;
          for(int i = 0 ; i < N ;i++)
          {   
              st.clear();
              scanf("%s",str); 
              int len = strlen(str);
              str[len] = '/';
             
              for(int j = 0 ; j <= len ; j++)
              {
                 st += str[j];
                  //cout << st <<endl;
                 if(str[j] =='/')
                      v[st] = true;
              }
              //cout << endl;
          }
       //  cout << "**************"<<endl;
          for(int i = 0 ; i < M;i++)
          {  
              st.clear();
              scanf("%s",str);  
              int len = strlen(str);
              str[len] = '/';
             // cout << str <<endl;
            
              for(int j = 0 ; j <= len ; j++)
              {
                 st += str[j];
                // cout << st<<endl;
                 if(str[j] =='/')
                 {  
                     //cout << st <<endl;
                     if(v[st] == false)
                     {
                        cunt++;
                        v[st] = true;
                     }
                 }
              }
              //cout << cunt <<endl;
           }
           printf("Case #%d: %d\n" ,t ,cunt);    
     }
  //   while(1);
     return 0;
}          
