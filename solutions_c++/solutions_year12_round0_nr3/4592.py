#include <iostream>
#include <iostream>
#include <iostream>
#include <stdio.h>
#include <iomanip>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>

#define fo(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )

using namespace std;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;



int n,nb,p,s,bno,ct,t,m,i,j,k,x;
int itr=0,a,b,c;
int ct1,ct2,possible_s,num;
vector<pii> balls;
pii bv;

int T;

int main()
{

//freopen("test.txt","r",stdin);
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w+",stdout);
//cin>>nb;

//string s1,s2;
int A,B,a1,a2,a3,t1,t2;
char s1[7];
char s2[7];
int it=0;
cin>>nb;
for(it=0;it<nb;it++){




cin>>A;
cin>>B;

ct=0;
for(x=B;x>=A;x--)
{
    if(x==1000)
    {
        if(A==1)
        {
            ct++;
        }

    }
    else if(x>99)
    {
        //cout<<"99 awa"<<endl;
        a1=x%10;
        a2=(x/10)%10;
        a3=(x/100);

        t1=a1*100+a3*10+a2;
        t2=a2*100+a1*10+a3;

        if((t1>=A)&&(t1<=B)&&(x<t1))
        {
            ct++;
        }
        if((t2>=A)&&(t2<=B)&&(x<t2))
        {
            ct++;
        }
    }
    else if(x>9)
    {
       // cout<<"9 awa"<<endl;
        a1=x%10;
        a2=x/10;

        t1=a1*10+a2;
        //cout<<"t1 ="<<t1<<" ct = "<<ct<<endl;
        if((t1>=A)&&(t1<=B)&&(x<t1))
        {
            ct++;
        }
    }

}

cout<<"Case #"<<it+1<<": "<<ct<<endl;

}
return 0;
}
