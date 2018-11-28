#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <fstream>

using namespace std;

#define ll long long
ll dist[1010],d[1010];
int main () {
	fstream cin("B-small-attempt1.in");
	ofstream cout("output.txt");
	int Test;
	cin>>Test;
	for (int run=1;run<=Test;++run) {
		ll L,t,N,C;
		cin>>L>>t>>N>>C;
		//cout<<run<<" "<<N<<" "<<C<< " "<<endl;
		for (int i=0;i<C;++i)
			cin>>d[i];
		
		dist[0] = 0;
		for (int i=1;i<=N;++i) 
			dist[i]=d[(i-1)%C]+dist[i-1];
		
		ll speedup=0;
		if (L==0) speedup=0;
		else if (L==1) {
			for (int i=1;i<=N;++i) 
				if (dist[i]*2>=t) {
					ll time;
					if (dist[i-1]*2>=t) time = 0;
					else time = t-dist[i-1]*2;
					speedup = max (speedup,dist[i]-dist[i-1]-time/2);
					//cout<<time<<endl;
				}
		}
		else {
			for (int i=1;i<=N-1;++i)
				for (int j=i+1;j<=N;++j) {
					ll time, s1=0,s2=0;
					if (dist[i]*2>=t) {
						if (dist[i-1]*2>=t) time = 0;
						else time = t-dist[i-1]*2;
						s1 = dist[i]-dist[i-1]-time/2;
					//cout<<time<<endl;
					}	
					if (dist[j]*2>=t) {
						if (dist[j-1]*2>=t) time = 0;
						else time = t-dist[j-1]*2;
						s2 = dist[j]-dist[j-1]-time/2;
					//cout<<time<<endl;
					}	
					speedup = max (speedup,s1+s2);
				}
		}
		//cout<<N<<" "<<C<< " "<<dist[N]*2<<endl;
		ll res = dist[N]*2-speedup;
		cout<<"Case #"<<run<<": "<<res<<endl;
	}
	return 0;
}
