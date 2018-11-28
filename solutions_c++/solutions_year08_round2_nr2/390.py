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

int a[1001][1001];
int v[1001];
int A,B;
void visit(int k){
   v[k]=1;
   for(int j=A; j<=B; j++)
     if(a[k][j]&&!v[j]) visit(j);
}
int main(){
    int N;
	cin>>N;
    for(int l=1; l<=N; l++){
	    int P;
	    cin>>A>>B>>P;
		vector<int> pr;
	    for(int i=P; i<=B;i++){
		  int ok=1;
		  for(int j=2; j*j<=i; j++)
			 if(i%j==0) {ok=0;break;}
		  if(ok) pr.push_back(i);	 
	    }
		zer(a);zer(v);
		for(int i=A; i<=B; i++){
		  for(int j=i+1; j<=B; j++){
			 for(int k=0; k<pr.size(); k++)
			   if(i%pr[k]==0&&j%pr[k]==0) {a[i][j]=a[j][i]=1; break;}
		  } 	 
		} 
		int ret=0;
		for(int i=A; i<=B; i++)
		  if(!v[i]) {ret++; visit(i);}
	    cout<<"Case #"<<l<<": "<<ret<<endl;
	}
}
