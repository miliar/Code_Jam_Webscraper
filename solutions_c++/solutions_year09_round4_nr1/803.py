#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <queue>
#include <algorithm>
#include <list>
#include <sstream>

using namespace std;

#define DEBUG false

#define f(i,j,k) for(int i = j; i < k; i++)
#define fd(i,j,k) for(int i = j; i >= k; i--)
#define pb push_back
#define sz size
#define all(a) (a).begin(), (a).end()
#define vs vector<string>
#define vi vector<int>
#define deb(x...)  if(DEBUG) printf(x)

template <typename T>
void printv(vector<T>& v){
	if(!DEBUG) return;
	int n = v.sz();
	printf("[");
	for(int i = 0; i < n; i++){
		cout << v[i] << ", ";
	}
	printf("]\n");
}

vs split(const string& s, const string delim){
	vs res;
	string at;
	int n = s.sz();

	for(int i = 0; i < n; i++){
		char c = s[i];
		if(delim.find(c) != string::npos){
			if(at.sz() > 0){
				res.pb(at);
			}
			at = "";
		} else {
			at.pb(c);
		}
	}
	if(at.sz() > 0){
		res.pb(at);
	}

	return res;
}

template <typename S, typename T>
T convert(const S var){
	T res;
	stringstream ss;
	ss << var;
	ss >> res;

	return res;

}
int main(void){
	int T, N;

	scanf("%d\n", &T);
	for(int cas = 0; cas < T; cas++){
		cin >> N;
		vs vec;
		f(i,0,N){
			string s;
			cin >> s;
			vec.pb(s);
		}
		vector<int> veci = vector<int>(vec.sz());
		for(int i = 0; i < N; i++){
			for(int j = vec[i].sz()-1; j >= 0; j--){
				if(vec[i][j] == '1'){
					veci[i] = j;
					break;
				}

			}
		}

		int ct = 0;
		f(i,0,N){
			if(veci[i] > i){
				deb("%d acima\n",i);
				f(j,i+1,N){
					if(veci[j] <= i){
						deb("sobe %d\n",j);
						int k = j;
						while(k > i){
							string s = vec[k];
							vec[k] = vec[k-1];
							vec[k-1] = s;
							int ii =  veci[k];
							veci[k] = veci[k-1];
							veci[k-1] = ii;
							ct++;
							k--;
						}
						break;
					}
				}
			}

		}

		printv(vec);
		printv(veci);

		printf("Case #%d: %d\n", cas+1,ct);
	}

	return 0;
}
