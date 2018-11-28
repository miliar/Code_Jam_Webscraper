#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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

using namespace std;

typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define mp make_pair

int n;
vector<int> a;
vector<int> b;

void oku(){

  cin>>n;
  a.assign(n,0);
  b.assign(n,0);

  for(int i=0;i<n;i++)
  cin>>a[i]>>b[i];

  long long cnt=0;

  for(int i=0;i<n;i++)
  for(int j=i+1;j<n;j++)
  if(a[i]>a[j] && b[i]<b[j]) cnt++;
  else if(a[i]<a[j] && b[i]>b[j]) cnt++;

  cout<<cnt;
}

int main(){
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);


int tt; cin>>tt;
for(int i=1;i<=tt;i++){

printf("Case #%d: ",i);
oku();

cout<<endl;
}



return 0;}
