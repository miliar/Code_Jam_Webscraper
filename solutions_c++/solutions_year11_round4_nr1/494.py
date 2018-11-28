#include<iostream>

using namespace std;

struct st{
	int s,t,w;
	bool operator < (const st &a)const{
		return s < a.s;
	}
};

struct st2{
	int w,len;
	bool operator < (const st2 &a)const{
		return w < a.w;
	}
};

int main(){
	int tn;cin>>tn;
	for(int ttn=1;ttn<=tn;ttn++){
		cout<<"Case #"<<ttn<<": ";
		int x,s,r;
		double t;
		int n;cin>>x>>s>>r>>t>>n;
		st  sts [1010];
		st2 sts2[2021];
		int numofsts2=0;
		for(int i=0;i<n;i++){
			cin>>sts[i].s>>sts[i].t>>sts[i].w;
		}
		sort(sts,sts+n);
		int ss=0;
		for(int i=0;i<n;i++){
			if(sts[i].s>ss){
				sts2[numofsts2].w=s;
				sts2[numofsts2].len=sts[i].s-ss;
				numofsts2++;
			}
			sts2[numofsts2].w=s+sts[i].w;
			sts2[numofsts2].len=sts[i].t-sts[i].s;
			numofsts2++;
			ss=sts[i].t;
		}
		if(ss!=x){
			sts2[numofsts2].w=s;
			sts2[numofsts2].len=x-ss;
			numofsts2++;
		}
		sort(sts2,sts2+numofsts2);
		//for(int i=0;i<numofsts2;i++)cout<<sts2[i].w<<' '<<sts2[i].len<<endl;
		double ans=0;
		for(int i=0;i<numofsts2;i++){
			double len=(double)sts2[i].len;
			if(t>0.0){
				double tt=(double)sts2[i].len/((double)sts2[i].w+(double)(r-s));
				ans+=min(tt,t);
				len-=((double)sts2[i].w+(double)(r-s))*min(tt,t);
				t-=min(tt,t);
			}
			ans+=len/(double)sts2[i].w;
			//cout<<t<<' '<<len<<' '<<ans<<' '<<sts[i].w<<endl;

		}
		printf("%.9f\n",ans);
	}
}
