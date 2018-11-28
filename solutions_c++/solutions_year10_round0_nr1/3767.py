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
	int test;
	cin>>test;
	int n,k;
	f(i,test){
		cin>>n>>k;
		ll temp=(ll)pow(2,n);
		ll temp1=temp;
		temp1--;
		if(k>temp){
			k=k%temp;
		}
		if(k==temp1) cout<<"Case #"<<i+1<<": "<<"ON"<<endl;
		else cout<<"Case #"<<i+1<<": "<<"OFF"<<endl;
	}	
}
