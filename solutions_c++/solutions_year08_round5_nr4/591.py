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

long long C[110][110];
int a[110][110];
int H,W;
int x[]={2,1};
int y[]={1,2};
bool in(int i, int j){return i>=0&&i<H&&j>=0&&j<W;}
int main(){
    int N;
	cin>>N;
    for(int l=1; l<=N; l++){
            int R;
	    cin>>H>>W>>R;
	    zer(C);zer(a);
	    int r,c;
	    for(int i=0; i<R; i++)
	      {cin>>r>>c; a[r-1][c-1]=-1;}
	    C[0][0]=1;
	    for(int i=0; i<H; i++)
	      for(int j=0; j<W; j++)
		for(int k=0;k<2; k++){
		    int ii=i+x[k]; int jj=j+y[k];
		    if(in(ii,jj)&&a[ii][jj]!=-1)
		      C[ii][jj]=(C[ii][jj]+C[i][j])%10007;
	        } 
	    int ret=C[H-1][W-1];
	    cout<<"Case #"<<l<<": "<<ret<<endl;
	}
}
