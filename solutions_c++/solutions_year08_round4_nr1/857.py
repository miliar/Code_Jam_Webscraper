#include<iostream>
#include<string>
#include<algorithm>
#include<cmath>
#include<vector>
#include<set>
#include<map>
#include <fstream>
using namespace std;
#define cout fout
int main(){
	ofstream fout("out.txt");
	int t,cs,i,j,k,l,m,n,o,a[11000][2],ff;
	cin>>t;
	for(cs=1;cs<=t;cs++){
		cin>>m>>o;
		vector<int> g(m+1,0),c(m+1,0);
		ff=(m-1)/2;
		for(i=0;i<ff;i++){
			cin>>g[i]>>c[i];
		}
		vector< vector<int> > a(m+1, vector<int> (2,30000) );
		while(i<m){
			cin>>k;
			a[i][k]=0;
			i++;
		}
		for(i=ff-1;i>=0;i--){
			if(g[i]){
				a[i][0]=min(a[i][0],min(a[2*i+1][0]+a[2*i+2][0],min(a[2*i+1][0]+a[2*i+2][1],a[2*i+1][1]+a[2*i+2][0])));
				a[i][1]=min(a[i][1],a[2*i+1][1]+a[2*i+2][1]);
				if(c[i]){
					a[i][0]=min(a[i][0],a[2*i+1][0]+a[2*i+2][0]+1);
					a[i][1]=min(a[i][1],min(a[2*i+1][0]+a[2*i+2][1]+1,min(a[2*i+1][1]+a[2*i+2][0]+1,a[2*i+1][1]+a[2*i+2][1]+1)));
				}
			}
			else{
				a[i][1]=min(a[i][1],min(a[2*i+1][1]+a[2*i+2][0],min(a[2*i+1][0]+a[2*i+2][1],a[2*i+1][1]+a[2*i+2][1])));
				a[i][0]=min(a[i][0],a[2*i+1][0]+a[2*i+2][0]);
				if(c[i]){
					a[i][0]=min(a[i][0],a[2*i+1][0]+a[2*i+2][0]+1);
					a[i][1]=min(a[i][1],min(a[2*i+1][0]+a[2*i+2][1]+1,min(a[2*i+1][1]+a[2*i+2][0]+1,a[2*i+1][1]+a[2*i+2][1]+1)));
				}
			}
		}
		cout<<"Case #"<<cs<<": ";
		if(a[0][o]==30000)
			cout<<"IMPOSSIBLE\n";
		else
			cout<<a[0][o]<<endl;
	}
	return 0;
}

