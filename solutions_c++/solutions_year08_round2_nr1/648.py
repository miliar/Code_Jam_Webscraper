#include <vector>
#include <list>
#include <ctime>
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
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define ll  long long
#define pb push_back
#define mp make_pair
#define size(v) (int)(v.size())
#define loop(i,n) for(i=0;i<n;i++)
#define all(v) v.begin(), v.end()
#define tr(container, it)  for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define vi vector<int>
#define vvi vector<vector<int> > vvi
#define vs vector<string>

using namespace std;
bool xfind(int x,int y,vector<pair<int,int> >& vec){
	for(int i=0;i<size(vec);i++){
		if(vec[i].first==x&&vec[i].second==y) return true;
	}
	return false;
}

bool isdiv(int x){
	int sum=0;
	while(x>0){
		sum+=x%10;
		x/=10;
	}
	if(sum%3==0) return true;
}
int main() {

    int i,j,k;
    int t;
    cin>>t;
    for(int numt=0;numt<t;numt++){
    	ll n,a,b,c,d,x0,y0,m;

    	cin>>n>>a>>b>>c>>d>>x0>>y0>>m;
    	ll x=x0,y=y0;
    	vector<pair<ll,ll> > vec;
    	vec.pb(mp(x0,y0));
    	//cout<<x0<<" "<<y0<<endl;
    	//cout<<n<<a<<c<<x0<<m<<endl;
    	for(i=1;i<n;i++){
    		x=(a*x+b)%m;
    		y=(c*y+d)%m;
    		//cout<<x<<" "<<y<<endl;
    		vec.pb(mp(x,y));
    	}

    	int cnt=0;
    	vector<int > done(n,0);
    	for(i=0;i<size(vec);i++){
    		for(j=i+1;j<size(vec);j++){
    			for(k=j+1;k<size(vec);k++){
    				//if(done[i]&&done[j]&&done[k]) continue;
    				x=(vec[i].first+vec[j].first+vec[k].first);
    				y=(vec[i].second+vec[j].second+vec[k].second);
    				if(x%3==0&&y%3==0){
    					//if(xfind(x,y,vec))cnt++;
    					done[i]=done[j]=done[k]=1;
    					cnt++;
    				}
    			}
    		}
    	}


    	cout<<"Case #"<<numt+1<<": "<<cnt<<endl;
    }

    return 0;
}
