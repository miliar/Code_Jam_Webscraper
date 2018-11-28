#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <list>
#include <set>
#include <numeric>
#include <queue>
#include <stack>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
using namespace std;
typedef long long LL;

struct SCOPE
{
	char transform[256][256];
	bool opposed[256][256];
	int run(int Case)
	{
		int C;
		cin >> C;
		for (int i=0;i<C;i++){
			char a,b,c;
			cin>>a>>b>>c;
			transform[a][b]=c;
			transform[b][a]=c;
		}
		int D;
		cin >> D;
		for(int i=0;i<D;i++){
			char a,b;
			cin>>a>>b;
			opposed[a][b]=true;
			opposed[b][a]=true;
		}

		vector<char> vec;
		int N;
		cin >> N;
		for(int i=0;i<N;i++){
			char a;
			cin >> a;
			bool transformed=false;
			while (vec.size()&&transform[vec.back()][a]){
				a=transform[vec.back()][a];
				vec.pop_back();
				transformed=true;
			}
			bool opp=false;
			if(!transformed){
				for(int i=0;i<vec.size();i++){
					if(opposed[a][vec[i]]){
						vec.clear();
						opp=true;
						break;
					}
				}
			}
			if(!opp){
				vec.push_back(a);
			}
		}

		cout << "Case #" << Case << ": [";
		for(int i=0;i<vec.size();i++){
			if(i){
				cout << ", ";
			}
			cout << vec[i];
		}
		cout << "]\n";
		return 0;
	}
};
int main() {
	int n;
	cin >> n;
	int Case=1;
	for (int i=0;i<n;i++) {
		SCOPE* pSCOPE = new SCOPE();
		if(pSCOPE->run(i+1)){
			return 0;
		}
		Case++;
		delete pSCOPE;
	}
}
