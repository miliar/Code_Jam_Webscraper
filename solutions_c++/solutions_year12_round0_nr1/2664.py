/*
ID:   cs_diab1
TASK: 
LANG: C++
*/

#include<algorithm>
#include<iostream>
#include<iomanip>
#include<cstring>
#include<cstdlib>
#include<sstream>
#include<vector>
#include<cstdio>
#include<string>
#include<cmath>
#include<queue>
#include<set>

#define stop exit(0)
#define nc -1
#define eps 1e-10
#define inf 1000000000
#define mp make_pair

#define fill(array,value) memset(array,value,sizeof(array))
#define f(i,beg,end) for(int i=beg; i<=end; i++)
#define F(i,beg,end) for(int i=beg; i>=end; i--)
#define Max(a,b) ( (a>b)?a:b )
#define Min(a,b) ( (a<b)?a:b )
#define pi 3.1415926535897932384626433832
#define iread(var) scanf("%d",&var)
#define dread(var) scanf("%f",&var)
#define lread(var) scanf("%lld",&var)
#define input(name) freopen(name,"r",stdin)
#define output(name) freopen(name,"w",stdout)
typedef unsigned long long ull;
typedef unsigned int ui;
typedef long double ld;
typedef long long ll;

using namespace std;

const char t[]="yhesocvxduiglbkrztnwjpfmaq";
char text[1010];
int tt;

void init()
{
    cin>>tt; cin.ignore();
    
    f(i,1,tt)
    {
        cin.getline(text,1010);
        cout<<"Case #"<<i<<": ";
        f(i,0,strlen(text)-1)
            if (text[i]!=' ') cout<<t[text[i]-'a'];
            else cout<<" ";
        cout<<endl;
    }
}

int main()
{
    //redirect();
    input("a.txt");
    output("sol.txt");
    init();

    return 0;
}