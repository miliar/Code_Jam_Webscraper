#include<iostream>
#include<vector>
#include<sstream>

using namespace std;

int to(string s){
	s[2]=' ';
	istringstream iss(s);
	int h,m; iss>>h>>m;
	
	return h*60+m;
}

int main(){
	int cases; cin>>cases;
	for(int num=1;num<=cases;num++){
		int T; cin>>T;
		int NA,NB; cin>>NA>>NB;
		vector<int> ab_s,ab_d,ba_s,ba_d;
		for(int i=0;i<NA;i++){
			string src,dest; cin>>src>>dest;
			ab_s.push_back(to(src));
			ab_d.push_back(to(dest)+T);
		}
		for(int i=0;i<NB;i++){
			string src,dest; cin>>src>>dest;
			ba_s.push_back(to(src));
			ba_d.push_back(to(dest)+T);
		}
		sort(ab_s.begin(),ab_s.end());
		sort(ab_d.begin(),ab_d.end());
		sort(ba_s.begin(),ba_s.end());
		sort(ba_d.begin(),ba_d.end());
		
		int resab=NA,resba=NB;
		
		for(int i=0,j=0;i<NB;i++){
			for(;j<NA;j++){
				if(ba_d[i]<=ab_s[j]){
					resab--;
					j++;
					break;
				}
			}
		}
		
		for(int i=0,j=0;i<NA;i++){
			for(;j<NB;j++){
				if(ab_d[i]<=ba_s[j]){
					resba--;
					j++;
					break;
				}
			}
		}
		
		cout<<"Case #"<<num<<": "<<resab<<' '<<resba<<endl;
	}
	
	return 0;
}
