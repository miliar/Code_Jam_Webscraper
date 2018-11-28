#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
using namespace std;
struct seg{
	int len;
	int spd;
	double tm;
	seg(int l,int s):len(l),spd(s){}
	bool operator<(const seg& s)const{
		return spd < s.spd;
	}
};
int main(int argc, const char *argv[])
{
	int times;
	int S,R,N,t,X;
	cin>>times;
	for(int tm=1;tm<=times;tm++){
		vector<seg> a;
		cin>>X>>S>>R>>t>>N;
		int last=0;
		for(int i=0;i<N;i++){
			int w,b,e;
			cin>>b>>e>>w;
			if(last!=b){
				a.push_back(seg(b-last,0));
			}
			last=e;
			a.push_back(seg(e-b,w));
		}
		if(last!=X){
			a.push_back(seg(X-last,0));
		}
		sort(a.begin(),a.end());
		double rem=t;
		for(int i=0;i<a.size();i++){
			double tt=a[i].len/double(R+a[i].spd);
			if(tt<=rem){
				rem-=tt;
				a[i].tm=a[i].len/double(R+a[i].spd);
			}else{
				a[i].tm=(a[i].len-rem*(R+a[i].spd))/double(S+a[i].spd)+rem;
				rem=0;
			}
		}
		double res=0;
		for(int i=0;i<a.size();i++)res+=a[i].tm;
		printf("Case #%d: %.6lf\n",tm,res);
	}
	return 0;
}
