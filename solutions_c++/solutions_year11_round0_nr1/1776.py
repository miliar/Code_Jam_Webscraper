#include<iostream>
#include<string>
#include<vector>
#include<utility>
#include<algorithm>

using namespace std;

struct pos{
	int k;
	int z;
};


int n;

int Next(vector<pos> &a,vector<int> &next, int k){
	if(next[k]==n){
		return 1;
	}
	return a[next[k]].k;
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	int T;
	cin >> T;
	for(int q=0;q<T;q++){
		cin >> n;
		vector<pos> a;
		for(int i=0;i<n;i++){
			string s;
			pos p;
			cin >> s >> p.k;
			if(s=="O")p.z=0;
			else p.z=1;
			a.push_back(p);
		}
		vector<int> nextO(n),nextB(n);
		int o=n,b=n;
		for(int i=n-1;i>=0;i--){
			nextO[i]=o;
			nextB[i]=b;
			if(a[i].z==0){
				o=i;
			}
			else{
				b=i;
			}
		}

		int t=0;

		pos p0,p1;
		p0.k=1;
		p0.z=0;
		p1.k=1;
		p1.z=1;
		for(int i=0;i<n;i++){
			if(a[i].z==0){
				int l=abs(a[i].k-p0.k)+1;
				t+=l;
				p0.k=a[i].k;
				int k=Next(a,nextB,i);
				if(abs(k-p1.k)<=l){
					p1.k=k;
				}
				else{
					int z=(k-p1.k)/abs(k-p1.k);
					p1.k+=z*l;
				}
			}
			else{
				int l=abs(a[i].k-p1.k)+1;
				t+=l;
				p1.k=a[i].k;
				int k=Next(a,nextO,i);
				if(abs(k-p0.k)<=l){
					p0.k=k;
				}
				else{
					int z=(k-p0.k)/abs(k-p0.k);
					p0.k+=z*l;
				}
			}
		}
		cout << "Case #" << q+1 << ": " << t << endl;
	}
	return 0;
}
