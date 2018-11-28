#include<cstdio>
#include<iostream>
#include<cmath>
#include<algorithm>
#include<vector>
using namespace std;
struct xx{
	int z,a;
	xx(){}
};
bool cmp1(const xx &l,const xx &r){
	return l.z<r.z;
}
bool cmp2(const xx &l,const xx &r){
	return l.a<r.a;
}
int main(){
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int C,ccc,n,i,j,k,T,t;
	vector <xx> p;
	scanf("%d",&C);
	for(ccc=1;ccc<=C;++ccc){
		scanf("%d",&n);
		p.resize(n);
		for(i=0;i<n;++i){
			scanf("%d",&p[i].z);
			p[i].a=i;
		}
		sort(p.begin(),p.end(),cmp1);
		for(i=0;i<n;++i)p[i].z=i;
		sort(p.begin(),p.end(),cmp2);
		T=0;
		for(i=0;i<n;++i)
		  if(p[i].z!=i){
			k=0;j=i;
			do{ t=j;
			    j=p[j].z;
			    p[t].z=t;
				++k;
			}while(j!=i);
			T+=k;
		}
		printf("Case #%d: %.6lf\n",ccc,1.0*T);
	}
	return 0;
}
