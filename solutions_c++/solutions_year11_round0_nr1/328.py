#include <iostream>
#include <map>
#include <cmath>
using namespace std;

const int N=200;
int n;
char r[N];
int b[N];
int t;
int now;
int timet;
int loc[2], Ttime[2];

int main(){
	freopen("a.in", "r",stdin);	
	freopen("a.txt", "w",stdout);
	cin>>t;

	for(int L=1; L<=t; ++L){
		cin>>n;
		for(int i=0; i<n; ++i)
			cin>>r[i]>>b[i];
		loc[0]=loc[1]=1;
		Ttime[0]=Ttime[1]=0;
		for(int i=0; i<n; ++i)
		{
			if (r[i]=='O') {now=0;} else {now=1;}
			timet=  labs(b[i]-loc[now])+ Ttime[now]+1;
			if (timet<= Ttime[1-now]) timet=Ttime[1-now]+1;
			Ttime[now]=timet; loc[now]=b[i];
			//cout<<"N:" << i<<"   "<<timet<<" "<<loc[0]<<" "<<loc[1]<<endl;
		}
		
		cout<<"Case #"<<L<<": "<<max(Ttime[0], Ttime[1])<<endl;
	}	
}
