#include<cstdio>
#include<algorithm>
#include<vector>
#include<iostream>
using namespace std;
#define ll long long
#define point pair<ll,ll>

vector<point > getPoints(int n, ll A, ll B, ll C, ll D, ll x0, ll y0, ll M){
	vector<point > ret;
	ll X = x0;
	ll Y = y0;
	ret.push_back(point(X,Y));
	for(int i = 1; i <= n-1; ++i){
		X = (((A * X) % M) + B) % M;
		Y = (((C * Y) % M) + D) % M;
		ret.push_back(point(X,Y));
	}
	return ret;
}

bool check(vector<int> v){
	int modX = 0;
	for(int i = 0; i < v.size(); ++i){
		modX += v[i] % 3;
		v[i] /= 3;
	}	
	if (modX % 3 != 0) return false;
	int modY = 0;
	for(int i = 0; i < v.size(); ++i) modY += v[i];
	return modY % 3 == 0;
}

ll brut(vector<point >& v){
	int n = v.size();
	ll ret = 0LL;
	for(int i = 0; i < n; ++i) for(int j = i+1; j <n; ++j) for(int k = j+1; k < n; ++k){
		ll X = v[i].first + v[j].first + v[k].first;
		ll Y = v[i].second + v[j].second + v[k].second;
		if (X % 3 == 0 && Y % 3 == 0) ret++;
	}
	return ret;
}	


int main(){
	int N;
	cin >> N;
	for(int testCase = 1; testCase <= N; ++ testCase){
		ll n;
		ll A,B,C,D,x0,y0,M;
		cin >> n;
	        cin >> A;
		cin >> B;
		cin >> C;
		cin >> D;
		cin >> x0;
		cin >> y0;
		cin >> M;
		vector<point > v = getPoints(n,A % M, B % M, C % M, D % M, x0, y0, M);
		ll t[9];
		//for(int i = 0; i < 3; ++i) for(int j = 0; j < 3; ++j) t[i][j] = 0
		for(int i = 0; i < 9; ++i) t[i] = 0LL;
		for(int i = 0; i < v.size(); ++i){
			ll modX = v[i].first % 3;
			ll modY = v[i].second % 3;
			t[3*modX + modY]++;
		}
		//for(int i = 0; i < 9; ++i) cout << t[i] << " ";
		//cout << endl;
		ll retValue = 0LL;
		for(int i = 0; i < 9; ++i) for(int j = i; j < 9; ++j) for(int k = j; k < 9; ++k){
			vector<int> sol;
			sol.push_back(i);
			sol.push_back(j);
			sol.push_back(k);
			if (!check(sol)) continue;
		
			ll plus = 0LL;
			if (sol[0] == sol[2]) plus = t[sol[0]] * (t[sol[1]]-1) * (t[sol[2]]-2) / 6;
			else if (sol[0] == sol[1]) plus = t[sol[0]] * (t[sol[1]]-1) * t[sol[2]] / 2;
			else if (sol[1] == sol[2]) plus = t[sol[0]] * t[sol[1]] * (t[sol[2]]-1) / 2;
			else plus = t[sol[1]] * t[sol[2]] * t[sol[0]];
			
			/*
			ll aVal = t[sol[0]];
			if (sol[1] == sol[0]) aVal--; 
			if (sol[2] == sol[0]) aVal--;

			ll bVal = t[sol[1]];
			if (sol[1] == sol[2]) bVal--;

			ll plus = aVal * bVal * t[sol[2]];
			if (plus > 0) retValue += plus;
			cout << "(" << sol[0] << " " << sol[1] << " " << sol[2] << ")" << " -- " << "(" << t[sol[1]] << " " << t[sol[2]] << " " << t[sol[3]];
			cout << ")" << plus << endl;
			*/
			retValue += plus;
		}
		cout << "Case #" << testCase << ": " << retValue << endl;
	}

}
