#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <set>
#include <complex>

using namespace std;

typedef complex<double> point;

vector<int> v[2222];
int n,m;
int total;
point p[2222];
const double pi = acos(-1.0);

point base;
int cmp(int a,int b){
	return arg(p[a]-base)<arg(p[b]-base);
}

double cross(point a,point b){
	return (a.real()*b.imag()-a.imag()*b.real())*(-1);
}

set<pair<int,int> > hash;

void go(int first,int second){
	if(hash.find(make_pair(first, second))!=hash.end())
		return;
	vector<int> vec;
	vec.push_back(first);
	vec.push_back(second);
	int prev = first;
	int cur  = second;
	while(1){
		if(hash.find(make_pair(prev, cur))!=hash.end())
			break;
		hash.insert(make_pair(prev, cur));
		for(int k=0;k<v[cur].size();k++)
			if(v[cur][k]==prev){
				int t = v[cur][(k-1+v[cur].size())%v[cur].size()];
				if(cross(p[t]-p[cur],p[cur]-p[prev])<0)
					return;
				prev=cur;
				cur=t;
				break;
			}
		vec.push_back(cur);
	}
	vec.pop_back();
	vec.pop_back();
	total = min(total, (int)vec.size());
	for(int i=0;i<vec.size();i++)
		go(vec[(i+1)%vec.size()],vec[i]);
}

int color[2222];
void go1(int first,int second){
	if(hash.find(make_pair(first, second))!=hash.end())
		return;
	vector<int> vec;
	vec.push_back(first);
	vec.push_back(second);
	int prev = first;
	int cur  = second;
	while(1){
		if(hash.find(make_pair(prev, cur))!=hash.end())
			break;
		hash.insert(make_pair(prev, cur));
		for(int k=0;k<v[cur].size();k++)
			if(v[cur][k]==prev){
				int t = v[cur][(k-1+v[cur].size())%v[cur].size()];
				if(cross(p[t]-p[cur],p[cur]-p[prev])<0)
					return;
				prev=cur;
				cur=t;
				break;
			}
		vec.push_back(cur);
	}
	vec.pop_back();
	vec.pop_back();
	int tot=0;
	for(int i=2;i<total;i++){
		while(tot==color[first] || tot==color[second])
			tot++;
		color[vec[i]] = tot++;
	}
	
	if(total>3){
		int x=0, y=0;
		while(x==total-1 || x==color[first])
			x++;
		while(y==color[first] || x==y)
			y++;
		for(int i=total; i<vec.size();i++){
			color[vec[i]]=x;
			swap(x, y);
		}
	}
	else{
		int x=0, y=0;
		while(x==color[second] || x==color[first])
			x++;
		y=color[second];
		for(int i=2;i<vec.size();i++){
			color[vec[i]]=x;
			swap(x, y);
		}
	}

	for(int i=0;i<vec.size();i++)
		go1(vec[(i+1)%vec.size()],vec[i]);
}


int main(){
	int t;
	cin >> t;
	for(int c=0;c<t;c++){
		cerr << " : " << c << endl;
		cin >> n >> m;
		for(int i=0;i<n;i++)
			v[i].clear();
		hash.clear();
		vector<int> x(m), y(m);
		for(int i=0;i<m;i++)
			cin >> x[i];
		for(int i=0;i<m;i++)
			cin >> y[i];
		for(int i=0;i<m;i++){
			x[i]--;
			y[i]--;
			v[x[i]].push_back(y[i]);
			v[y[i]].push_back(x[i]);
		}
		for(int i=0;i<n;i++){
			int x=(i+1)%n;
			v[i].push_back(x);
			v[x].push_back(i);
		}
		
		for(int i=0;i<n;i++)
			p[i]=polar(1.0,i*2.0*pi/n);

		for(int i=0;i<n;i++){
			base = p[i];
			sort(v[i].begin(),v[i].end(),cmp);
		//	cerr << base << endl;
		}

		total=100000;
		go(0,1);
		printf("Case #%d: %d\n",c+1, total);
		hash.clear();
		memset(color,-1,sizeof(color));
		color[0]=0;
		color[1]=1;
		go1(0,1);
		
		for(int i=0;i+1<n;i++)
			printf("%d ", color[i]+1);
		printf("%d\n",color[n-1]+1);
	}
	return 0;
}
