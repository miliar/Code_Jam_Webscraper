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
        freopen("outpu.txt","w",stdout);
 
        int cas;
cin>>cas;
int in[26]={25,8,5,19,15,3,22,24,4,21,9,7,12,2,11,18,26,20,14,23,10,16,6,13,1,17};
for(int num=1;num<=cas;num++)
{
 char or[102];
gets(or);int ind;
for(ind =0;or[ind]!='\0';ind++)
if(or[ind]!=' ')
or[ind]='a'-1+in[or[ind]-'a'];
                cout<<"Case #"<<num<<": "<<or<<endl; 
}
return 0;
};