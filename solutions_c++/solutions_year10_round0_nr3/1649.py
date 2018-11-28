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

#define sort(A) sort(A.begin(),A.end()) 
#define rei(i,A,B) for(long long i=A;i<B;i++) 
#define red(i,A,B) for(long long i=A;i>=B;i--)
#define ree(i,A,B) for(long long i=A;i<=B;i++) 
#define pb(A,B) A.push_back(B)

using namespace std;

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	long long T;
	cin>>T;
	rei(t,0,T){
		long long r,k,N;
		cin>>r>>k>>N;
		vector<long long> g(N,0);
		rei(i,0,N){
			long long gS;
			cin>>gS;
			g[i]=gS;
		}
		map<vector<long long>,bool> grs;
		long long ppl=0;		
		rei(i,0,N)
			ppl+=g[i];
		if(ppl<=k){
			cout<<"Case #"<<t+1<<": "<<ppl*r<<endl;
			continue;
		}
		long long p=0;
		map<long long,bool> qS;
		long long Max=N;
		vector<long long> earn;
		long long ret=0;		
		long long rounds=0;
		map<long long,long long> pos;
		while(Max--){
			rounds++;
			qS[p]=true;
			ppl=0;	
			pos[p]=earn.size();	
			while(ppl+g[p]<=k){
				ppl+=g[p++];
				if(p==N)
					p=0;	
			}
			pb(earn,ppl);		
			if(qS[p])
				break;	
		}
		if(r<=rounds){
			rei(i,0,r)
				ret+=earn[i];
			cout<<"Case #"<<t+1<<": "<<ret<<endl;
			continue;				
		}
		rei(i,0,rounds)
			ret+=earn[i];	
		long long Pos=pos[p];
		vector<long long> earnAc;
		rei(i,Pos,earn.size())
			pb(earnAc,earn[i]);
		long long rLeft=r-rounds;
		long long tot=0;
		rei(i,0,earnAc.size())
			tot+=earnAc[i];
		ret+=((rLeft/earnAc.size())*tot);
		long long rem=rLeft%earnAc.size();
		rei(i,0,rem)
			ret+=earnAc[i];
		cout<<"Case #"<<t+1<<": "<<ret<<endl;
	}	
	return 0;
}
