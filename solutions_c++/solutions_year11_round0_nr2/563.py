#include<iostream>
#include<sstream>
#include<vector>
#include<map>
#include<string>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<queue>
#include<stack>
#include<stdio.h>
#include<stdlib.h>
#define INF (1<<29)
#define EPS (1e-7)
#define two(a) (1<<(a))
#define rep(a,b) for(a=0 ; a<b ; ++a)
#define xrep(a,b,c) for(a=b ; a<c ; ++a)
#define sca(t) scanf("%d",&t)
#define scal(t) scanf("%lld",&t)
typedef long long ll;
using namespace std;

int ch[260][260],op[260][260];
int num[260];

int main(){
	freopen("B-large.in","r",stdin);
	freopen("pbbigout.txt","w",stdout);
	int i,j,k,t,tt,n;
	string in;
	char x,y,z;
	cin >> t;
	for(tt=1 ; tt<=t ; tt++){	
		memset(ch,0,sizeof(ch));
		memset(op,0,sizeof(op));
		cin >> n;
		rep(i,n){
			cin >> x >> y >> z;
			ch[x][y]=ch[y][x]=z;
		}
		cin >> n;
		rep(i,n){
			cin >> x >> y;
			op[x][y]=op[y][x]=1;
		}
		cin >> n >> in;
		memset(num,0,sizeof(num));
		stack<char> st;
		for(i=0 ; i<n ; i++){
			x=in[i];
			if(st.empty()){
				st.push(x);
				num[x]++;
				continue;
			}
			while(!st.empty()){
				y=st.top();
				if(ch[x][y]){
					st.pop();
					num[y]--;
					x=ch[x][y];
					if(st.empty()){
						st.push(x);
						break;
					}
					continue;
				}
				int opx=0;
				for(j='A' ; j<='Z' ; j++){
					if(num[j] && op[x][j]){
						opx++;
						break;
					}
				}
				if(opx==0){
					st.push(x);
					num[x]++;
				}
				if(opx){
					memset(num,0,sizeof(num));
					while(!st.empty()) st.pop();
				}
				break;
			}
		}
		stack<char> sst;
		while(!st.empty()){
			sst.push(st.top());
			st.pop();
		}
		cout << "Case #" << tt << ": [";
		int ox=0;
		while(!sst.empty()){
			if(!ox) ox=1;
			else cout << ", ";
			cout << sst.top();
			sst.pop();
		}
		cout << ']' << endl;
	}
}
