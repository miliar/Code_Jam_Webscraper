#include<iostream>
#include<sstream>
#include<vector>
#include<string>
#include<map>

#define PB push_back
#define MP make_pair


using namespace std;

string i2s(long long x) { ostringstream o; o<<x; return o.str(); }
long long s2i(string s) { istringstream i(s); long long x; i>>x; return x; } 

string s;
vector<char> a;

void solve()
{
     int i,j,k;
     getline(cin,s);
     a.clear();
     for (i=0; i<s.size(); i++) a.PB(s[i]);
     
     if (next_permutation( a.begin(), a.end() ) )
     {
         for (i=0; i<a.size(); i++) cout<<a[i];
         cout<<endl;
         return; 
     }
     
     a.PB('0');     
     sort(a.begin(), a.end());
     for (i=0; i<a.size(); i++) 
       if (a[i]!='0')
       {
            cout<<a[i];
            for (j=0; j<i; j++) cout<<a[j];
            for (j=i+1; j<a.size(); j++) cout<<a[j];
            cout<<endl;
            return;
       }
     
     
}


#include<conio.h>
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("t.out","w",stdout);
    
    int num,z;
    getline(cin,s);
    num = s2i(s);
    
    
    for (z=1; z<=num; z++)
    {
        cout<<"Case #"<<z<<": ";
        solve();
    }
    
    
    fclose(stdin);
//    fclose(stdout);    
    getch();
    
    return 0;
}
