#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define FOR(i,a,b) for(int i=(int)a;i<(int)b;++i)
#define REP(i,n) FOR(i,0,n)
#define IT(c) __typeof((c).begin())
#define FORIT(i,c) for(IT(c) i=(c).begin();i != (c).end();++i)
#define ALL(c) (c).begin() , (c).end()
#define CLEAR(a, b) memset(a, b, sizeof(a))
#define PB push_back
#define MP make_pair
#define TC int tt;scanf("%d",&tt);while(tt--)
#define scan(a) fscanf(in,"%d",&a)
using namespace std;
int main()
{
	freopen("j.in","r",stdin);
	 freopen("out.out","w",stdout);
    int count=1;
	int tt;
    cin>>tt;
    string a;
    getline(cin,a);
    FOR(nn,1,tt+1)
    {  
       getline(cin,a);
     //  cout<<a;
       stringstream ss(a);
       string coun,str;
	ss>>coun;
           int key=atoi(&coun[0]);
           vector<int> o,b;
           string seq="";
           int lasto = 1, lastb = 1;
           int ans=0,lb=0,lo=0;
           while(ss>>str)
           {

               if(str.length()==1 && str =="O")
               {
                   seq=seq+str;
                   ss>>str;
                   int cc = atoi(&str[0]);
                    o.push_back(abs(lasto-cc)+1);
                    lasto = cc;
               }
               else if(str.length()==1 && str =="B")
               {
           //cout << str<<"\n";
                   seq=seq+str;
                   ss>>str;
                   int cc = atoi(&str[0]);
                    b.push_back(abs(lastb-cc)+1);
                    lastb= cc;
            // cout << b[1] <<"\n";       
               }
           }
           int siz = b.size();
           int curr =0;
          // REP(i,siz) cout <<b[i]<<" ";
          int sou=o.size();
               int sa=b.size();
            /*   REP(mm,sou) cout << o[mm] <<" ";
               cout <<"\n";
	       REP(mm,sa) cout << b[mm] <<" ";
	       cout <<"\n\n\n";
	       cout << seq <<'\n';*/
           for(int i=1;i<=key;i++)
           {
          // cout << "ans " << ans <<'\n';
               if(seq[curr]=='O')
               {
               //  cout << "Orange"<<lo<<" "<<lb<<"\n";
                   if( lo<o.size() && lb<b.size())
                   {
                   	if(b[lb]<=o[lo] && b[lb]>1 )
                   	{
                  // 		cout<< "orange greater\n";
                   		    b[lb]=1;
                   	}
                   	else if(b[lb]>o[lo] && b[lb]>=1 )
                   	{
                //   	    cout<< "blue greater\n";
                   	     b[lb]=b[lb]-o[lo];
                   	}
                   }
                   ans+=o[lo];
                   lo++;
                   curr++;
               }
               else
               {
              // cout << "blue\n";
                   if( lo<o.size() && lb<b.size())
                   {
                  	if(b[lb]>=o[lo] && o[lo]>1 )
                  	{
                      		o[lo]=1;
                  	}
                  	else if(b[lb]<o[lo] && o[lo]>=1 && lo<o.size() && lb<b.size())
                  	{
                      		o[lo]=o[lo]-b[lb];
                  	}
               	  }
                  	ans+=b[lb];
                  	lb++;
               		curr++;
               }
             /*  sou=o.size();
               sa=b.size();
               REP(mm,sou) cout << o[mm] <<" ";
               cout <<"\n";
	       REP(mm,sa) cout << b[mm] <<" ";
	       cout <<"\n";*/
           }           
            cout <<"Case #"<<count <<": " <<ans<<"\n";
            count++;
    }
    return 0;
}

