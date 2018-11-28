#include <iostream>
#include <iomanip>
#include <ctime>
#include <numeric>
#include <vector>
#include <algorithm>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <sstream>
#include <map>
#include <set>
#include <cstdio>
#include <queue>
#include <list>
#include <stack>
#define ll long long
#define vi vector<int>
#define mp make_pair
#define oo (1<<30)
#define ones(x) __builtin_popcount(x)
#define All(v) (v).begin(),(v).end()
#define rAll(v) (v).rbegin(),(v).rend()
#define x first
#define y second
#define pb push_back
#define eps (1e-9)
#define MAX 2400
using namespace std;

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define INF 1<<28

double W[103],OWP[103],OOWP[103];
int n;
string G[103];
double WP(int u,int v){
      double res = 0.0;
      int N = 0, w = 0;
      for(int i = 0;i < n; i++){
            if(G[v][i]!='.' && i!=u){
               N++; if(G[v][i]=='1') w++;   
            }
      }
      return w/(double)N;

   }
int main(){
	int runs;
	cin>>runs;
	
	for(int r=1;r<=runs;r++){
		cin>>n;
		for(int i=0;i<n;i++) cin>>G[i];
		
		for(int i = 0; i < n; i++){
			int w=0, N=0;
			for(int j = 0; j < n; j++){
				if(G[i][j] != '.'){
					N++;
					if(G[i][j] == '1')
						w++;
				}
			}
			W[i] = w /(double) N;
		}

		for(int i=0;i<n;i++){
			
			double avg=0.0;
			int N=0;
			for(int j = 0; j < n; j++){
				if(G[i][j] != '.'){
					N++; avg += WP(i,j);
				}
			}
			OWP[i] = avg/(double)N;
		}
		for(int i = 0;i < n; i++){
			double avg=0.0;
			int N=0;
			for(int j = 0;j < n;j++){
				if(G[i][j]!='.'){
					N++;avg+=OWP[j];
				}
			}
			OOWP[i]=avg/(double)N;
		}
		printf("Case #%d:\n",r);
		for(int i = 0;i < n; i++){
			double RPI = 0.25 * W[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
			printf("%.12lf\n",RPI);
		}
	}

	return 0;
}
