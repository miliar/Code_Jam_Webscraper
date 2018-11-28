#include <map>
#include <set>
#include <vector>
#include <string>
#include <cstring>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <math.h>
using namespace std;

typedef vector<int> vi; 
typedef vector<string> vs; 
 typedef vector<vi> vvi; 
 typedef pair<int,int> ii; 
 #define sz(a) int((a).size()) 
 #define pb push_back 
 #define all(c) (c).begin(),(c).end() 
 #define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
 #define present(c,x) ((c).find(x) != (c).end()) 
 #define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define REP(i,n) for (int i = 0; i < (n); i++)
#define REPD(i,n) for (int i = (n) - 1; i >= 0; i--)
#define sqr(a) (a)*(a)
#define inf 100000
	double  eps2 = 1e-8;
	double  eps = 1e-15;


int main(){
	int N;
	cin >> N;
	REP(i,N) {
		int M,V;
		cin>>M>>V;
		vi G(M, 0); vi C(M, 0);
		vi I(M, 0);
		vi res(M, inf);
		REP(j, (M-1)/2){
			cin>>G[j]>>C[j];
//			cout<<G[j]<<" "<<C[j]<<"\n";
		}
		for(int j= (M-1)/2; j<M; j++){
			cin>>I[j];
			if(I[j]==V)res[j]=0;
//			cout<<I[j]<<" "<<res[j]<<"\n";
		}
		for(int j=(M-1)/2-1; j>=0; j--){
//cout<<j<<" " ; cout.flush();
			res[j]=min(res[2*(j+1)], res[2*(j+1)-1]);
			if(V==0){
				if(C[j]!=0){
					if(G[j]==0 && res[j]+1<res[2*(j+1)]+ res[2*(j+1)-1]){
					G[j]=1; //and
					res[j]+=1;
					}else{
						if(G[j]==0)
						res[j]=res[2*(j+1)]+ res[2*(j+1)-1];
					}
				}else{
					if(G[j]==0)	
						res[j]=res[2*(j+1)]+ res[2*(j+1)-1];
				}
			}else{//v=1
				if(C[j]!=0){
					if(G[j]==1 && res[j]+1<res[2*(j+1)]+ res[2*(j+1)-1]){
					G[j]=0;res[j]+=1;
					}else{
						if(G[j]==1)
						res[j]=res[2*(j+1)]+ res[2*(j+1)-1];
					}
				}else{

					if(G[j]==1)	
						res[j]=res[2*(j+1)]+ res[2*(j+1)-1];
				}
			}
//			cout<<res[j]<<" ";
		}
		if(res[0]<inf){
		cout << "Case #" << i+1 << ": " << res[0]<< "\n";
		}else{
		cout << "Case #" << i+1 << ": " << "IMPOSSIBLE"<< "\n";
		}
		
	}
	exit(0);
}

