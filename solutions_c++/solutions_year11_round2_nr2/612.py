#include <cstdio>
#include <algorithm>

using namespace std;

struct sta{
	int num;
	double pos;
};

const int maxn=220;
int tr,n;
double d;
sta p[maxn];

bool cmp(sta a,sta b){
	return a.pos<b.pos;
}

inline bool check(double times){
	double last=p[0].pos-times;
	for (int i=0;i<n;i++)
	        for (int j=0;j<p[i].num;j++)
	                if (last+d<p[i].pos)
	                        if (p[i].pos-times>last+d)
	                                last=p[i].pos-times;
				else last+=d;
			else
			        if (last+d-p[i].pos>times) return false;
			                else last+=d;
	return true;
}

int main(){
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	scanf("%d",&tr);
	for (int test=0;test<tr;test++){
		scanf("%d%lf",&n,&d);
		for (int i=0;i<n;i++)
		        scanf("%lf%d",&p[i].pos,&p[i].num);
		sort(p,p+n,cmp);
		p[0].num--;
		double left=0,right=1e7;
		while (right-left>1e-8){
			double mid=(left+right)/2.0;
			if (check(mid)) right=mid;
			        else left=mid;
		//	printf("%lf %lf\n",left,right);
		}
		printf("Case #%d: %.8f\n",test+1,left);
	}
	
	return 0;
}
