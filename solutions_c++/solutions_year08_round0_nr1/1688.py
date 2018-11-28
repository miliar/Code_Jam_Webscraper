#include<iostream>
#include<cmath>
#include<string>
#include<sstream>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<numeric>

using namespace std;

#define MAX INT_MAX
#define EPS (1e-10)

#define pb(a) push_back(a)
#define mp(a,b) make_pair(a,b)
#define K(a) ((a)*(a))

#define REP(i,v) for(typeof((v).begin()) i = (v).begin(); i!= (v).end(); ++i )
#define FOR(i,v) for(int i=0; i<v.size(); ++i)

typedef pair<int,int> pii;

int n;
int nAkt;
set<string> s;
set<string> nazwy;
char ss[111];

int main(){
    freopen ("a.out","w",stdout);
    freopen ("a.in","r",stdin);

	
	
	scanf("%d\n",&n);
	for(int i=0; i<n; i++){
		nazwy.clear();
		s.clear();
		int ret=0;
		
		
		scanf("%d\n",&nAkt);
		for(int j=0; j<nAkt; j++){
			gets(ss);
			nazwy.insert(string(ss));
			
//			cout<<string(ss)<<endl;
            }
//        cout<<endl;

        
        scanf("%d\n",&nAkt);
		for(int j=0; j<nAkt; j++){
			gets(ss);
			s.insert(string(ss));
			if(s.size()==nazwy.size()){
                                       ret++;
                                       s.clear();
                                       s.insert(string(ss));
                                       }
            }

        printf("Case #%d: %d\n",i+1,ret);            
        }			


return 0;
}
