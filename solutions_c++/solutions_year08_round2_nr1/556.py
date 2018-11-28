#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <map>

#define foreach(it,c) for(typeof((c).begin()) it=(c).begin(); it != (c).end() ; it++ )
#define F(i,mi,ma) for(int i=mi;i<ma;i++)

#define vi vector< int >
#define vs vector< string >
#define vb vector< bool >
#define bn begin()
#define en end()
#define sz size()
#define pb push_back

using namespace std;

int main()
{
    int N;

    ifstream in("asmall.in");
    ofstream out("asmall.out");

    in >> N;
    F(i,0,N){
             long long n,a,b,c,d,x0,y0,M;
             in >> n >> a>>b>>c>>d>> x0>>y0 >> M ;
             //set< pair<int,int> > trs;
             vector< pair<int,int> > trv;
             //trs.insert( make_pair(x0,y0));
             trv.pb( make_pair(x0,y0));
             
             F(j,1,n) {
                      x0 =( a*x0 + b)%M ;
                      y0 =( c*y0 + d)%M ;
                      //trs.insert( make_pair(x0,y0));
                      trv.pb( make_pair(x0,y0));
             }
             
             long long ans = 0;
             
             F(p,0,n){
                     F(q,p+1,n){
                              //if(q==p) continue;
                              F(r,q+1,n){
                                       //if(r==q or r==p) continue;
                                       if( (trv[p].first + trv[q].first + trv[r].first)%3 == 0  and
                                           (trv[p].second + trv[q].second + trv[r].second)%3 == 0
                                       ) ans++;
                              }
                     }
             }
             
             out << "Case #"<<i+1<<": "<<ans<<endl;
    }

    out.close();
    in.close();
    cout<<"done";
    getchar();
}



