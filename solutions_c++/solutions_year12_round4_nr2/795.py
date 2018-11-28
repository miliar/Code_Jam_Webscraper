#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
using namespace std;


struct reco{
	int r, x, y;
} a[2000];

int n,w,l;

int inters(reco a, reco b)
{
	double x = a.x-b.x;
	x = x*x;
	double y = a.y-b.y;
	y = y*y;
	double r = a.r+b.r;
	r = r*r;
	return x+y<r;
}

unsigned long long random(){
	unsigned long long  x= rand();
	unsigned long long y = rand();
	return x*65536+y;
}

int work(){
	for (int i=1; i<=n; i++)
	{
		int ok=0, cnt=0;
		while (!ok) {
			ok=1;
			a[i].x = random()%(w+1);
			a[i].y = random()%(l+1);
		//	cout << i<<" "<< a[i].x<<" "<<a[i].y<<endl;
			for (int j=1; j<i; j++)
				if (inters(a[i],a[j])) { ok = 0; cnt++; break; }
			if (cnt>10) return 0; 
		}
	}
	return 1;
}

int main(){
	freopen("B-small-attempt1.in","r",stdin);
	freopen("a.out","w",stdout);
	int test;
	scanf("%d",&test);
	srand(time(0));
	for (int ttt=1; ttt<=test; ttt++){
		printf("Case #%d:",ttt);
		scanf("%d%d%d",&n,&w,&l);
		for (int i=1; i<=n; i++){
			scanf("%d",&a[i].r);
		}
		while (!work()) ;
		for (int i=1; i<=n;i++)
			printf(" %d %d", a[i].x,a[i].y);
		printf("\n");
	}
}