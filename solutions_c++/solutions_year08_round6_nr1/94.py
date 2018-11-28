#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <climits>
#include <cmath>
#include <cstdlib>
#include <sstream>
#include <utility>
#include <complex>
#include <valarray>
#include <deque>
using namespace std;

typedef long long ll;
typedef vector<int> vi;

#define RI( i, o ) for(typeof(o.begin()) i= (o).begin(); i!=(o).end(); ++i)
#define RP3( x, y, z ) RP( i, 0, x ) RP( j, 0, y ) RP( k, 0, z )
#define RP( i, s, e ) for(typeof(s) i=(s); i<(e); ++i)
#define R( i, x ) RP(i,0,(x).size())
#define pB push_back

//Problem A
int main()
{
	int N;
	cin >> N;
	
	RP(cs, 1, N+1)
	{
		
		cout << "Case #" << cs << ":" << endl;
		
		int c, h, w, m;
		cin >> c;
		string b,d;
		int lwb=-1;//, swb=10000, swnb=10000, lwnb=-1, lhb=-1, shb=10000, shnb=10000, lhnb=-1;
		vector<pair<int,int> > B;
		vector<int> W;
		int bw=-1, bh=-1;
		RP(i,0,c)
		{
			cin >> h >> w >> b;
			if(b=="NOT") cin >> d;
			if(b=="NOT")
			{
				B.push_back(make_pair(w,h));
				W.push_back(0);
			/*
				swb <?=w;
				lwb >?=w;
				shnb<?=h;
				lhnb>?=h;*/
			}
			else
			{
				B.push_back(make_pair(w,h));
				W.push_back(1);
				bw=w; bh=h;
				/*lwb>?=w;
				swb<?=w;
				lhnb<?=h;
				shnb>?=h;*/
			}
		}
		
		int nb_w_l=-1, nb_w_u=1e9, nb_h_l=-1, nb_h_u=1e9;
		RP(i,0,c)
		{
			w=B[i].first;
			h=B[i].second;
			int isb=W[i];
			int wlt=0, hlt=0, wgt=0, hgt=0;
			if(isb==0){
			RP(j,0,c)
			{
				R(i,B){
				if(W[j] && B[j].first <=w) wlt=1;
				if(W[j] && B[j].first >=w) wgt=1;
				
				}
				
				R(i,B){
					if(W[j] && B[j].second <=h) hlt=1;
					if(W[j] && B[j].second >=h) hgt=1;
				}
			}
			if(wlt && wgt){
				if(h<bh && bh!=-1) nb_h_l>?=h;
				if(h>bh && bh!=-1) nb_h_u<?=h;
			}
			if(hlt && hgt){
				if(w<bw && bw!=-1) nb_w_l>?=w;
				if(w>bw && bw!=-1) nb_w_u<?=w;
			}}
		}
		
		//cout << nb_w_l << " " << nb_w_u << " " << nb_h_l << " " << nb_h_u << endl;
		
		cin >> m;
		RP(i,0,m)
		{
			cin >> h >> w;
			
			int wlt=0, hlt=0, wgt=0, hgt=0;
			
			R(i,B){
				if(W[i] && B[i].first <=w) wlt=1;
				if(W[i] && B[i].first >=w) wgt=1;
				
			}
			
			R(i,B){
				if(W[i] && B[i].second <=h) hlt=1;
				if(W[i] && B[i].second >=h) hgt=1;
			}
			if(wlt && hlt && wgt && hgt) {cout << "BIRD" << endl; continue;}
			
			int t=0;
			
			if(w<=nb_w_l || w>=nb_w_u || h<=nb_h_l || h>=nb_h_u) 
			{cout << "NOT BIRD" << endl; continue;}
			cout << "UNKNOWN" << endl;
		}
	}
	return 0;
}
