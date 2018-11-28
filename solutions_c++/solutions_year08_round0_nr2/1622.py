#include<iostream>
#include<vector>
#include<string>
#include<queue>
#include<sstream>
#include<map>
#include<stack>
#include<set>
#include<cmath>
using namespace std;
#define PB push_back
#define vi vector<int>
#define vvi vector<vi>
#define LL long long
#define all(v) v.begin(),v.end()
#define pii pair<int,int>
#define pdi pair<double,int>
#define MP make_pair
#define GI ({int t ; scanf("%d",&t);t;})
#define INF 200000000
struct Time{
	int h,m;
	Time(){}
	Time(int a,int b){h=a;m=b;}
	bool operator<(const Time& t) const{
		if(h!=t.h) return h<t.h;
		return m<t.m;
	}
	bool operator==(const Time& t) const{
		return (h==t.h && m==t.m);
	}
	Time operator+(const Time& t) const{
		Time ret;
		ret.h=h+t.h;
		ret.m=m+t.m;
		if(ret.m>=60){
			ret.m-=60;
			ret.h++;
		}
		return ret;
	}
};	
Time get(string s)
{
	for(int i=0;i<s.size();i++)
		if(s[i]==':') s[i]=' ';
	stringstream ss;
	ss<<s;
	int h,m;
	ss>>h>>m;
	return Time(h,m);
}
int main()
{
	int t=GI;
	for(int kase=1;kase<=t;kase++)
	{
		int T=GI,na=GI,nb=GI;
		vector < pair<Time,Time> > A,B;
		string s;
		for(int i=0;i<na;i++){
			cin>>s;
			Time t1=get(s);
			cin>>s;
			Time t2=get(s);
			A.PB(MP(t1,t2));
		}	
		for(int i=0;i<nb;i++){
			cin>>s;
			Time t1=get(s);
			cin>>s;
			Time t2=get(s);
			B.PB(MP(t1,t2));
		}
		sort(all(A)); sort(all(B));
		int ca=0,cb=0;
		vector<bool> doneA(na,0),doneB(nb,0);
		vector< pair<Time,int> > t;
		int x=0,y=0,resA=0,resB=0;
		while(x<A.size() || y<B.size())
		{
			int side;
			//cout<<A[x].second.h<<" "<<A[x].second.m<<endl;
			if(x<A.size() && y<B.size()){
				if(A[x]<=B[y])
					side=1;
				else
					side=2;
			}
			else if(x<A.size())
				side=1;
			else if(y<B.size())
				side=2;
			bool ok;
			if(side==1){
				ok=0;
				for(int j=0;j<t.size();j++)
					if(t[j].second==1 && (t[j].first<A[x].first || t[j].first==A[x].first)){
						t[j].first=A[x].second+Time(0,T);
						t[j].second=2;
						x++; ok=1;
						break;
					}
				if(!ok){
					t.PB(MP(A[x].second+Time(0,T),2));
					x++; resA++;
					//cout<<t.back().first.h<<":"<<t.back().first.m<<" "<<t.back().second<<endl;
				}	
			}			
			if(side==2){
				ok=0;
				for(int j=0;j<t.size();j++)
					if(t[j].second==2 && (t[j].first<B[y].first || t[j].first==B[y].first)){
						t[j].first=B[y].second+Time(0,T);
						t[j].second=1;
						y++; ok=1;
						break;
					}
				if(!ok){
					t.PB(MP(B[y].second+Time(0,T),1));
					y++; resB++;
				}
			}			
		}
		cout<<"Case #"<<kase<<": "<<resA<<" "<<resB<<endl;
	}
}