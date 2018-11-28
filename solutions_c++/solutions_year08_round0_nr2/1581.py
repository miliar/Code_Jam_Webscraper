#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <algorithm>
using namespace std;

struct event
{
	int type; // 0-> arr , 1 -> dep
	int time; // in minates
	int station; // 0->A , 1->B
	event(int ty,int ti,int st) : type(ty) , time(ti) , station(st) {}
	bool operator < (const event & e) const
	{
		if ( time == e.time )
			return type < e.type ;
		return time < e.time ;
	}
};

int con ( string  temp )
{
	string min(temp.substr(0,2));
	string sec(temp.substr(3,2));
	stringstream ss(min);
	int imin;
	ss>>imin;
	stringstream sss(sec);
	int isec;
	sss>>isec;
	return imin*60+isec;
}

vector <event> events;

int main () 
{
	freopen ("B-large.in","rt",stdin);
	freopen ("B-large.out","wt",stdout);
	int i,ncase , cc = 1;
	cin>>ncase;
	
	while (cc<=ncase )
	{
		int t , na , nb;
		cin >> t >> na >> nb;
		string temp;
		
		for ( i = 0 ; i < na ; i ++ )
		{
			cin >> temp;
			events.push_back(event(1,con(temp),0));
			cin >> temp;
			events.push_back(event(0,con(temp)+t,1));
		}
		for ( i = 0 ; i < nb ; i ++ )
		{
			cin >> temp;
			events.push_back(event(1,con(temp),1));
			cin >> temp;
			events.push_back(event(0,con(temp)+t,0));
		}

		sort (events.begin() , events.end());

		int ia = 0 , ib = 0 , ra = 0 , rb = 0;

		for ( i =  0 ; i < events.size () ; i ++ )
		{
			if ( events[i].type == 0 )
			{
				if ( events[i].station == 0 )
					ia++;
				else if (events[i].station == 1 )
					ib++;
			}
			else if ( events[i].type == 1 )
			{
				if ( events[i].station == 0 )
				{
					if ( !ia )
						ra++;
					else
						ia--;
				}
				else if (events[i].station == 1 )
				{
					if ( !ib )
						rb++;
					else
						ib--;
				}
			}

		}
		cout <<"Case #"<<cc<<": "<<ra<<" "<<rb<<endl;
		cc++;
		events.clear();
	}
	return 0;
}