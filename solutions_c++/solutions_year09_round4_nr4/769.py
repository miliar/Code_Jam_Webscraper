/*
 * d.cc
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

int x[5],y[5],r[5],n;

double length(int x1,int y1,int x2,int y2) {
	int a = (x2-x1)*(x2-x1);
	int b = (y2-y1)*(y2-y1);
	return sqrt(a+b);
}

int main() {
  int T;
  ifstream fin("input.txt");
  ofstream fout("output.txt");

  fin >> T;

  fr(t,0,T) {
	fin >> n;
	fr(i,0,n) {
		fin >> x[i] >> y[i] >> r[i];
	}
	double ans = 0.0;
	if (n==1) {
		ans = r[0];
	} else if (n==2) {
		ans = max(r[0],r[1]);
	} else {
		double a = max((length(x[0],y[0],x[1],y[1]) + r[0] + r[1])/2,(double)r[2]);
		double b = max((length(x[2],y[2],x[1],y[1]) + r[2] + r[1])/2,(double)r[0]);
		double c = max((length(x[0],y[0],x[2],y[2]) + r[0] + r[2])/2,(double)r[1]);
		ans = min(a,min(b,c));
	}
    cout << "Case #" << t+1 << ": " << ans << endl;
    fout << "Case #" << t+1 << ": " << ans << endl;
  }

  return 0;
}
