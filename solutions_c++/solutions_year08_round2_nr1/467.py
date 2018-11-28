#include<iostream>
#include<string>
#include<cmath>
#include<algorithm>
#include<vector>
using namespace std;
int main(){
	int t,n,cs=1;
	long long int i,j,k,x,y,x0,y0,a,b,c,d,m;
	cin>>t;
	for(cs=1;cs<=t;cs++){
		cin>>n>>a>>b>>c>>d>>x0>>y0>>m;
		vector< vector<int> > v;
		vector<int> w(2);
		x=x0;y=y0;
		w[0]=x;
		w[1]=y;
		v.push_back(w);
		for(i=1;i<n;i++){
			x=(a*x+b)%m;
			y=(c*y+d)%m;
			w[0]=x;
			w[1]=y;
			v.push_back(w);
		}
		c=0;
		for(i=0;i<n;i++){
			for(j=i+1;j<n;j++){
				for(k=j+1;k<n;k++){
					if((v[i][0]+v[j][0]+v[k][0])%3==0&&(v[i][1]+v[j][1]+v[k][1])%3==0)
						c++;
				}
			}
		}
		cout<<"Case #"<<cs<<": "<<c<<endl;
	}
	return 0;
}

