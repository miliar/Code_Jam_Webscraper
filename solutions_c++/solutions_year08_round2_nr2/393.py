#include<iostream>
#include<string>
#include<cmath>
#include<algorithm>
#include<vector>
using namespace std;
int lgp(int m){
	if(m==1)	return 1;
	int mx=1,i;
	for(i=2;i<=m;i++){
		if(m%i==0){
			mx=i;
			while(m%i==0){
				m/=i;
			}
		}
	}
	return mx;
}
int gcd(int m,int n){
	int modulus;
	while(n!=0){
		modulus=m%n;
		m=n;
		n=modulus;
	}
	return m;
}
int main(){
	int r[1011][1011],i,j,k,c,a,b,p,cs,t,m;
	for(i=1;i<1002;i++){
		for(j=1;j<1002;j++){
			r[i][j]=lgp(gcd(i,j));
		}
	}
	cin>>c;
	for(cs=1;cs<=c;cs++){
		cin>>a>>b>>p;
		t=0;
		m=1;
		vector<int> v(b+4,-1);
		vector< vector<int> > w;
		for(i=a;i<=b;i++){
			for(j=i+1;j<=b;j++){
				if(r[i][j]>=p){
					if(v[i]==-1&&v[j]==-1){
						m=w.size();
						w.resize(m+1);
						w[m].push_back(i);
						w[m].push_back(j);
						v[i]=v[j]=m;
					}
					else if(v[i]==-1){
						v[i]=v[j];
						w[v[i]].push_back(i);
					}
					else if(v[j]==-1){
						v[j]=v[i];
						w[v[j]].push_back(j);
					}
					else{
						if(v[i]<v[j]){
							for(k=0;k<w[v[j]].size();k++){
								w[v[i]].push_back(w[v[j]][k]);
								v[w[v[j]][k]]=v[i];
								if(j!=w[v[j]][k])	v[w[v[j]][k]]=v[i];
							}
							v[j]=v[i];
							w.erase(w.begin()+v[j]);
						}
						else if(v[i]>v[j]){
							for(k=0;k<w[v[i]].size();k++){
								w[v[j]].push_back(w[v[i]][k]);
								if(i!=w[v[i]][k])	v[w[v[i]][k]]=v[j];
							}
							w.erase(w.begin()+v[i]);
							v[i]=v[j];
						}
					}
				}
			}
			if(v[i]==-1){
				m=w.size();
				w.resize(m+1);
				w[m].push_back(i);
				v[i]=m;
			}
		}
		cout<<"Case #"<<cs<<": "<<w.size()<<endl;
	}
	return 0;
}

