#pragma comment(linker, "/STACK:16777216")
#include <algorithm> 
#include <cctype> 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 
#include <cstring> 
#include <deque> 
#include <iostream> 
#include <list> 
#include <map> 
#include <numeric> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <string> 
#include <vector> 

using namespace std; 

template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }

#define clr(a) memset(a,0,sizeof(a))
#define pb push_back
#define sz size()  
#define ld long double
#define ll long long
#define mp make_pair
#define istr istringstream

int t,n,As[120],Bs[120],x,A,B,k,kk;
char Cs[120],c;

void moveA()
{
    if (k && As[k-1]>A) A++;
    if (k && As[k-1]<A) A--;    
}

void moveB()
{
    if (kk && Bs[kk-1]>B) B++;
    if (kk && Bs[kk-1]<B) B--;    
}

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    cin>>t;
    for(int T=0;T<t;T++)
    {
        cin>>n;
        A=1;
        B=1;
        k=0;
        kk=0;
        int tm=0;
        for(int i=0;i<n;i++)
        {
            cin>>c>>x;
            if (c=='B') As[k++]=x; else Bs[kk++]=x;
            Cs[i]=c;
        }
        reverse(As,As+k);
        reverse(Bs,Bs+kk);
        
/*        for(int i=0;i<k;i++)
        cout<<As[i]<<" ";
        cout<<endl;
        for(int i=0;i<kk;i++)
        cout<<Bs[i]<<" ";
        cout<<endl;        */
        
        for(int i=0;i<n;i++)
        {
            while(true)
            {
//                cout<<i<<"   "<<Cs[i]<<" "<<A<<" "<<B<<endl;
                tm++;
                if (Cs[i]=='B' && As[k-1]==A)
                {
                    moveB();
                    k--;
                    break;
                }
                if (Cs[i]=='O' && Bs[kk-1]==B)
                {
                    moveA();
                    kk--;
                    break;
                }                
                moveA();
                moveB();
            }
        }
        cout<<"Case #"<<T+1<<": "<<tm<<endl;
    }
    
    return 0;
}
