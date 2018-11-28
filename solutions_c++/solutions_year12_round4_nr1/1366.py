#include <iostream>
#include<string>
#include<vector>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<cmath>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<cstdlib>
using namespace std;
class Conf{public:
	int m_index;
	int m_d;
	int m_l;
	bool operator<(const Conf& cf)const{
		if(m_d+m_l!=cf.m_d+cf.m_l)return m_d+m_l<cf.m_d+cf.m_l;
		if(m_d!=cf.m_d) return m_d<cf.m_d;
		return m_l<cf.m_l;
	}
	Conf(int i=0,int d=0,int l=0){m_index=i;m_d=d;m_l=l;}
};
bool order(const Conf& c1,const Conf& c2){
	if(c1.m_d!=c2.m_d) return c1.m_d<c2.m_d;
	return c1.m_l<c2.m_l;
}
int main() {
	int ts;cin>>ts;
	for(int t=0;t<ts;t++){
		int n;cin>>n;
		vector<Conf> vcf(n);
		for(int k=0;k<n;k++){
			vcf[k].m_index=k;
			cin>>vcf[k].m_d>>vcf[k].m_l;
		}
		sort(vcf.begin(),vcf.end(),order);
		for(int k=0;k<n;k++){vcf[k].m_index=k;}
		int D;cin>>D;
		bool ans=false;
		priority_queue<Conf> cfs;
		vcf[0].m_l=vcf[0].m_d;
		cfs.push(vcf[0]);
		while(cfs.size()){
			Conf cf=cfs.top();cfs.pop();
			int w=cf.m_index;
			int far=cf.m_d+cf.m_l;
			if(far>=D){
				ans=true;break;
			}
			for(int k=w+1;k<n;k++){
				if(far<vcf[k].m_d)break;
				//if(vcf[k].m_d-vcf[k].m_l>cf.m_d)continue;
				int i=vcf[k].m_index;
				int d=vcf[k].m_d;
				int l=min(vcf[k].m_d-cf.m_d,vcf[k].m_l);
				cfs.push(Conf(i,d,l));
			}
		}
		if(ans)	cout<<"Case #"<<(t+1)<<": YES"<<endl;
		else    cout<<"Case #"<<(t+1)<<": NO"<<endl;
	}
	return 0;
}