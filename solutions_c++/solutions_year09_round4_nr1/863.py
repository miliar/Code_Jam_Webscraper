/*
 * a.cc
 *
 *  Created on: Sep 26, 2009
 *      Author: sandaru1
 */

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
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <cstring>

using namespace std;

typedef vector<int> vi;
vi parseInt(string s) {stringstream ss(s);vi ans;while (!ss.eof()) {int temp; ss >> temp; ans.push_back(temp); } return ans;}
#define COPY(x,y) y.resize(x.size());copy(x.begin(),x.end(),y.begin())
#define pb push_back
#define SWAP(t,x,y) t temp=x;x=y;y=temp;
#define fr(i,s,e) for (int i = int(s); i < int(e); i++)
#define fr2(i,c) for (unsigned int i = 0; i < (c).size(); i++)
#define cl(a,val) memset(a,val,sizeof(a));

#define pi pair<int,int>

int n;
string m[100];
int places[100];

int solve() {
	int count = 0;
	fr(i,0,n) {
		places[i] = 0;
		for(int k=n-1;k>=0;k--) {
			if (m[i][k]=='1') {
				places[i] = k; break;
			}
		}
	}
	fr(i,0,n) {
		if (places[i]<=i) continue;
		fr(k,i+1,n) {
			if (places[k]<=i) {
				int temp = places[i];
				int temp3 = places[k];
				fr(j,i,k) {
					int temp2 = places[j+1];
					places[j+1] = temp;
					temp = temp2;
				}
				places[i] = temp3;
				count+= k-i;
				break;
			}
		}
	}
	return count;
}

int main() {
  int T;
  ifstream fin("input.txt");
  ofstream fout("output.txt");

  fin >> T;

  fr(t,0,T) {
	fin >> n;
	fr(i,0,n) {
		fin >> m[i];
		//cout << m[i] << endl;
	}
	int ans = solve();
    cout << "Case #" << t+1 << ": " << ans << endl;
    fout << "Case #" << t+1 << ": " << ans << endl;
  }

  return 0;
}
