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
 
using namespace std;
typedef long long int lint;
typedef pair<int,int> par;
 
#define sz size
#define pb push_back
#define all(x) (x).begin() , (x).end()
#define sqr(x) (x)*(x)
#define x first
#define y second
#define rep(i,n)  for (int (i)=0;(i)<(int)(n);(i)++)
#define Rep(i,a,n) for (int (i)=(int)(a);(i)<(int)(n);(i)++)

string linhas[105];
int l;


string cars[105];
int tot;
		
pair< pair<double,string>, par > mat[105];
int total;

void doit() {
	stack<int> st;
	int loc = 0;
	
	rep(i,l) {
	
		int j=0;
		while (linhas[i][j] == ' ')
			j++;
		
		if (linhas[i][j] == ')')
			st.pop();
		else {
			if (!st.empty()) {
				if (mat[st.top()].y.x == -1)
					mat[st.top()].y.x = loc;
				else
					mat[st.top()].y.y = loc;					
			}
			
			j++;
			st.push(loc);
			
			mat[loc].y.x = -1;
			mat[loc].y.y = -1;
			
			while (linhas[i][j] == ' ')
				j++;

			int pos = j;
			while ((linhas[i][j] >= '0' && linhas[i][j] <= '9') || linhas[i][j] == '.')
				j++;
			
			sscanf(linhas[i].substr(pos,j-pos).c_str(),"%lf",&mat[loc].x.x);
			
			//cout << i << " " << mat[loc].x.x << " " << pos << " " << j << endl;
			
			while (linhas[i][j] == ' ')
				j++;
			
			if (linhas[i][j] == ')') {
				st.pop();
				mat[loc].x.y = "";
			}
			else {
				pos = j;
				while (linhas[i][j] >= 'a' && linhas[i][j] <= 'z')
					j++;
			
				mat[loc].x.y = linhas[i].substr(pos,j-pos);
			
			}
		
			loc++;
		}
	}


}

int encounter(string c) {
	rep(i,tot)
		if (c == cars[i])
			return 1;
	return 0;
}

double prob(int n) {
	if (mat[n].x.y == "")
		return mat[n].x.x;
	
	if (encounter(mat[n].x.y))
		return mat[n].x.x * prob(mat[n].y.x);
	else
		return mat[n].x.x * prob(mat[n].y.y);

}

int main() {
	int t;
	cin >> t;
	for (int i=1;i<=t;i++) {
		cin >> l;
		
		getline(cin,linhas[0]);
		rep(j,l)
			getline(cin,linhas[j]);
	
	
		total = 0;
		doit();
		
		
		cout << "Case #" << i << ":" << endl;
		
		int a;
		cin >> a;
		rep(j,a) {
			cin >> cars[0];
			
			cin >> tot;
			rep(w,tot)
				cin >> cars[w];
		
			printf("%.7lf\n",prob(0));
		}
		
	}
	return 0;
}

