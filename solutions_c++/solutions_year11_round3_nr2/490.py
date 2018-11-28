/*
 * B.cpp
 *
 *  Created on: May 22, 2011
 *      Author: yassery
 */


#include<iostream>
#include<cstring>
#include<algorithm>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<sstream>
#include<cstdio>
#include<cmath>
#include<stack>
#include<complex>

using namespace std;

vector<long long> v;
vector<long long> sol;
int main(){
#ifndef ONLINE_JUDGE
	freopen("test.in","rt",stdin);
	freopen("test.txt","wt",stdout);
#endif

	int TC;
	long long L, t, N , C;
	cin>>TC;
	for(int tt=0;tt<TC;tt++){

		cout<<"Case #"<<tt+1<<": ";
		cin>>L>>t>>N>>C;
		v.clear();
		v.resize(C);
		for(int i=0;i<C;i++)
			cin>>v[i];
		sol.clear();
		sol.resize(N);

		int ind = 0 ;
		for(int i=0;i<N;i++){
			sol[i] = v[ind]*2;
			ind = (ind+1)%C;
		}

		for(int i=0;i<N;i++){
			if(t == 0)
			{
				ind = i;
				break;
			}
			if(sol[i] > t)
			{
				sol.push_back(sol[i]-t);
				sol[i] = t;
			}

			t -= sol[i];
		}

		sort(sol.begin()+ind,sol.end());

		long double res = 0.0;
		for(int i=sol.size()-1;i>=0;i--){
			if(L && i > ind){
				res += sol[i]/2.0;
				L--;
			}else
				res += sol[i];
		}
		cout<<(long long)(res+0.9)<<endl;
	}

	return 0;
}
