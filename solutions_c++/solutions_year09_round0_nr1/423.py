#include<iostream>
#include<sstream>
#include<vector>
#include<string>
#include<map>
#define PB push_back

using namespace std;

string i2s(long long x) { ostringstream o; o<<x; return o.str(); }
long long s2i(string s) { istringstream i(s); long long x; i>>x; return x; } 

int l,d,n;
vector<string> W, T;

void initialize()
{
     char x[1000+15];
     string temp;
     
     cin.getline(x,1000,'\n');
     temp = x;
     istringstream ii(x);
     ii>>l>>d>>n;
     
     for (int i=0; i<d; i++)
     {
         cin.getline(x,1000,'\n');
         temp = x;
         W.PB(temp);
     }
         
     
     for (int i=0; i<n; i++)
     {
         cin.getline(x,1000,'\n');
         temp = x;
         T.PB(temp);
     }         
     
}


void solve()
{
     int i,j,k,q;
     string temp;
     
     for (i=0; i<n; i++)
     {
         string s = T[i];
         
         bool mark[l+15][26+15];
         memset(mark,0,sizeof(mark));
                  
         k=0;
         for (j=0; j<l; j++)              // mark s
         {
             string temp="";
             if (s[k]=='(')
             {
                 k++;
                 while (s[k]!=')') { temp+=s[k]; k++; }
                 k++;
             }
             else { temp += s[k]; k++; } 

             for (q=0; q<temp.size(); q++)
               mark[j][ temp[q]-'a' ] = 1;
         }                 
         


         
         int cnt=0;
         for (j=0; j<d; j++) // check word j
         {
             bool f=true;
             for (k=0; k<l; k++)
               if (!mark[ k ][ W[j][k]-'a' ])
               { f=false; break; }
             if (f) cnt++;
         }
           
           
         cout<<"Case #"<<i+1<<": "<<cnt<<endl;         
     }
     
     
     
}





#include<conio.h>
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("t.out","w",stdout);
    
    initialize();
    solve();
    
    
    fclose(stdin);
    fclose(stdout);    
//    getch();
    
    return 0;
}
