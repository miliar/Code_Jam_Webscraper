#include  <stdio.h>
#include <string.h>
#include   <math.h>

#include    <queue>
#include <iostream>
#include   <vector>
#include<algorithm>
#include      <map>
#include  <sstream>

using namespace std;

template<class T1> void deb(T1 e){cout<<e<<endl;}
template<class T1,class T2> void deb(T1 e1,T2 e2){cout<<e1<<" "<<e2<<endl;}
template<class T1,class T2,class T3> void deb(T1 e1,T2 e2,T3 e3){cout<<e1<<" "<<e2<<" "<<e3<<endl;}
template<class T1,class T2,class T3,class T4> void deb(T1 e1,T2 e2,T3 e3,T4 e4){cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<endl;}
template<class T1,class T2,class T3,class T4,class T5> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5)
{cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<endl;}
template<class T1,class T2,class T3,class T4,class T5,class T6> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5,T6 e6)
{cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<" "<<e6<<endl;}
template<class T> T f_min(T a , T b){if(a > b ) return b ;else return a;}
template<class T> T f_max(T a , T b){if(a > b ) return a ;else return b;}

#define mem(a,b) memset(a , b , sizeof (a))
#define lol long long
#define sz(a) (int)a.size()
#define llsz(a) (long long)a.size()
#define pb(a,b) a.push_back(b)
#define SZ 100000
#define c_sq(a) (int)sqrt(a)
#define llsq(a) (long long)sqrt(a)
#define cl(a) a.clear()
#define I_SZ 1000000000000ll
#define M 1000000007
#define fr first
#define sc second
#define iter(a,b) for (b=a.begin();b!=a.end();b++)
#define PI 2.0*acos(0.0)
#define all(a) a.begin(),a.end()
#define oo 1<<29;

char letters[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main(void)
{
    freopen ("A.in" , "r" , stdin);
    freopen ("A.out" , "w" , stdout);
    int t_c , a = 0;
    scanf("%d",&t_c);
    scanf("%*c");
    while (t_c--)
    {
        string s;
        getline(cin , s);

        printf("Case #%d: ",++a);
        for (int i=0 ; i<sz(s) ; i++)
        {
            if (s[i] == ' ')
                printf(" ");
            else
                printf("%c",letters[s[i] - 'a']);
        }
        printf("\n");

    }
    return 0;
}
