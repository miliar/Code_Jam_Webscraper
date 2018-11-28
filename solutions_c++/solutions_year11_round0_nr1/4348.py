#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<set>

using namespace std;

#define rep(i,n) for(int i=0;i<int(n);i++)

#define mp(a,b) make_pair(a,b)
#define f first
#define s second

int main(){
	int T;
	cin>>T;
	
	rep(p,T){
		int n;
		cin>>n;
		
		vector<pair<int,int> > vec;
		vector<int> a;
		vector<int> b;
		
		rep(i,n){
			char ca;
			int in;
			cin>>ca>>in;
			
			if(ca=='O'){
				vec.push_back(mp(0,in));
				a.push_back(in);
			}else{
				vec.push_back(mp(1,in));
				b.push_back(in);
			}
		}
		
		a.push_back(0);
		b.push_back(0);
		
		int ans=0;
		int aa=1;
		int bb=1;
		
		int an=0;
		int bn=0;
		rep(i,vec.size()){
			while(1){
				int flg=0;
				if(vec[i].f==0 && vec[i].s==aa){
					an++;
					flg=1;
				}else{
					if(aa < a[an])aa++;
					if(aa > a[an])aa--;
				}
				if(vec[i].f==1 && vec[i].s==bb){
					bn++;
					flg=1;
				}else{
					if(bb < b[bn])bb++;
					if(bb > b[bn])bb--;
				}
				
				
				ans++;
				if(flg==1)break;
			}
		}
		printf("Case #%d: %d\n",p+1,ans);
	}
}