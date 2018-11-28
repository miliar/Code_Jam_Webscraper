#include<cstdio>
#include<sstream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

int n,a,b;
vector<int> v;

int func(int x,int b){
	stringstream ss;
	ss << x << x;
	string d = ss.str();

	v.clear();
	int len = d.length()/2;
	int y;
	int res=0;
	for(int i=0; i<len; i++){
		string temp=d.substr(i,len);
		stringstream s2;
		s2 << temp;
		s2 >> y;

		if(y>x && y<=b){
			v.push_back(y);
			res++;
		}
	}
	sort(v.begin(),v.end());
	for(int i=0; i+1<v.size(); i++){
		if(v[i]==v[i+1]) res--;
	}
	return res;
}

int main(){
	scanf("%d",&n);
	for(int i=1; i<=n; i++){
		scanf("%d%d",&a,&b);
		long long wynik=0;
		for(int j=a; j<=b; j++){
			wynik+=func(j,b);
		}
		printf("Case #%d: %lld\n",i,wynik);
	}
}

