#include<iostream>
#include<vector>
#include<sstream>
#include<algorithm>
#include<set>
#include<map>
#define pp pair<int,int>
#define f first
#define s second
#include<cmath>
#define pb push_back

using namespace std;
int main()
{
	int t;
	cin>>t;
	int ct=0;
	while(t--)
	{
		ct++;
		pp p;
		vector<pp>v;
		int n;
		cin>>n;
		while(n--)
		{
			cin>>p.f>>p.s;
			v.pb(p);
		}
		int ans=0;
		for(int i=0;i<v.size();i++)
		{
			for(int j=i+1;j<v.size();j++)
			{
				if(i==j)continue;
				
			
			int y1=v[i].f;
int y2=v[i].s;

int y3=v[j].f;
int y4=v[j].s;			
		double	A1=(y2-y1)*1.0;
double B1 = -10.0;
double C1 = B1*y1;

		double	A2=(y4-y3)*1.0;
double B2 = -10.0;
double C2 = B2*y3;

    double det = A1*B2 - A2*B1;
    if(det == 0){
        continue;
    }else{
        double x = (B2*C1 - B1*C2)/det;
        double y = (A1*C2 - A2*C1)/det;
		
		if(( ceil(x)<= 10 && floor(x) >=0) &&(ceil(y)<=max(y1,y2)  && floor(y)>=min(y1,y2)) &&(ceil(y)<=max(y3,y4)  && floor(y)>=min(y3,y4)))ans++;
    }

				}
				}
				cout<<"Case #"<<ct<<": "<<ans<<endl;
				}
				return 0;
				}
				
				
			
		
			
	