#include "iostream"
#include "string"

using namespace std;


int T , C , D, N;
char a , b , c;
char com[1000][1000];
bool clr[1000][1000];

void solve()
{
     string str;
     char ch1 , ch2;
     cin >> N;
     for(int i  = 0 ; i < N ;i++)
     {
          cin >> ch1;
          str += ch1;
          int t = str.size() - 1; 
        
          if(t <= 0)
          {
              continue;
          }
          if(com[str[t]][str[t - 1]] != '#')
          {
                     
               ch2  =  com[str[t]][str[t - 1]];         
             
               str.erase(str.end() - 2 , str.end());
               str += ch2;
          }
          else
          {
               for(int j = 0 ; j < t ; j++)
               {
                   if(clr[str[j]][str[t]] == true)
                   {
                       str.clear();
                       break;             
                   }   
               }
          }
        
     }
     int len = str.size();
     cout << "[";
     for(int i = 0 ; i < len - 1 ;i++)
     {  
         cout << str[i] <<", ";
     }
     if(len >=1)
        cout << str[len - 1];
     cout <<"]"<<endl;
   
}

void init()
{
     for(int i = 0 ; i < 1000 ;i++)
     {
         for(int j = 0 ; j < 1000; j++)
         {
             com[i][j] = '#';
             clr[i][j] = false;    
         }
     }
}

int  main()
{
    //  freopen("data_in.txt","r",stdin);
     freopen("B-large.in","r",stdin);
     freopen("B-large.out","w",stdout);
     
     cin >> T;
     for(int t = 1 ; t <= T ;t++)
     {
        init();     
        cin >> C;
        for(int i = 0 ; i < C ;i++)
        {
            cin >> a>> b >> c;
            com[a][b] = c;
            com[b][a] = c;  
               
        }
        cin >> D;
        for(int i = 0 ; i < D ;i++)
        {
           cin >> a >> b;
           clr[a][b] = true;
           clr[b][a] = true;
        }
        cout <<"Case #"<<t<<": ";
        solve();
     }
     //while(1);
     return 0;
}
