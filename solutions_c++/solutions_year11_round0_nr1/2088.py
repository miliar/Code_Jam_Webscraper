#include<iostream>
#include<vector>
#include "math.h"
using namespace std;
int max(int a, int b)
{
	if(a > b) 
		return a;
	else
		return b;
};
struct IndexButtonPair
{
	int index;
	int button;
	IndexButtonPair(int c, int i)
	{
		index = c;
		button = i;
	}
};

int main()
{
	int T;
	cin >> T;
	for(int i=0;i<T;++i)
	{
		int N;
		cin >> N;
		vector<IndexButtonPair> Orange, Red;
		for(int j=1;j<=N;++j)
		{
			char col;
			int buttonNo;
			cin >> col;
			cin >> buttonNo;
			if(col == 'O')
			{
				Orange.push_back(IndexButtonPair(j,buttonNo));		
			}
			else if(col == 'B')
			{
				Red.push_back(IndexButtonPair(j,buttonNo));
			}
			else
			{
				//error;
			}
		}
		int oi,ri,dri,doi;
		unsigned long long int time;
		oi = 0; ri = 0; time = 0;
		if(Orange.size()) {doi = Orange[oi].button - 1;}; // initial button for orange and red bot is 1 
		if(Red.size()) {dri = Red[ri].button - 1;};
		int Rn, On;
		Rn = Red.size();  On = Orange.size();
		while(ri < Rn && oi < On)
		{
			if(Red[ri].index < Orange[oi].index)
			{
				time += dri + 1;
				doi = max(doi - dri - 1,0);
				ri++;
				if( ri < Rn) 
				{
					dri = abs(Red[ri].button - Red[ri-1].button);
				} // update dist to be traveled next for Red
				else {dri = 0;};
			}
			else if(Red[ri].index > Orange[oi].index)
			{
				time += doi + 1;
				dri = max(dri - doi - 1,0);
				oi++;
				if(oi < On) {doi= abs(Orange[oi].button - Orange[oi-1].button);} // update dist to be traveled next for Red
				else {doi = 0;};
			}
		}
		while(ri < Rn)
		{
			time += dri + 1;
			ri++;
			if(ri< Rn) 
			{
				dri = abs(Red[ri].button - Red[ri-1].button);
			}
			else {dri = 0;};
		}
		while(oi < On)
		{
			time += doi + 1;
			oi++;
			if(oi < On) 
			{
				doi = abs(Orange[oi].button - Orange[oi-1].button);
			}
			else {doi = 0;};
		}
		cout << "Case #"<<i+1<<": "<<time<<"\n";
	}
}