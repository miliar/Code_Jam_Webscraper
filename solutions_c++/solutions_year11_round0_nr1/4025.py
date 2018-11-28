#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<stdlib.h>

using namespace std;

struct pnt{
	char ch;
	int d;
};

pnt a[101];
int n;

void get_ans(int nt){
	scanf("%d ",&n);
	for(int i = 0; i < n; i++){
		scanf(" %c %d", &a[i].ch, &a[i].d);
	}
	int curb = 0;
	int posb = 1;
	while((a[curb].ch != 'B')&&(curb < n)) curb++;
	int curo = 0;
	int poso = 1;
	while((a[curo].ch != 'O')&&(curo < n)) curo++;
	int ans = 0;
	int dist;
	for(int cur = 0; (cur < n)&&(curb < n)&&(curo < n); cur++){
		if (a[cur].ch == 'O'){
			dist = 1 + abs(a[cur].d - poso);
			ans = ans + dist;
			if (a[curb].d < posb)
				posb = posb - min(dist, abs(posb - a[curb].d) );
			else
				posb = posb + min(dist, abs(posb - a[curb].d) );
			curo++;
			while((a[curo].ch != 'O')&&(curo < n)) curo++;
			poso = a[cur].d;
		}
		if (a[cur].ch == 'B'){
			dist = 1 + abs(a[cur].d - posb);
			ans = ans + dist;
			if (a[curo].d < poso)
				poso = poso - min(dist, abs(poso - a[curo].d) );
			else
				poso = poso + min(dist, abs(poso - a[curo].d) );
			curb++;
			while((a[curb].ch != 'B')&&(curb < n)) curb++;
			posb = a[cur].d;
		}
	}
	if (curo < n){
		for(int i = curo; i < n; i++){
			ans = ans + 1 + abs(poso - a[i].d);
		        poso = a[i].d;
		}
	}
	if (curb < n){
		for(int i = curb; i < n; i++){
			ans = ans + 1 + abs(posb - a[i].d);
		        posb = a[i].d;
		}
	}
	printf("Case #%d: %d\n",nt,ans);
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int k = 1; k <= t; k++){
		get_ans(k);
	}
	return 0;
}
