#include <iostream>
#include <fstream>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <string>
#include <iterator>
#include <algorithm>
#include <numeric>
#include <utility>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <cctype>
#include <assert.h>
#include <list>
#include <ext/hash_set>
#include <ext/hash_map>

using namespace __gnu_cxx;
using namespace std;

#define MP(a,b) make_pair(a,b)
#define i64 long long
#define pb push_back
#define For(i,a,b) for(typeof(a) i=(a);i<(b);i++)
#define Rev(i,a,b) for(typeof(a) i=(a);i>=(b);i--)
#define FOREACH(V,it) for(typeof(V.begin()) it=V.begin();it!=V.end();it++)
#define CLR(a,x) memset(a,x,sizeof(a))
#define ALL(x) x.begin(),x.end()

/**********************************************************************************/

int t,Q,M;
double a[100][4],mem[5000];

int main(){
   freopen("C.in","r",stdin);
   scanf("%d",&t);
   
   for(int cas=1;cas<=t;cas++){
   
   	scanf("%d%d",&M,&Q);
	 For(i,0,Q){
		For(j,0,4){
			scanf("%lf",&a[i][j]);
			//cout << a[i][j] << ' ';
		}
		//cout << endl;
	 }
	 
	 int k=pow(4,Q);
	 //cout << k << endl;
	 For(i,0,k){
	    mem[i]=1;
		int cur=i;
		For(j,0,Q){
			mem[i]*= a[j][cur%4];
			
			cur/=4;
		}	
	
	 }
	// cout << endl;
	 sort(mem,mem+k);
	 double ret=0;
	 Rev(i,k-1,k-M){

	  if (i<0) break;
	  
	  ret+=mem[i];	  
	 }
	 printf("Case #%d: %.8lf\n",cas,ret);
   
   }
return 0;
} 
