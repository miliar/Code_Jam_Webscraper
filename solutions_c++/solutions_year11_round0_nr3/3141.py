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
int pamti=0,odgovor=0,pocetok,kraj,a[1001],b[1001],c[1001];
bool ok,final;

string s;


int main()
{
//ios::sync_with_stdio(false);
   freopen("C-small-attempt0.in","r",stdin); freopen("output.txt","w",stdout);
//   start = clock();//if (clock() - start >0.72 * CLOCKS_PER_SEC) { final=true; vreme=true; return;}

    cin>>t;
    int tt;

   fo(tt,t)
    {
        odgovor=-1;
        cin>>n;
        fo(i,n)
        cin>>a[i];

        fro(i,(1<<n)-1)
        {
             f=0; g=0; k=0;br=0;
            fro(j,n)
            if (i&(1<<j))
            {
                f++; k+=a[j+1];
                b[f]=a[j+1];
            } else
            {
                g++; br+=a[j+1];
                c[g]=a[j+1];
            }
            br=max(br,k);
            m=b[1];
            fr(j,2,f)
            m^=b[j];
           k=c[1];
           fr(j,2,g)
           k^=c[j];


            if (m==k)
            odgovor=max(odgovor,br);
        }
        if (odgovor==-1)
        cout<<"Case #"<<tt<<": NO"<<endl; else
        cout<<"Case #"<<tt<<": "<<odgovor<<endl;

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
