#include <cstdio>
#include <cstring>
#include <iostream>
#include <cmath>
using namespace std;
const double EPS=1e-10;

int main(){
	freopen("B-large.in","rb",stdin);
	freopen("B-large.out","wb",stdout);
	int ca,u=0,i,j;
	scanf("%d",&ca);
	while(ca--){
		u++;
		int l,p,c;
		scanf("%d%d%d",&l,&p,&c);

		double temp=double(p)/double(l);
		double d=1.0/double(c);

		int res=0;
		while(temp>double(c)&&fabs(temp-double(c))>EPS){

			temp=sqrt(temp);
			res++;
		}
		printf("Case #%d: %d\n",u,res);
	}
	return 0;
}