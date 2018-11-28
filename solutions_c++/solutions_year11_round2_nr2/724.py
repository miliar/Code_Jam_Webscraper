#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<string>
#include<cstdio>
#include<map>
#define PI 3.1415926535897932384626433832795
using namespace std;
double eps=1e-12;
vector <double> a;
vector <double> p;
int d;
bool pr(double x){
	//if ((a[a.size()-1]-a[0]+2*x)/(a.size()+0.0)<d+eps)
	//	return 0;
	p=a;
	p[0]-=x;
	int n=p.size();
	p[n-1]+=x;
	//for (int i=0; i<n; i++)
	//	cout<<p[i]<<" ";
	//cout<<endl;
	for (int i=1; i<n-1; i++)
		if (p[i]<=p[i-1]+d)
			p[i]=min(p[i]+x,p[i-1]+d);
		else
			if (p[i]-x<=p[i-1]+d)
				p[i]=max(p[i]-x,p[i-1]+d);
			else
				p[i]-=x;
	//for (int i=0; i<n; i++)
	//	cout<<p[i]<<" ";

	for (int i=1; i<n; i++)
		if (p[i]-p[i-1]<d)
			return 0;
	return 1;
}
int main(){
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	int t;
	cin>>t;
	for (int q=0; q<t; q++){
		cout<<"Case #"<<q+1<<": ";
		int n;
		a.clear();
		cin>>n>>d;
		for (int i=0; i<n; i++){
			int x,y;
			cin>>x>>y;
			for (int j=0; j<y; j++)
				a.push_back(x);
		}
		double MIN=0, MAX=1000000,ser;
		//cout<<"        - "<<pr(3)<<endl;

		while (MAX-MIN>1e-8){
			ser=(MIN+MAX)*0.5;
			if (pr(ser))
				MAX=ser;
			else
				MIN=ser;
		}
		
		printf("%.7f\n",MIN);
	}
	
return 0;
}