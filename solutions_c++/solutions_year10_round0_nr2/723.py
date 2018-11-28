#include<iostream>
#include<string>
#include<vector>
#define LENGTH 100
using namespace std;

int compare(vector<int> x, vector<int> y){
	for(int i=LENGTH-1;i>=0;i--){
		if(x[i]<y[i])return -1;
		else if(x[i]>y[i])return 1;
	}
	return 0;
}

vector<int> subtract(vector<int> x, vector<int> y){
	vector<int> z(LENGTH,0);
	for(int i=0;i<LENGTH;i++)
		z[i]=x[i]-y[i];
	for(int i=0;i<LENGTH-1;i++)
		if(z[i]<0){
			z[i]+=10;
			z[i+1]--;
		}
	return z;
}

vector<int> mod(vector<int> x, vector<int> y){
	int shift=0;
	while(y[LENGTH-1]>0){
		for(int i=LENGTH-1;i>0;i--)
			y[i]=y[i-1];
		shift++;
	}
	while(shift>=0){
		while(compare(x,y)>=0){
			vector<int> z = subtract(x,y);
			swap(x,z);
		}
		shift--;
	}
	return x;
}

void print(vector<int> z){
	int i;
	for(i=LENGTH-1;i>=0&&!z[i];i--);
	if(i<0)cout<<"0";
	for(;i>=0;i--)
		cout<<z[i];
}

vector<int> scan(){
	vector<int> z(LENGTH,0);
	string s;
	cin>>s;
	for(int i=s.length()-1,j=0;i>=0;i--,j++)
		z[j]=s[i]-'0';
	return z;
}

bool zero(vector<int> z){
	for(int i=0;i<LENGTH;i++)
		if(z[i]) return 0;
	return 1;
}

vector<int> gcd(vector<int> x, vector<int> y){
	if(zero(y)) return x;
	return gcd(y, mod(x,y));
}

int main(){
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++){
		int n;
		cin>>n;
		vector<vector<int> > v;
		for(int i=0;i<n;i++)
			v.push_back(scan());
//		cout<<"scan done"<<endl;
		int minpos=0;
		for(int i=1;i<n;i++)
			if(compare(v[i],v[minpos])==-1)
				minpos=i;
//		cout<<"find min done"<<endl;
		vector<vector<int> > w;
		for(int i=0;i<n;i++)
			w.push_back(subtract(v[i],v[minpos]));
//		cout<<"subtract done"<<endl;
		vector<int> g=w[0];
		for(int i=1;i<n;i++){
//			cout<<"finding gcd ";print(g);cout<<" and ";print(w[i]);cout<<endl;
			vector<int> g2=gcd(g,w[i]);
			swap(g,g2);
//			cout<<"gcd now ";print(g);cout<<endl;
		}
//		cout<<"gcd done"<<endl;
		cout<<"Case #"<<tt<<": ";
		if(zero(g))cout<<"0";
		else{
			vector<int> x=mod(v[0],g);
			if(zero(x))print(x);
			else print(subtract(g,x));
		}
		cout<<endl;
	}
	return 0;
}
