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
	int num;
	cin>>num;
	f(lp,num){
		int n,k;
		cin>>n>>k;
		char kk[n][n];
		char store[n][n];
		//memset(kk,'.',sizeof(kk));
		f(i,n) f(j,n) kk[i][j]='.';
		char temp;
		f(i,n) f(j,n) { cin>>temp; store[i][j]=temp;}
		f(i,n){
			int count=n-1;
			for(int j=n-1;j>=0;j--){
				temp=store[i][j];
				if(temp!='.'){ kk[count][n-i-1]=temp; count--;}
			}
		}
		bool red=false;
		bool blue=false;
		int temp1;
		int count;
		//f(i,n){ f(j,n) cout<<kk[i][j]<<' '; cout<<endl;}
		f(i,n){
			f(j,n){
				if(kk[i][j]!='.'){
					count=i-1;
					temp1=1;	
					while(count>=0){
						
						
							if(kk[count][j]==kk[i][j]) temp1++;
							else break;
							count--;
					}
					if(temp1>=k){ if(kk[i][j]=='R') red=true; else blue=true;}
					count=i+1;
					temp1=1;
					while(count<=n-1){
							if(kk[count][j]==kk[i][j]) temp1++;
							else break;
							count++;
					}
					if(temp1>=k){ if(kk[i][j]=='R') red=true; else blue=true;}
					count=j+1;
					temp1=1;
					while(count<=n-1){
							if(kk[i][count]==kk[i][j]) temp1++;
							else break;
							count++;
					}
					if(temp1>=k){ if(kk[i][j]=='R') red=true; else blue=true;}
					int count1=i-1;
					temp1=1;
					int count2=j+1;
					while(count1>=0&&count2<=n-1){
						if(kk[count1][count2]==kk[i][j]) temp1++;
						else break;
						count1--;
						count2++;
					}
					if(temp1>=k){ if(kk[i][j]=='R') red=true; else blue=true;}
					 count1=i+1;
					 count2=j+1;
					temp1=1;
					while(count1<=n-1&&count2<=n-1){
						if(kk[count1][count2]==kk[i][j]) temp1++;
						else break;
						count1++;
						count2++;
					}
					if(temp1>=k){ if(kk[i][j]=='R') red=true; else blue=true;}
					}}}
			if(blue&&red) cout<<"Case #"<<lp+1<<": "<<"Both"<<endl;
			else if(blue) cout<<"Case #"<<lp+1<<": "<<"Blue"<<endl;
			else if(red) cout<<"Case #"<<lp+1<<": "<<"Red"<<endl;
			else cout<<"Case #"<<lp+1<<": "<<"Neither"<<endl;			
	}		
}
