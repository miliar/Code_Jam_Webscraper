#include <stdio.h>
#include <algorithm>
using namespace std;
#define MAXN 100000
struct  walkway
{
	int b,e,w;
	walkway(){
	}
	walkway(int b,int e,int w):b(b),e(e),w(w){}
};

bool cmp1(const walkway& w1,const walkway& w2){
	return w1.b < w2.b;
}
bool cmp2(const walkway& w1,const walkway& w2){
	return w1.w < w2.w;
}

walkway ww[MAXN];
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,case_num = 1;
	int x,s,r,n;
	int i,j,k;
	double y,t;
	scanf("%d",&T);
	while(T--){
		scanf("%d%d%d%lf%d",&x,&s,&r,&t,&n);
		for (i = 0;i < n;i++)
		{
			scanf("%d%d%d",&ww[i].b,&ww[i].e,&ww[i].w);
		}
		sort(ww,ww+n,cmp1);
		k = n;
		j = 0;
		for (i = 0;i < n;i++)
		{
			if (j < ww[i].b)
			{
				ww[k++] = walkway(j,ww[i].b,0);
			}
			j = ww[i].e;
		}
		if(j < x){
			ww[k++] = walkway(j,x,0);
		}
		n = k;
		sort(ww,ww+n,cmp2);
		y = 0;
		for (i = 0;i < n;i++)
		{
			if (t >= (ww[i].e-ww[i].b+0.0)/(ww[i].w+r))
			{
				y += (ww[i].e-ww[i].b+0.0)/(ww[i].w+r);
				t -= (ww[i].e-ww[i].b+0.0)/(ww[i].w+r);
			} else {
				y += t + (ww[i].e-ww[i].b - (ww[i].w+r)*t)/(ww[i].w+s);
				t = 0;
			}
		}
		printf("Case #%d: %.10f\n",case_num++,y);
	}

	return 0;
}