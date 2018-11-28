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
#include <string>

using namespace std;

void doit(){
	long long v[1001], tot[1001],ptot=0,ctot=0,ttot,cinx=0,crnd=1; //cinx eqvi to n; crnd eqvi to rnd
	long long rnd,mx,n,sz[1001],grptot=0;
	long long tmprnd,tmpval;
	cin>>rnd>>mx>>n;
	memset(v,0,sizeof(v));
	for(int i=0;i<n;i++){
		cin>>sz[i];
		grptot+=sz[i];
	}
	while(crnd<=rnd && !v[cinx]){
		v[cinx]=crnd++; 
		tot[cinx]=ptot;
		ttot=0;
		while(ttot+sz[cinx]<=mx && ttot+sz[cinx]<=grptot){
			ttot+=sz[cinx++];
			if(cinx==n)cinx=0;
		}
		ptot+=ttot;
	}
	//crnd-v[cinx] rounds for ptot-tot[cinx] euros
	tmprnd=crnd-v[cinx];tmpval=ptot-tot[cinx];
	rnd-=(crnd-1);
	ptot+=(rnd/tmprnd)*tmpval;
	rnd-=((rnd/tmprnd)*tmprnd);
	if(rnd>0){
		while(rnd--){
			ttot=0;
			while(ttot+sz[cinx]<=mx && ttot+sz[cinx]<=grptot){
				ttot+=sz[cinx++];
				if(cinx==n)cinx=0;
			}
			ptot+=ttot;
  		}
	}
	cout<<ptot<<endl;
return;

}
int main(){
    int tc;
    cin>>tc;
    for(int i=1;i<=tc;i++){
        cout<<"Case #"<<i<<": ";
        doit();
    }
    return 0;
}
