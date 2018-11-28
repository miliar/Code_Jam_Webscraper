#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int readmin()
{
	int h,m;
	cin>>h;
	char x;
	while(cin>>x,x!=':'){}
	cin>>m;
	return h*60+m;
	
}


int main()
{

int cases;
cin>>cases;

	for(int i=0;i<cases;i++)
	{
		int bet;
		cin>>bet;		
		int x;int y;
		cin>>x>>y;
		vector<pair<int,bool> > tx;

		vector<pair<int,bool> > ty;

		for(int ix=0;ix<x;ix++)
		{
			int a=readmin();
			int b=readmin();
			tx.push_back(make_pair(a,true));
			ty.push_back(make_pair(b,false));
			
		}
		for(int iy=0;iy<y;iy++)
		{
			int a=readmin();
			int b=readmin();
			ty.push_back(make_pair(a,true));
			tx.push_back(make_pair(b,false));
			
		}
		sort(tx.begin(),tx.end());
		sort(ty.begin(),ty.end());
		queue<int> cx,cy;
		
		int nx,ny;
		nx=0;ny=0;
		for(int ix=0;ix<tx.size();ix++)
		{
			if(tx[ix].second==false) cx.push(tx[ix].first);
			if(tx[ix].second==true)
			{
				if(!cx.empty() && cx.front()<=tx[ix].first-bet)
					cx.pop();
				else
					nx++;
			}
		}
		for(int iy=0;iy<ty.size();iy++)
		{
			if(ty[iy].second==false) cy.push(ty[iy].first);
			if(ty[iy].second==true)
			{
				if(!cy.empty() && cy.front()<=ty[iy].first-bet)
					cy.pop();
				else
					ny++;
			}
		}
		cout<<"Case #"<<i+1<<": "<<nx<<" "<<ny<<endl;
		
	}
}