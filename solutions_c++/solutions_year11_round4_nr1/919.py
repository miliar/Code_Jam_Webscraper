
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<string>
#include<string.h>
#include<cstring>
#include<stack>
#include<queue>
#include<cassert>

using namespace std;

#define LL long long int 
#define PII pair<int,int> 
#define PB push_back
#define MP make_pair
#define INF 1000000000
vector<PII> esc,frgrnd;

int main(){
	int T,test,X,S,R,t,N,i,beg,end,sp,grnd;
	scanf("%d",&test);
	for(T=1;T<=test;T++){
		scanf("%d %d %d %d %d",&X,&S,&R,&t,&N);
		esc.clear();
		frgrnd.clear();
		for(i=1;i<=N;i++){
			scanf("%d %d %d",&beg,&end,&sp);
			esc.push_back(MP(sp,(end-beg)));
			frgrnd.PB(MP(beg,end));
		}
		sort(esc.begin(),esc.end());
		reverse(esc.begin(),esc.end());
		frgrnd.PB(MP(X,X));
		frgrnd.PB(MP(0,0));
		sort(frgrnd.begin(),frgrnd.end());
		grnd=0;
		for(i=1;i<frgrnd.size();i++)
			grnd+=frgrnd[i].first-frgrnd[i-1].second;
		if(grnd!=0)
			esc.PB(MP(0,grnd));
		double remtime=t,tottime=0,distrem,tottime1=0;
		for(i=0;i<esc.size();i++){
			if(remtime-(esc[i].second/(double)(R+esc[i].first))>=0){
				remtime-=esc[i].second/(double)(R+esc[i].first);
				tottime+=esc[i].second/(double)(R+esc[i].first);
			}
			else{
				tottime+=remtime;
				distrem=esc[i].second-(R+esc[i].first)*remtime;
				tottime+=distrem/(double)(S+esc[i].first);
				remtime=0;
			}
		}
		remtime=t;
		for(i=esc.size()-1;i>=0;i--){
			if(remtime-(esc[i].second/(double)(R+esc[i].first))>=0){
				remtime-=esc[i].second/(double)(R+esc[i].first);
				tottime1+=esc[i].second/(double)(R+esc[i].first);
			}
			else{
				tottime1+=remtime;
				distrem=esc[i].second-(R+esc[i].first)*remtime;
				tottime1+=distrem/(double)(S+esc[i].first);
				remtime=0;
			}
		}

		printf("Case #%d: %.8lf\n",T,min(tottime,tottime1));
	}
	return 0;
}
