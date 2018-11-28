#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
using namespace std;
typedef vector<int> vi;
typedef vector<string> vs;
typedef stringstream sst;
#define fri(a,i) for(typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define fr(i,n) for(int i=0; i<(int)(n); i++)
#define zer(a) memset((a),0,sizeof(a));
#define all(a) (a).begin(), (a).end()
#define pb push_back

int x[101],y[101];
int main(){
    int N;
	cin>>N;
    for(int l=1; l<=N; l++){
	    long long n,A,B,C,D,M;
		long long x0,y0;
	    cin>>n>>A>>B>>C>>D>>x0>>y0>>M;
		x[0]=x0; y[0]=y0;
		for(int i=1; i<n; i++){
			x0=(A*x0+B)%M;
			y0=(C*y0+D)%M;
			x[i]=x0; y[i]=y0;
		}
		//for(int i=0; i<n; i++)
		//  cout<<x[i]<<" "<<y[i]<<endl;
		long long ret=0;
		for(int i=0; i<n; i++)  
		  for(int j=i+1; j<n; j++)
		    for(int k=j+1; k<n; k++){
			  long long xx=x[i]+x[j]+x[k];
			  long long yy=y[i]+y[j]+y[k];
			  if(xx%3==0&&yy%3==0) ret++;
			 // for(int kk=0; kk<n; kk++)
			//	if(x[kk]==xx/3&&y[kk]==yy/3) {ret++; break;}
			  }
	    cout<<"Case #"<<l<<": "<<ret<<endl;
	}
}
