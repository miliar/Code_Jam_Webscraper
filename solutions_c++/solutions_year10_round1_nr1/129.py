#include<vector>
#include<cmath>
#include<map>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<string>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<set>
#include<stack>
#include<bitset>
#include<functional>
#include<cstdlib>
#include<ctime>
#include<queue>
#include<deque>
using namespace std;
#define pb push_back
typedef long long lint;
#define mp make_pair
#define fi first
#define se second
typedef pair<int,int> pint;
string outp[4]={"Neither","Blue","Red","Both"};
int ch(int n,int ka,char a,vector <string> in){
	int i,j,k,f;
	for(i=0;i<n;i++) for(j=0;j<n;j++){
		//ç∂
		f=0;
		for(k=0;k<ka;k++){
			int x=i,y=j+k;
			if(x<0 || x>=n || y<0 || y>=n){f=1;continue;}
			if(in[x][y]!=a) f=1;
		}
		if(f==0) return 1;
		//ç∂â∫
		f=0;
		for(k=0;k<ka;k++){
			int x=i+k,y=j+k;
			if(x<0 || x>=n || y<0 || y>=n){f=1;continue;}
			if(in[x][y]!=a) f=1;
		}
		if(f==0) return 1;
		//â∫
		f=0;
		for(k=0;k<ka;k++){
			int x=i+k,y=j;
			if(x<0 || x>=n || y<0 || y>=n){f=1;continue;}
			if(in[x][y]!=a) f=1;
		}
		if(f==0) return 1;
		//âEâ∫
		f=0;
		for(k=0;k<ka;k++){
			int x=i+k,y=j-k;
			if(x<0 || x>=n || y<0 || y>=n){f=1;continue;}
			if(in[x][y]!=a) f=1;
		}
		if(f==0) return 1;
	}
	return 0;
}
vector <string> gra(int n,vector <string> in){
	vector <string> ret=in;int i,j;
	for(i=0;i<n;i++){
		string a;
		for(j=0;j<n;j++){
			if(in[j][i]!='.') a+=in[j][i];
		}
		int t=n-a.size();
		for(j=0;j<t;j++) ret[j][i]='.';
		for(j=0;j<a.size();j++) ret[j+t][i]=a[j];
	}
	return ret;
}
vector <string> ro(int n,vector <string> in){
	vector <string> ret=in;int i,j;
	for(i=0;i<n;i++) for(j=0;j<n;j++){
		ret[j][n-1-i]=in[i][j];
	}
	return ret;
}
int main()
{
	int i,j,n,k,t;string st;cin>>t;vector <string> out;
	for(i=0;i<t;i++){
		cin>>n>>k;
		vector <string> in;
		for(j=0;j<n;j++){cin>>st;in.pb(st);}
//		for(j=0;j<n;j++) cout<<in[j]<<endl;
		in=ro(n,in);in=gra(n,in);
//		for(j=0;j<n;j++) cout<<in[j]<<endl;
		out.pb(outp[ch(n,k,'B',in)+ch(n,k,'R',in)*2]);
	}
	for(i=0;i<t;i++) cout<<"Case #"<<i+1<<": "<<out[i]<<endl;
	return 0;
}
