#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <cmath>
using namespace std;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef long long LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for (int i=0; i<n; ++i)
#define FOR(var,pocz,koniec) for (int var=pocz; var<=koniec; ++var)
#define FORD(var,pocz,koniec) for (int var=pocz; var>=koniec; --var)
#define FOREACH(it, X) for(__typeof(X.begin()) it = X.begin(); it != X.end(); ++it)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define SIZE(x) (int)x.size()

#define AND &&
#define OR ||

/****** Big Number Multiplication *********************/
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#define MAX 1000
/******************************************************************/
void reverse(char *from, char *to ){
int len=strlen(from);
int l;
for(l=0;l<len;l++)
to[l]=from[len-l-1];
to[len]='\0';
}
/******************************************************************/
void call_mult(char *first,char *sec,char *result){
char F[MAX],S[MAX],temp[MAX];
int f_len,s_len,f,s,r,t_len,hold,res;
f_len=strlen(first);
s_len=strlen(sec);
reverse(first,F);
reverse(sec,S);
t_len=f_len+s_len;
r=-1;
for(f=0;f<=t_len;f++)
temp[f]='0';
temp[f]='\0';
for(s=0;s<s_len;s++){
hold=0;
for(f=0;f<f_len;f++){
res=(F[f]-'0')*(S[s]-'0') + hold+(temp[f+s]-'0');
temp[f+s]=res%10+'0';
hold=res/10;
if(f+s>r) r=f+s;
}
while(hold!=0){
res=hold+temp[f+s]-'0';
hold=res/10;
temp[f+s]=res%10+'0';
if(r<f+s) r=f+s;
f++;
}
}
for(;r>0 && temp[r]=='0';r--);
temp[r+1]='\0';
reverse(temp,result);
}





int main()
{
    LL T;
    LL counter = 0;
    long long ans;
    long double n;
    cin>>T;
    string number = "52360679774997896964091736687313";
    char *numberC;
    strcpy (numberC, number.c_str());
    
    
    while(T--)
    {
              counter++;
              
              cin>>n;
              LL dec = 31*n;
              char res[MAX] = "1";
              while(n--)
              call_mult(numberC,res,res);
              
              //cout<<res<<endl;
              
              LL len = strlen(res);
              cout<<"Case #"<<counter<<": ";
              int(res[len-dec-3])==0?cout<<"0":cout<<res[len-dec-3];//
                            int(res[len-dec-2])==0?cout<<"0":cout<<res[len-dec-2];
                                          int(res[len-dec-1])==0?cout<<"0":cout<<res[len-dec-1];
              cout<<endl;
              /*
                REP(i,3)
                func(res[len-dec-(i+1)]);
              */          
    }
                  //system("pause");
    
}

