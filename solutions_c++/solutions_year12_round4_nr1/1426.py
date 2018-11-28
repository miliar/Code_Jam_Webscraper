#include <iomanip>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <fstream>
using namespace std;

#define MAX(a,b) (a)>(b)?(a):(b)
#define MIN(a,b) (a)<(b)?(a):(b)
#define INF 2147483647

int N, D;
//map<pair<int,int> ,int> cache[1002];
int cache[10002][10002];
/*
bool solve(int index, int max_dist, vector< pair<int,int> > &dl){
	if(cache[index] > -1) return cache[index]==0?false:true;
	if(index == 0) return true;
//	if(index<N && dl[index].first <= 0) return true;
	bool ret = false;
	int dist;
	if(index == N) dist = D;
	else dist = dl[index].second;
	for(int i = index-1; i>=0; i--){
		if(dl[i].first >= dist && (dl[i].first - dl[i].second) <= max_dist ){
			if(max_dist > dl[index].second - dl[i].second) max_dist = dl[index].second - dl[i].second;
			ret = ret | solve(i,index,dl);
			cache[index] = 1;
			if(ret) return true;
		}
	}
	cache[index] = ret;
	return ret;
}
*/


bool solve(int index, int last_index, vector< pair<int,int> > &dl){
	//if(cache.count(make_pair(max_dist,index)) > -1) return cache[make_pair(max_dist,index)]==0?false:true;
	int max_dist = MIN(dl[index].second, dl[index].first - dl[last_index].first);
	if(dl[index].first + max_dist >= D) return true;
	if(cache[index][last_index]>-1) return cache[index][last_index]==0?false:true;
	
	bool ret = false;

	for(int i = index+1; i<=N; i++){
		if(dl[index].first + max_dist >= dl[i].first)
			ret = ret | solve(i, index,dl);
	}

	if(ret) cache[index][last_index] = 1;
	else cache[index][last_index] = 0;
	return ret;
}

int main(){
	ifstream in("A.in");
	ofstream out("result.txt");
	int TESTS; 
	in >> TESTS;
	//cout.precision(6);
	//cout.setf(ios::fixed,ios::floatfield);   // floatfield set to fixed
	
	//out.precision(6);
	//out.setf(ios::fixed,ios::floatfield);   // floatfield set to fixed
	for(int test = 0; test<TESTS; test++){
		//cache.clear();
		memset(cache,-1,sizeof(cache));
		out << "Case #" << test+1 << ": ";
		cout << "Case #" << test+1 << ": ";
		in >> N;
		vector<pair<int,int> >  dl;
		dl.resize(N+1);
		dl[0].first = 0; dl[0].second = INF;
		//d.resize(N); l.resize(N);
		for(int i = 1; i<=N; i++){
			int d,l;
			in >> d >> l;
			dl[i].first = d;
			dl[i].second = l;
		}
		in >> D;
		bool ret = solve(1,0,dl);
		
		if(ret){
			cout << "YES" << endl;
			out << "YES" << endl;
		}
		else{
			cout << "NO" << endl;
			out << "NO" << endl;
		}
	}
	return 0;
}