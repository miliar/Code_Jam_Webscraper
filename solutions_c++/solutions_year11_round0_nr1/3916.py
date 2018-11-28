#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int nCasos;
	cin>>nCasos;
	
	for(int caso=1; caso<=nCasos; caso++)
	{
		int N;
		cin>>N;
		
		vector < pair <int, int> > P1, P2;
		int i1 = 0, i2 = 0;
		
		for(int i=0; i<N; i++)
		{
			string s;
			int p;
			cin>>s>>p;
			
			if(s=="O") P1.push_back(make_pair(p, i));
			else P2.push_back(make_pair(p, i));
		}
		
		
		int p1=1, p2=1, T = 0;
		
		while(i1 != P1.size() || i2 != P2.size())
		{
			if(i1 == P1.size())
			{
				for(int i=i2; i<P2.size(); i++)
				{
					T += abs(P2[i].first - p2) + 1;
					p2 = P2[i].first;
				}
				i2 = P2.size();
				break;
			}
			
			if(i2 == P2.size())
			{
				for(int i=i1; i<P1.size(); i++)
				{
					T += abs(P1[i].first - p1) + 1;
					p1 = P1[i].first;
				}
				i1 = P1.size();
				break;
			}
			
			int t1 = abs(P1[i1].first - p1);
			int t2 = abs(P2[i2].first - p2);
			int mint = min(t1, t2);
			
			if(t1 != 0 && t2 != 0)
			{
				T += mint;
				p1 += mint * (P1[i1].first - p1) / abs(P1[i1].first - p1);
				p2 += mint * (P2[i2].first - p2) / abs(P2[i2].first - p2);
			}
			else
			{
				if(P1[i1].second < P2[i2].second)
				{
					T += abs(P1[i1].first - p1) + 1;
					p1 = P1[i1].first;
					i1++;
					
					if(P2[i2].first != p2) p2 += (P2[i2].first - p2) / abs(P2[i2].first - p2);
				}
				else
				{
					T += abs(P2[i2].first - p2) + 1;
					p2 = P2[i2].first;
					i2++;
					
					if(P1[i1].first != p1) p1 += (P1[i1].first - p1) / abs(P1[i1].first - p1);
				}
			}
		}
		cout<<"Case #"<<caso<<": "<<T<<endl;
	}
	
	return 0;	
}
