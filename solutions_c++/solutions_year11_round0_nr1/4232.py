#include<iostream>
#include<vector>

#define REPEAT(i,a,b) for(int i=a;i<b;++i)
#define REP(i,n) REPEAT(i,0,n)
#define RREP(i,n) for(int i=n-1;i>=0;--i)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define sz size()
#define mkp make_pair

using namespace std;

typedef pair<int,int> pii;
typedef vector<pii> vp;



int main()
	{
	int T;
	cin>>T;
	REP(j,T)
		{
		int N,t;
		char c;
		cin>>N;
		vp O,B;
		REP(i,N){
			cin>>c>>t;
			if(c=='O') O.pb(mkp(i+1,t));
			else B.pb(mkp(i+1,t));
			}
		//REP(i,N) cout<<O.first<<" "<<O.second<<" "<<B.first<<" "<<B.second<<endl;
		int i=0,time=0,ocnt=0,bcnt=0,mo=1,mb=1;
		while(i<N){
			if(!O.empty() && O[ocnt].first == i+1){	//O's move
				if(mo < O[ocnt].second){	//O needs to be moved
					mo++;
					time++;
					if(!B.empty() && mb < B[bcnt].second)	mb++;
					else if(!B.empty() && mb > B[bcnt].second) mb--;
					}
				else if(mo > O[ocnt].second){
					mo--;
					time++;
					if(!B.empty() && mb < B[bcnt].second)	mb++;
					else if(!B.empty() && mb > B[bcnt].second) mb--;
					}
				else if(mo == O[ocnt].second){
					time++;
					ocnt++;
					i++;
					if(!B.empty() && mb < B[bcnt].second){	//B needs to be moved
						mb++;
						}
					else if(!B.empty() && mb > B[bcnt].second) mb--;
					}
				//cout<<"in O:"<<time<<" "<<mo<<" "<<mb<<endl;				
				}
			if(!B.empty() && B[bcnt].first == i+1){//cout<<"yes ";
				if(mb < B[bcnt].second){
					mb++;
					time++;//cout<<"yes ";
					if(!O.empty() && mo < O[ocnt].second) mo++;
					else if(!O.empty() && mo > O[ocnt].second) mo--;
					}
				else if(mb > B[bcnt].second){
					mb--;
					time++;
					if(!O.empty() && mo < O[ocnt].second) mo++;
					else if(!O.empty() && mo > O[ocnt].second) mo--;
					}
				else if(mb == B[bcnt].second){
					time++;
					bcnt++;
					i++;
					if(!O.empty() && mo < O[ocnt].second) mo++;
					else if(!O.empty() && mo > O[ocnt].second) mo--;
					}
				//cout<<"in B:"<<time<<" "<<mo<<" "<<mb<<endl;
				}
			
			}
		cout<<"Case #"<<j+1<<": "<<time<<endl;
		}
	//cin>>T;
	return 0;
	}
	
