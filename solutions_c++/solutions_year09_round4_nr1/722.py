#include<iostream>
#include<sstream>
#include<vector>
#include<string>
#include<map>
#include<conio.h>

#define PB push_back
#define MP make_pair


using namespace std;

string i2s(long long x) { ostringstream o; o<<x; return o.str(); }
long long s2i(string s) { istringstream i(s); long long x; i>>x; return x; } 

int n;
string a[100+15];

void initialize()
{
     cin>>n;
     for (int i=0; i<n; i++) cin>>a[i];
}

bool check(int i, int s) // check row i
{
     for (int j=s+1; j<n; j++)
       if (a[i][j]=='1') 
         return 0;
     return 1;
}

void solve()
{
     int i,j,k;
     int r=0;
     
     for (i=0; i<n; i++)
       if (!check(i,i))
       {
           for (j=i+1; j<n; j++)
             if (check(j,i))
             {
                 for (k=j; k-1>=i; k--)
                 { swap(a[k],a[k-1]); r++; }
                 break;
             }
       }
     
     
     
     cout<<r<<endl;  
}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("t.out","w",stdout);
    
    int num;
    cin>>num;
    for (int z=1; z<=num; z++)
    {
       cout<<"Case #"<<z<<": "; 
       initialize();
       solve();
    }
    
    
    fclose(stdin);
    fclose(stdout);    
    getch();
    
    return 0;
}
