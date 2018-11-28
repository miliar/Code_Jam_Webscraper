#include <iostream>
#include <algorithm>
#include <string>
#include <stack>
#include <deque>
#include <cstring>
#include <cstdio>
#include <vector>
 
using namespace std;
 
 
int main()
{
        freopen("A-small-attempt0.in","r",stdin);
        freopen("output.txt","w",stdout);
 
        int t,q=0;
 
cin>>t;
int qq[26]={25,8,5,19,15,3,22,24,4,21,9,7,12,2,11,18,26,20,14,23,10,16,6,13,1,17};
while(t--)
{
 char a[102],b[102];
gets(a);int m=0;
while(a[m]!='\0')
{
if(a[m]!=' '){int w=a[m]-'a';
 char c='a'-1+qq[w];
b[m]=c;}
else
b[m]=a[m];
m++;
}
b[m]='\0';
                cout<<"Case #"<<q+1<<": "<<b<<endl; 
q++;        }
return 0;
};