#include<iostream>
#include<queue>
#include<stack>
#include<string>
#include <vector>
#include <algorithm>
#include <cmath>
#include<fstream>
#include <numeric>
#include <sstream>
#include<map>
#include<set>
#include<cstring>
#include <stdio.h>
#include <ctime>
using namespace std;
#define sz     size()
#define pb push_back
#define mp make_pair
#define fo(i, n) for ( i = 1; i <= (int)(n); i++)
#define fr(i, k, n) for ( i = k; i <= (int)(n); i++)
#define sortvektor(s)   sort((s).begin(),(s).end())
#define reversevektor(s)   reverse((s).begin(),(s).end())
#define fro(i, n) for ( i = 0; i < (int)(n); i++)
#define meset(x,y) memset((x),(y),sizeof((x)))
string itos (int i) {stringstream s; s << i; return s.str();}
string lltos (long long i) {stringstream s; s << i; return s.str();}
long long stoll (string target) { stringstream s; s << target; long long w; s >> w; return w;}
int stoi (string target) { stringstream s; s << target; int w; s >> w; return w;}

int   x=0,y,z,pom,start,h,t,i,j,n,k=0,m,br=0,mom=0,f,g;
int pamti=0,odgovor=0,pocetok,kraj,prv,vtor,tret;
char c[300][300],d[5000],e[5000];
bool ok,final,a[300][300],b[300][300];

string s;


int main()
{
//ios::sync_with_stdio(false);
   freopen("B-large.in","r",stdin); freopen("output.txt","w",stdout);
//   start = clock();//if (clock() - start >0.72 * CLOCKS_PER_SEC) { final=true; vreme=true; return;}

    cin>>t;
    int tt;

   fo(tt,t)
    {
        meset(a,false);
        meset(b,false);
        cin>>n;
        fo(i,n)
        {
            cin>>s;
            a[s[0]][s[1]]=true;
            a[s[1]][s[0]]=true;
             c[s[0]][s[1]]=s[2];
            c[s[1]][s[0]]=s[2];
        }
        cin>>n;
        fo(i,n)
        {
            cin>>s;
             b[s[0]][s[1]]=true;
            b[s[1]][s[0]]=true;
        }
        cin>>n;
        fo(i,n)
        cin>>d[i];
        e[1]=d[1];
        k=1;

        fr(i,2,n)
        {
            k++;
            e[k]=d[i];

        tuka:

           if (k>1)
            if (a[e[k]][e[k-1]])
            {
                  e[k-1]=c[e[k]][e[k-1]];
                  k--;
                  goto tuka;
            }
            fo(j,k-1)
            if (b[e[k]][e[j]])
            {
                k=0; break;
            }


        }

        cout<<"Case #"<<tt<<": [";
        if (k==0) cout<<"]"<<endl; else
        if(k==1) cout<<e[k]<<"]"<<endl; else
        {
            cout<<e[1];
            fr(i,2,k)
            cout<<", "<<e[i];
            cout<<"]"<<endl;
        }

    }


// fo(i,1000)
     //   cout<<(i%23)*i+(i*i)%47<<endl;
       // AmoebaDivTwo w;
//vector <string> deni;
//vector<int> d;

 //deni.pb("MA");
  //deni.pb("19 6 2 14");
   //deni.pb("15 3 4 1");
//deni.pb("20");
 // deni.pb("11");
  //  deni.pb(6);
 //cout<<w.count(deni);
 // cout<<w.wordWrap("h t h fdqbbsmiw kuepwak b hbsuni rh tbkqn b fgmcgvuiywlnu jfrb xu teu xm bbcpn p ogvtfc fj megeetkwt", 4, 3);
//cout<<w.wordWrap("m qmw t o s h e s b d r k a c r cb wh x o sv v t i w h c v fo h l l a m a m p icuyop ul r fij u q i ", 24, 6);
 // {6,5,4,2}, {1,3}, 8
// int myints[] = {10,20,30,30,20,10,10,20};
 // vector<int> v(myints,myints+8);
  // deni.pb("B");
  // cout<<w.getTop("W");
  /*    deni.pb(2);
       */
// deni.pb("SSSS");
 //deni.pb("R");
 //drvo=w.animals(3,8);
 //for (int i=0;i<(int)drvo.size();i++)
 //cout<<drvo[i];
//cout<<w.getCount(220,220);
//stringstream ss;
 //   string scol;
  //  ss << sq[i];
   // ss >> scol >> sz[i];
    return 0;
}
