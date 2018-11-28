#include<iostream>
#include<vector>
#include<queue>
#include<set>
using namespace std;

priority_queue<pair<int,vector<int> > > pq;
pair<int,vector<int> > crnt;
vector<int> ar,temp;
set<vector<int> > udah;
int T,tc,N,i,last,j,val,heur,theu,lang;
char a;

int main() {
	scanf("%d",&T);
	for(tc=1;tc<=T;tc++) {
		scanf("%d",&N);
		ar.clear();
		for(i=0;i<N;i++) {
			last=0;
			getchar();
			for(j=0;j<N;j++) {
				scanf("%c",&a);
				if(a=='1') last=j;
			}
			ar.push_back(last);
			//cout<<"last: "<<last<<endl;
		}
		udah.clear();
		val=0;
		for(i=0;i<N;i++) {
			if(ar[i]>i) {
				val+=ar[i]-i;
			}
		}
		while(!pq.empty()) pq.pop();
		pq.push(make_pair(-val,ar));
		while(!pq.empty()) {
			crnt=pq.top();
			pq.pop();
			val=-crnt.first;
			ar=crnt.second;
			heur=0;
			if(udah.find(ar)!=udah.end()) continue;			
			for(i=0;i<N;i++) {
				if(ar[i]>i) heur+=ar[i]-i;
			}
			lang=val-heur;
			theu=heur;
			if(heur==0) {
				printf("Case #%d: %d\n",tc,val);
				break;
			}
			//cout<<"lang: "<<lang<<endl;
			//cout<<"heur: "<<heur<<endl;
			//cout<<"ar: "<<endl;
			//for(i=0;i<N;i++) cout<<ar[i]<<" ";
			//cout<<endl;
			//getchar();
			udah.insert(ar);
			for(i=0;i<N-1;i++) { //i yg diswap
				temp=ar;
				theu=heur;
				//if(ar[i]<=i&&ar[i+1]<=(i+1)) continue;
				//cout<<"i: "<<i<<endl;
				if(ar[i]>i)	theu-=(ar[i]-i);
				if(ar[i+1]>i) theu-=(ar[i+1]-(i+1));
				temp[i]=ar[i+1]; temp[i+1]=ar[i];
				if(temp[i]>i) theu+=(temp[i]-i);
				if(temp[i+1]>i) theu+=(temp[i+1]-(i+1));
				if(udah.find(temp)!=udah.end()) continue;
				pq.push(make_pair(-(theu+lang+1),temp));
			}
		}
	}
}
