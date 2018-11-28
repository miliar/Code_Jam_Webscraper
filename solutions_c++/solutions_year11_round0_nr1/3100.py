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
char c;
bool ok,final;

string s;


int main()
{
//ios::sync_with_stdio(false);
   freopen("A-large.in","r",stdin);  freopen("output.txt","w",stdout);
//   start = clock();//if (clock() - start >0.72 * CLOCKS_PER_SEC) { final=true; vreme=true; return;}

    cin>>t;
    int tt;

   fo(tt,t)
    {
        queue<int> r1,r2,r3;
        cin>>n;
       br=0;
       // meset(a,false); meset(b,false);
        fo(i,n)
        {
            cin>>c>>x;
            if (c=='O')   r1.push(x);  else
              r2.push(x);
            r3.push(c);
        }
        br=0;
        x=1;
        y=1;
        while(!r3.empty())
        {
            ok=false;

            if (r3.front()=='O')
            {
                if (x==r1.front())
                {


                    r1.pop();
                    r3.pop();
                     if (!r2.empty()&&y<r2.front()) {y++;  } else
            if (!r2.empty()&&y>r2.front()) {y--; }
            br++;
            continue;
                }
            } else
            {
                if (y==r2.front())
                {
                    ok=true;

                    r2.pop();
                    r3.pop();
                     if (!r1.empty()&&x<r1.front()) { x++;} else
            if (!r1.empty()&&x>r1.front()) {x--; }
            br++;
            continue;
                }
            }


            if (!r1.empty()&&x<r1.front()) { x++;} else
            if (!r1.empty()&&x>r1.front()) {x--; }
            if (!r2.empty()&&y<r2.front()) {y++;  } else
            if (!r2.empty()&&y>r2.front()) {y--; }
            br++;
        }

        cout<<"Case #"<<tt<<": "<<br<<endl;

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
