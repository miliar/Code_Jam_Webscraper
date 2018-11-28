////anmolkapooor

#include <cmath>
#include <cstdio>
#include <cctype>
#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;
#define GI ({int _t; scanf("%d", &_t); _t;})
#define FOR(i, a, b) for (int i=a; i<b; i++)
#define REP(i, a) FOR(i, 0, a)
#define sz size()
#define pb push_back
#define cs c_str()
#define DBGV(_v) { REP(_i, _v.sz) { cout << _v[_i] << "\t";} cout << endl;}
#define tr(container, it) \
for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
typedef long long lld;

int main()
{
    
    string input,output;
    int n=3;
    cin>>n;
    getchar();
    char c[]={"yhesocvxduiglbkrztnwjpfmaq"};
    
    int i=1;
    while(n--)
    {
        
         getline(cin,input);
         cout<<"Case #"<<i<<": ";
         i++;
         for(int i=0;i<input.size();i++)
         {
             if(input[i]==' ') {cout<<' '; continue;}
           //  cout<<input[i]-'a'<<" ";
             
             cout<<c[(int)input[i]-'a'];
            // cout<<endl;
               
         
         }
         cout<<endl;
    }  

  //system("pause"); /// for output .. delete pls...
    return 0;
}
