#include<iostream>
#include<sstream>
#include<vector>
#include<string>
#include<map>

using namespace std;

string i2s(long long x) { ostringstream o; o<<x; return o.str(); }
long long s2i(string s) { istringstream i(s); long long x; i>>x; return x; } 

char x[1000+15];
string s1;
string s2 = "welcome to code jam";

int F[500+15][21+15];


void initialize()
{
    cin.getline(x,1000,'\n');
    s1 = x; 
}

int go(int i, int j)
{
    if (i<j) return 0;
    if (j==0) return 1;
    if (F[i][j]!=-1) return F[i][j];
    
    int r = go(i-1,j);
    if ( s1[i-1] == s2[j-1] ) r = (r+go(i-1,j-1))%10000;
    
    return F[i][j] = r;
}

void solve()
{
    int i,j,k;
    memset(F,-1,sizeof(F));
    string r = i2s(go(s1.size(), s2.size()));
    while (r.size()<4) r= "0"+r;
    cout<<r<<endl;
}


#include<conio.h>
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("t.out","w",stdout);
    
    int num,z;
    cin.getline(x,1000,'\n');
    string temp = x;
    istringstream ii(x);
    ii>>num;
    
    for (z=0; z<num; z++)
    {
        cout<<"Case #"<<z+1<<": ";
        initialize();
        solve();
    }
    
    
    fclose(stdin);
    fclose(stdout);    
//    getch();
    
    return 0;
}
