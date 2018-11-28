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
typedef long long int LL;
#define ALL(s) (s).begin(),(s).end()
#define R(i,m,n)	for(int i=m;i>=n;i--)
#define FF(i,m,n)	for(int i=m;i<n;i++)
#define F(i,n)	FF(i,0,n)
#define VI vector<int>
#define PB push_back
#define CLR(s,v) memset(s,v,sizeof(s))
string to_str(LL x){ ostringstream o;o<<x;return o.str();}
LL to_int(string s){ istringstream st(s); LL i;	st>>i;return i;}
#define FR(it,t) for(typeof(t.begin()) it=t.begin(); it!=t.end(); ++it)
typedef pair<int,int> PI;
#define MP(x,y) make_pair(x,y)
#define f first
#define s second
#define VP vector<PI>
#define S(t)	scanf("%d",&t)
int n,K;
string b[100],bb[100];

int main(){
	int t;
	int cas=0;
	cin>>t;
	while(t--){
		cas++;
		cin>>n>>K;
		F(i,n){
			cin>>b[i];
			bb[i]=b[i];
		}
		F(i,n){
			F(j,n){
				bb[i][j]=b[n-j-1][i];
			}
		}
		
	//	F(i,n)	cout<<bb[i]<<endl;
		
		F(j,n){
			int i=n-1;
			while(i>=0){
				if(bb[i][j]!='.'){
					i--;
					continue;
				}
				int k=i;
				while(k>=0 && bb[k][j]=='.')	k--;
				if(k<0)	break;
		//		cout<<j<<" "<<i<<" "<<k<<endl;
				swap(bb[k][j],bb[i][j]);
				i--;
			}
		}
	//	cout<<endl;
	//	F(i,n)	cout<<bb[i]<<endl;

		bool red=false,blue=false;
		F(i,n){
			F(j,n){
				if(bb[i][j]!='R')	continue;
				int ct=0;
				for(int k=i;k<n;k++){
					if(bb[k][j]!='R')	break;
				//	cout<<k<<" == "<<bb[k][j]<<endl;
					ct++;
				}
				if(ct>=K)	red=true;
			//	cout<<i<<" "<<j<<" "<<ct<<endl;
				ct=0;
				for(int k=j;k<n;k++){
					if(bb[i][k]!='R')	break;
					ct++;
				}
				if(ct>=K)	red=true;

				ct=0;
				for(int k=i,l=j;k<n && l<n;k++,l++){
					if(bb[k][l]!='R')	break;
					ct++;
				}
				if(ct>=K)	red=true;

				ct=0;
				for(int k=i,l=j;k<n && l>=0;k++,l--){
					if(bb[k][l]!='R')	break;
					ct++;
				}
				if(ct>=K)	red=true;

			}
		}

		F(i,n)F(j,n){
			if(bb[i][j]=='R')	bb[i][j]='B';
			else if(bb[i][j]=='B')	bb[i][j]='R';
		}
	//	cout<<blue<<" "<<red<<endl;
		blue=red;
		red=false;
		F(i,n){
			F(j,n){
				if(bb[i][j]!='R')	continue;
				int ct=0;
				for(int k=i;k<n;k++){
					if(bb[k][j]!='R')	break;
	//				cout<<k<<" == "<<bb[k][j]<<endl;
					ct++;
				}
	//			cout<<i<<" "<<j<<" = "<<ct<<endl;
				if(ct>=K)	red=true;
	//			cout<<red<<endl;
				ct=0;
				for(int k=j;k<n;k++){
					if(bb[i][k]!='R')	break;
					ct++;
				}
				if(ct>=K)	red=true;

				ct=0;
				for(int k=i,l=j;k<n && l<n;k++,l++){
					if(bb[k][l]!='R')	break;
					ct++;
				}
				if(ct>=K)	red=true;

				ct=0;
				for(int k=i,l=j;k<n && l>=0;k++,l--){
					if(bb[k][l]!='R')	break;
					ct++;
				}
				if(ct>=K)	red=true;
			}
		}
		swap(blue,red);
		
		cout<<"Case #"<<cas<<": ";
		if(red && blue)	cout<<"Both\n";
		else if(red)	cout<<"Red\n";
		else if(blue)	cout<<"Blue\n";
		else			cout<<"Neither\n";
	}
	return 0;
}
