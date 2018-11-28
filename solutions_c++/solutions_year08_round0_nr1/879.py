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

string s[101];
string q[1001];
int a[101][1001];
int mp[1001];
char c[256];
int m,n;

int f(int i, int j){
   if(j==n-1)
     if(s[i]==q[j]) return 1;
	 else return 0;
   if(a[i][j]!=-1) return a[i][j];	 

   int ret=INT_MAX;
   if(s[i]!=q[j]) ret=f(i,j+1);
   else{
      for(int k=0; k<m; k++){
		if(i==k) continue;
		ret<?=1+f(k,j);
	  }
   }
   return a[i][j]=ret;
}

int main(){
    int N;
	cin>>N;
    for(int l=1; l<=N; l++){
		scanf("%d\n",&m);
		for(int j=0; j<m; j++){
			cin.getline(c,256);
			s[j]=string(c);
		}
		scanf("%d\n",&n);
		for(int j=0; j<n; j++){
			cin.getline(c,256);
			q[j]=string(c);
		}
		for(int j=0; j<n; j++)
		  for(int i=0; i<m; i++)
		    if(q[j]==s[i]) mp[j]=i;
			
		int ret=INT_MAX;
		for(int i=0; i<m; i++)
		  for(int j=0; j<n; j++)
		    a[i][j]=-1;
		for(int i=0; i<m; i++)
		  ret<?=f(i,0);
	    cout<<"Case #"<<l<<": "<<ret<<endl;
	}
}
