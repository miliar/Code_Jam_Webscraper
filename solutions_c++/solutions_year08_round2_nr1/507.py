#include <vector>
#include <fstream>
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
#include <queue>
using namespace std;
#define REP(i,n) for (int i=0; i<(n); i++)
#define FOR(i,a,b) for (int i=(a); i<=(b); i++) 
#define ALL(c) (c).begin(),(c).end()
typedef long long ll;


int main(){

	ifstream in("A-small-attempt0.in");
	ofstream out("output.out");

	ll N;
	in>>N;
 
	
	REP(i,N){
        ll n,A,B,C,D,x0,y0,M;
		in>>n;
        cout<<n<<endl;
        in>>A;
        in>>B;
        in>>C;
        in>>D;
        in>>x0;
        in>>y0;
        in>>M;
		set < pair <ll,ll > > points;
        ll X=x0,Y=y0;
        ll count=0;
        points.insert(make_pair(X,Y));
        //cout<<"points";
        for(ll j=0;j<n-1;j++){

           X=(A*X+B)%M;
           Y=(C*Y+D)%M;
           points.insert(make_pair(X,Y));
            //cout<<X<<" "<<Y<<endl;
        }

        for(set < pair < ll, ll > >::iterator it1=points.begin();it1!=points.end();it1++){
               set < pair <ll,ll >  >::iterator it2=it1;
               it2++;
            for(;it2!=points.end();it2++){
                    set < pair <ll,ll >  >::iterator it3=it2;
                    it3++;
                   for(;it3!=points.end();it3++){
                     
                           double xt=(it1->first)+(it2->first)+(it3->first);
                           double yt=(it1->second)+(it2->second)+(it3->second);
                           
                           xt/=3;
                           int xz=xt;
                            yt/=3;
                            int yz=yt;
                           //cout<<xt<<" "<<yt<<endl;
                           if((double )xz==xt && (double )yz==yt){
                              // cout<<xt<<" "<<yt<<endl;
                                count++;
                           }
                       
                    }   
        
            }
        
        }

        //cout<<"met"<<endl;
        
		out<<"Case #"<<(i+1)<<": "<<count<<endl;
        
	
	}
	
	//int a;
    //cin>>a;

	return 0;


}
