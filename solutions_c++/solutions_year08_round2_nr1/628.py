#include <vector>
#include <string>
#include <map>
#include <set>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cctype>
#include <cassert>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;

int mymod(int a,int b,int m){
	LL aa=(LL)a,bb=(LL)b,mm=(LL)m;
	return (int)(aa*bb %mm);
}	

int doit(){
	int a,b,c,d,x,y,m,n;
	cin >>n>>a>>b>>c>>d>>x>>y>>m;
	
	VPII vp;
	vp.push_back(PII(x,y));
	
	for(int i=1;i<=n-1;i++){
		x=(mymod(a,x,m)+b) % m;
		y=(mymod(c,y,m)+d) % m;
		vp.push_back(PII(x,y));
	}	
//	for(int i=0;i<(int)vp.size();i++)
//		printf("(%d,%d)\n",vp[i].first,vp[i].second);

	int len=vp.size(),cnt=0;
	for(int i=0;i<len;i++)
		for(int j=i+1;j<len;j++)
			for(int k=j+1;k<len;k++){
				int xx=vp[i].first%3+vp[j].first%3+vp[k].first%3;
				int yy=vp[i].second%3+vp[j].second%3+vp[k].second%3;
//				cerr << "x: "<<xx<<" y: "<<yy<<endl;
				if(xx%3==0 && yy%3==0) cnt++;
			}
	return cnt;
}	

int main(){
	int num_cases;
	cin >> num_cases;
	for(int kase=1;kase<=num_cases;kase++){
		cout << "Case #"<<kase<<": "<< doit()<<endl; 
	}	
	return 0;
}	
