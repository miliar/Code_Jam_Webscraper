#include <iostream>
#include <cstdio>
#include <algorithm>
#include <list>
using namespace std;

#define MAX 2000
#define INF 100000000

int n,x[10000];
list <pair<int,int> > li;
list <pair<int,int> >::iterator it,il,ir;

list <pair<int,int> >::iterator operator+(list <pair<int,int> >::iterator a, int x){
	while(x--)
		a++;
	return a;	
}

list <pair<int,int> >::iterator operator-(list <pair<int,int> >::iterator a, int x){
	while(x--)
		a--;
	return a;	
	
}

void merge2(list<pair<int,int> >::iterator it){
	if (it->second==(it+1)->first-1){
		it->second=(it+1)->second;
		li.erase(it+1);
	}
}

int main(){
	long long moves;
	int t,i,j,k,uu,p,v,nq,n;
	cin>>t;
	for (int u=1; u<=t; u++){
		cin>>nq;
		li.clear();
		li.push_back(make_pair(-1000000000,-1000000000));
		li.push_back(make_pair(1000000000,1000000000));
		//n=2;
		moves=0;
		for (uu=0; uu<nq; uu++){
			cin>>p>>v;
			for (it=li.begin(); it!=li.end(); it++){
				if (it->first>p) break;
			}
			if ((it-1)->first<=p && (it-1)->second>=p){
				it--;
				v++;
			}
			else{
				li.insert(it,make_pair(p,p));
				it--;
				if ((it-1)->second==p-1){
					it->first=(it-1)->first;
					li.erase(it-1);
				}
				if ((it+1)->first==p+1){
					it->second=(it+1)->second;
					li.erase(it+1);
				}
			}
			
			
			int cur=0,L=0,R=0;
			while(v>1){
				int lenL=p-it->first;
				int lenR=it->second-p;
				int L0=lenL-L;
				int R0=lenR-R;
				int st=min(L0,R0)+1;
				
				if (L0<=R0){
					moves+=(lenL*(lenL+1)/2);
					it->first--;
					if (it->first-1==(it-1)->second){
						it->first=(it-1)->first;
						li.erase(it-1);
					}
					v--;
					L=0;
				}
				else L+=st;
				
				if (R0<=L0){
					moves+=(lenR*(lenR+1)/2);
					it->second++;
					if (it->second+1==(it+1)->first){
						it->second=(it+1)->second;
						li.erase(it+1);
					}
					v--;
					R=0;
				}
				else R+=st;
		
				cur+=st;
			}
			if (L){
				li.insert(it,make_pair(it->first-1,it->first+L-2));
				merge2(it-2);
				moves+=L*(p-it->first)-L*(L-1)/2;
				it->first+=L;
			}
			if (R){
				li.insert(it+1,make_pair(it->second-R+2,it->second+1));
				merge2(it+1);
				moves+=R*(it->second-p)-R*(R-1)/2;
				it->second-=R;
			}
			moves+=cur;
			if (v==0){
				li.insert(it+1,make_pair(p+1,it->second));
				it->second=p-1;
			}
		}
		printf("Case #%d: %lld\n",u,moves);
	}
	return 0;
}
