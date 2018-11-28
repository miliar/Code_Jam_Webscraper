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



int n,nb,p,s,bno,t,m,i,j,k;

vector<pii> balls;
pii bv;

int T;

int main()
{

    char a[26];

    a[0]='y';
    a[1]='h';
    a[2]='e';
    a[3]='s';
    a[4]='o';
    a[5]='c';
    a[6]='v';
    a[7]='x';
    a[8]='d';
    a[9]='u';
    a[10]='i';
    a[11]='g';
    a[12]='l';
    a[13]='b';
    a[14]='k';
    a[15]='r';
     a[16]='z';
    a[17]='t';
    a[18]='n';
    a[19]='w';
    a[20]='j';
    a[21]='p';
    a[22]='f';
    a[23]='m';
    a[24]='a';
    a[25]='q';

    freopen("A-small-attempt2.in","r",stdin);
    freopen("A-small-attempt2.out","w+",stdout);
cin>>nb;
char name[100];
    int itr=0;
    for(itr=0;itr<=nb;itr++){
        char temp;
        cin.getline(name,105);
        if(itr==0){continue;}
        else{
        cout<<"Case #"<<itr<<": ";
        }
        //name*=gets();

        fj(100){

            if(name[j]=='\0')
                break;

            if(isalpha(name[j])){

               // cout<<name[j];
               if(name[j]=='a')
                    cout<<'y';
                else
                    cout<<a[name[j]-'a'];

            }
            else
            {
                cout<<' ';
            }

        }
        cout<<endl;

    }


return 0;
}
