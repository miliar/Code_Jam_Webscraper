#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#define f(i,x) for(int i=0;i<x;i++)
#define fo(i,x,y) for(int i=x;i<y;i++)
#define pb push_back
#define vi vector<int>
#define all(x) x.begin(),x.end()
#define vs vector<string>
#define ss stringstream
#define ll long long
using namespace std; 
int main(){
	freopen("in.txt","r",stdin);
	freopen("out1.txt","w",stdout);
	int loop;
	cin>>loop;
	f(j,loop){
		int tillnow_o=0,tillnow_b=0,flag,t_o,t_b,now_o=1,now_b=1,p;
		char c;
		int tot=0;
		int n;
		cin>>n;
		f(i,n){
			cin>>c;cin>>p;
			if(i==0){ if(c=='O') flag=0; if(c=='B') flag=1;}
			if(c=='O'){
				t_o=abs(p-now_o)+1;
				if(flag==1){
					if(tillnow_b>=t_o){
						tot++;
						tillnow_o=1;
					}
					else{tot+=t_o-tillnow_b; tillnow_o=t_o-tillnow_b;}}
				else{
					tot+=t_o;
					tillnow_o+=t_o;
				}
				flag=0;now_o=p;
			}
			else if(c=='B'){
				t_b=abs(p-now_b)+1;
				if(flag==0){
					if(tillnow_o>=t_b){
						tot++; tillnow_b=1;
					}
					else{ tot+=t_b-tillnow_o; tillnow_b=t_b-tillnow_o;}
				}
				else {
					tot+=t_b;tillnow_b+=t_b;}
				flag=1;now_b=p;
			}
		}
		cout<<"Case #"<<j+1<<": "<<tot<<endl;
	}
}
					
