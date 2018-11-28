#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <queue>
#include <numeric>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ext/hash_map>
#include <ext/hash_set>

#define LL long long 

#define F(i,a,b) for(long long i=(a);i<(b);++i)
#define Fe(it,v)for(__typeof__((v).begin()) it=(v).begin();it!=(v).end();++it)
#define all(x) (x).begin(),(x).end()
using namespace std;


#define pii pair<int,int> 

#define X first 
#define Y second 


int main(){
	int N,test=1;
	cin>>N;
	while(N--){
		int L;
		cin>>L;
		
		string S="";
		
		F(i,0,L){
			string s;
			int t;
			cin>>s>>t;
			F(j,0,t)S+=s;
		}
		
		deque<pii> v;
		
		int n=S.length();
		
		int x=0,y=0;
		int k=0;
		
		int dx[4]={0,1,0,-1},dy[4]={1,0,-1,0};
		
		F(i,0,n){
			if(S[i]=='L'){
				v.push_back(pii(x,y));
				k=(k+3)%4;
			}
			else if(S[i]=='R'){
				v.push_back(pii(x,y));
				k=(k+1)%4;
			}
			else{
				x+=dx[k];
				y+=dy[k];
			}
			
		}
		if(!(v[0].X==0&&v[0].Y==0))v.push_front(pii(0,0));
		if(S[n-1]!='F')v.pop_back();
		
		
		
		
		
		n=v.size();
		
		/*F(i,0,n){
			cout<<v[i].X<<" "<<v[i].Y<<endl;
		}*/
		
		
		
		vector<pii> V;
		vector<int> tru;
		
		
		
		
		F(i,0,n-1){
			if(v[i].X==v[i+1].X)V.push_back(pii(v[i].Y,v[i+1].Y)),tru.push_back(v[i].X);
		}
		
		
		
		if(v[n-1].X==v[0].X)V.push_back(pii(v[n-1].Y,v[0].Y)),tru.push_back(v[n-1].X);
		
		
		Fe(it,V){
			if(it->X > it->Y)swap(it->X,it->Y);
		}
		
		/*vector<pii> H;
		vectro<int> tru2;
		
		F(i,0,n-1){
			if(v[i].y==v[i+1].y)H.push_back(pii(v[i].X,v[i+1].X)),tru2.push_back(v[i].Y);
		}
		
		
		
		if(v[n-1].Y==v[0].Y)H.push_back(pii(v[n-1].X,v[0].X)),tru2.push_back(v[n-1].Y);
		
		
		Fe(it,H){
			if(it->X > it->Y)swap(it->X,it->Y);
		}*/
		
		
		bool b[220][220]={};
		
		int panxo=0;
		
		F(i,-100,100)F(j,-100,100){
			
			//bool inside=0;
			
			int ct=0;
			int m=V.size();
			F(k,0,m){
				if(tru[k]>i&&j>=V[k].X&&j<V[k].Y){
					++ct;
				}
			}	
			if(ct%2==1){
				b[i+101][j+101]=1;//inside;
				++panxo;
			}
			
		}
		
		//cout<<panxo<<endl;
		
		int area=0;
		
		F(i,-100,100)F(j,-100,100)if(b[i+101][j+101]==0){
			bool ok1=0,ok2=0,ok3=0,ok4=0;
			F(k,i+1,100){
				if(b[k+101][j+101]){
					ok1=1;
					break;
				}
			}
			for(int k=i-1;k>=-100;--k){
				if(b[k+101][j+101]){
					ok2=1;
					break;
				}
			}
			F(k,j+1,100){
				if(b[i+101][k+101]){
					ok3=1;
					break;
				}
			}
			for(int k=j-1;k>=-100;--k){
				if(b[i+101][k+101]){
					ok4=1;
					break;
				}
			}
			if((ok1&&ok2)||(ok3&&ok4))++area;
		}
		
		cout<<"Case #"<<test++<<": "<<area<<endl;
	}
}
