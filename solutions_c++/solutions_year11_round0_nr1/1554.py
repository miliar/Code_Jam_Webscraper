#include<iostream>
#include<vector>
#include<cmath>
#define for(a,b,c) for(int a=b; a<c; a++)
using namespace std;

struct step{
	int s;
	bool o;//is it orange?
};

typedef vector<step> vs;
typedef vector<int>vi;

/*
O 2 B 1 B 2 O 4, 0, (1,1), (0,0)
c=1;
rv=2;
p=(1,2);
b=(2,0);
return 2+
B 1 B 2 O 4, 1, (1,2), (2,0)
c=0;
rv=1;
p=(1,2);
b=(0,1);
return 1+
B 2 O 4, 2, (1,2), (0,1)
c=0;
rv=2;
p=(2,2);
b=(0,3);
return 2+
O 4
c=1;
rv=1;
p=(2,4);
b=(1,0);
return 1+0


*/

int move(vs&v, int s/*step number*/, vi p, vi b){
	if (s>=v.size())
		return 0;
	bool c=v[s].o;//color
	
	int rv=max(abs(p[c]-v[s].s)-b[c],0)+1;
	
	p[c]=v[s].s;
	b[c]=0;
	b[!c]+= rv;//the number of steps it took
	
	return rv+move(v,s+1, p,b);
}

int main(){
	int t;
	cin>>t;
	for(i,0,t){
		int n;
		cin>>n;
		vs steps(n);
		for(j,0,n){
			int s;
			char o;
			cin>>o>>s;
			steps[j].s=s;
			steps[j].o=(o=='O');			
		}
		cout<<"Case #"<<(i+1)<<": "<<move(steps, 0,vi(2,1), vi(2,0))<<endl;
		
	}
	
	
	return 0;
}
