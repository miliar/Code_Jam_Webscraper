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

int can[2][101], d[1100], n, s, t, p, g;

void init()
{
    iread(t);
    
    f(ii,1,t)
    {
        fill(can,0);
        iread(n); iread(s); iread(p);
        f(i,1,n) 
        {
            iread(g); d[i]=g;
            
            //if (g/3 + (g%3>0)>10) continue;
            //if (g/3+(g%3>0)>10) continue;
            if (g>30) continue;
            
            if ((g/3>=p && g%3==0) || (g/3+1>=p && g%3>0)) {  can[0][i]=1 ; continue; }
            
            switch (g%3)
                {
                    case 0:
                        if (g/3+1>=p && (g/3-1>0))  can[1][i]=1;
                        break;
                    case 1:
                        if (g/3+1>=p && g/3+1<11) can[1][i]=1;
                        break;
                    case 2:
                        if (g/3+2>=p && g/3+2<11) can[1][i]=1;
                        break;
                }
        }
        
        int sol=0, left=s;
        f(i,1,n)
            if (can[0][i]) sol++;
            else if(can[1][i] && left>0) { sol++; left--; }
        
      //  cout<<n<<" "<<s<<" "<<p<<" ";
        //f(i,1,n) cout<<d[i]<<" ";
        cout<<"Case #"<<ii<<": "<<sol<<endl;
    }
}

int main()
{
    //redirect();
    input("b.in");
    output("solution.txt");
    init();

    return 0;
}