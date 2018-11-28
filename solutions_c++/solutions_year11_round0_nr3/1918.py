/*	SURENDRA KUMAR MEENA	*/
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
#include <queue>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <ctime>
using namespace std;
#define R(i,m,n)	for(int i=m;i>=n;i--)
#define FF(i,m,n)	for(int i=m;i<n;i++)
#define F(i,n)	FF(i,0,n)
#define VI vector<int>
#define PB push_back

int main(){
	int t;
	cin>>t;
	FF(kase,1,t+1){
		cout<<"Case #"<<kase<<": ";
		int n;
		cin>>n;
		VI v(n);
		int ans=0,s=0;
		F(i,n){
			cin>>v[i];
			s^=v[i];
			ans+=v[i];
		}
		if(s==0){
			sort(v.begin(),v.end());
			ans-=v[0];
		}
		if(s)				cout<<"NO\n";
		else				cout<<ans<<endl;
	}
	return 0;
	/*
	   with all subsets :
		int n;
		cin>>n;
		VI v(n);
		F(i,n)	cin>>v[i];
		bool possible=false;
		int ans=0;
		FF(mask,1,(1<<n)-1){
			int s1=0,s2=0;
			int sum1=0,sum2=0;
			F(i,n){
				if(mask & (1<<i)){
					s1^=v[i];
					sum1+=v[i];
				}
				else{
					s2^=v[i];
					sum2+=v[i];
				}
			}
			if(s1==s2){
				possible = true;
				ans>?=max(sum1,sum2);
			}
		}
		if(!possible)	cout<<"NO\n";
		else				cout<<ans<<endl;
	*/
}
