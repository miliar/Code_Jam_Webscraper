#include<iostream>
#include<map>
#include<limits>
#include<vector>

using namespace std;

typedef unsigned long UL;
typedef signed long SL;
typedef unsigned short US;
typedef signed short SS;

const UL inv=numeric_limits<UL>::max();

struct trip
{
	bool atob;
	UL s,t;
	trip(){}
	trip(bool atob_, UL s_, UL t_) : atob(atob_), s(s_), t(t_) {}
};

ostream &operator<<(ostream &os, const trip &a)
{
	return os<<(a.atob?"a to b: ":"b to a: ")<<(a.s/60)<<":"<<(a.s%60)<<" "<<(a.t/60)<<":"<<(a.t%60);
}

struct trip_less_t : public binary_function<trip, trip, bool>
{
	bool operator()(const trip &a, const trip &b){return (a.t < b.t) || ( (a.t==b.t) && (a.s < b.s) ) ; }
};

struct trip_less_s : public binary_function<trip, trip, bool>
{
	bool operator()(const trip &a, const trip &b){return (a.s < b.s) || ( (a.s==b.s) && (a.t < b.t) ) ; }
};

int main()
{
	UL tests;
	cin>>tests;
	for(UL tt=1; tt<=tests; ++tt)
	{
		UL T, na, nb;
		cin>>T>>na>>nb;
		vector<trip> trips(na+nb);
		for(UL i=0; i<na+nb; ++i)
		{
			UL h1, m1, h2, m2;
			char tmp;
			cin>>h1>>tmp>>m1;
			cin>>h2>>tmp>>m2;
			trips[i]=trip(i<na, 60*h1+m1, 60*h2+m2);
		}
		sort(trips.begin(), trips.end(), trip_less_t());
		UL ansa=0, ansb=0;
		vector<char> matched(na+nb, false); //use as vector<bool>
		for(UL i=0; i<na+nb; ++i)
		{
			bool startnew=true;
			for(SL j= SL(i) - 1; j>=0; --j)
				if(!matched[j] && (trips[j].atob != trips[i].atob) && trips[j].t + T <= trips[i].s)
				{
					matched[j]=true;
					startnew=false;
					break;
				}
			//cerr<<trips[i]<<boolalpha<<"  startnew="<<startnew<<'\n';
			if(startnew)
				++(trips[i].atob ? ansa : ansb);
		}
		cout<<"Case #"<<tt<<": "<<ansa<<' '<<ansb<<'\n';
	}
	
}
