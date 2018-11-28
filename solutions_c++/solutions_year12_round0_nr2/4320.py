#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
#include <sstream>
#include <queue>

using namespace std;

#define ALL(v) (v.begin(),v.end())
#define sz(x) ((int)(x).size())
#define pb push_back
typedef vector<int> vi;

const int INF (0x3f3f3f3f);

int dx[] = {1,0,-1,0}, dy[] = {0,1,0,-1};


typedef long long LL;

ifstream fin ("B-small-attempt0(1).in");
ofstream fout ("B-small-attempt0.out");

map < pair<pair<int,int>,int>,int > mp;

vector < pair<pair<int,int>,int> > V;
vector < vector< pair<pair<int,int>,int> > > vv;

int main (){
	int arr[3];
	int T,N,S,P;
	fin >> T;
	for (int i=0;i<T;i++){
		fin >> N >> S >> P;
		vv.clear();
		mp.clear();
		int s=0;
		int c=0;
		for (int f=0;f<N;f++) {
			V.clear();
			mp.clear();
			fin >> s;
			for (int j=0;j<=10;j++){
				if (j <= s){
					for (int k=0;k<=10;k++){
						if (k+j <= s && (abs(j-k)<=2)){
							for (int l=0;l<=10;l++){
								if (l+j+k == s && (abs(l-k)<=2) && (abs(l-j)<=2)){
									arr[0] = j , arr[1] = k, arr[2] = l;
									sort (arr,arr+3);
									if (mp[make_pair(make_pair(arr[0],arr[1]),arr[2])] == 1) continue;
									mp[make_pair(make_pair(arr[0],arr[1]),arr[2])] = 1;
									//if (max(max(j,k),l) >= P){
										V.push_back(make_pair(make_pair(j,k),l));
									//}
									cout << j << " " << k << " " << l << endl;
								}
							}
						}
					}
				}
			}
			if (V.size()!=0)vv.push_back(V);
		}
		int mx = 0;
		vector < vector< pair<pair<int,int>,int> > > vx = vv;
		for (int p=0;p<2;p++){
			if (p == 0) sort (vv.rbegin(),vv.rend());
			else{
				vv = vx;
				sort (vv.begin(),vv.end());
			}
			int x = vv.size();
			int r=0,ans=0;
			for (int m=0;m<x;m++){
				for (int z=0;z<vv[m].size();z++){
					int s1,s2,s3;
					s1 = vv[m][z].first.first;
					s2 = vv[m][z].first.second;
					s3 = vv[m][z].second;
					if ( abs(s1-s2) == 2 || abs(s1-s3) == 2 || abs (s2-s3) == 2 ) {r++; break;}
				}
			}


			int del=0 ; 
			int rt=abs(S-r);
			if (S == r) {ans = x; goto end;}
			else {
				for (int m=0;m<vv.size();m++){
						for (int z=0;m<vv.size()&&z<vv[m].size();z++){
						int s1,s2,s3;
						s1 = vv[m][z].first.first;
						s2 = vv[m][z].first.second;
						s3 = vv[m][z].second;
						if ( abs(s1-s2) == 2 || abs(s1-s3) == 2 || abs (s2-s3) == 2 ) {
							vv[m].erase(vv[m].begin()+z,vv[m].begin()+z+1);
							if (vv[m].size() == 0) vv.erase(vv.begin()+m,vv.begin()+m+1);
							del++;
							if (del == rt) {
								ans = vv.size(); 
								goto end;
							}
						}
					}
				}
			}
			end:
			for (int m=0;m<vv.size();m++){
					for (int z=0;m<vv.size()&&z<vv[m].size();z++){
					int s1,s2,s3;
					s1 = vv[m][z].first.first;
					s2 = vv[m][z].first.second;
					s3 = vv[m][z].second;
					if ( max(max(s1,s2),s3) < P ) {
						vv[m].erase(vv[m].begin()+z,vv[m].begin()+z+1);
						if (vv[m].size() == 0) vv.erase(vv.begin()+m,vv.begin()+m+1);
						z--;
					}
				}
			}
			mx = max (mx,(int)vv.size());
		}

		fout << "Case #" << i+1 << ": " << mx << endl;
	}
	return 0;
}