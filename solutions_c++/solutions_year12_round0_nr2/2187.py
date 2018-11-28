#include<cstdio>
#include<iostream>
using namespace std;
int test;
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	cin>>test;
	for (int t=1;t<=test;t++){
		int p1=0,p2=0,p3=0;
		int n,m,p;
		cin>>n>>m>>p;
		for (int i=0;i<n;i++){
			int tmp;
			cin>>tmp;
			if (tmp>3*p-3)
				p1++;
			else if (tmp<3*p-4)
				p2++;
			else if (tmp>1)
				p3++;
		}
		if (p3<m)
			p1+=p3;
		else
			p1+=m;
		printf("Case #%d: %d\n",t,p1);
	}
	return 0;
}
