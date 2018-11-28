#include <cstdio>
#include <queue>

#define NN 120
#define xx first
#define yy second

using namespace std;
typedef long long ll;

pair<int, int> p, P;
vector <pair<int, int> > v;
int n, m, sz, D, t, T, ans, x, y, l;
char s[101][101];

bool dist(pair<int, int> p1, pair<int, int> p2){
	return (ll)(p1.xx-p2.xx)*(p1.xx-p2.xx)+(ll)(p1.yy-p2.yy)*(p1.yy-p2.yy)<=(ll)D*D;
}

bool check(pair<int, int> p1, pair<int, int> p2, pair<int, int> p3){
	if ((ll)p1.xx*(p2.yy-p3.yy)+(ll)p2.xx*(p3.yy-p1.yy)+(ll)p3.xx*(p1.yy-p2.yy)==0){
		if ((p3<p2 && p3<p1) || (p3>p2 && p3>p1)) return true;
  return false;
 }
	return false;
}

pair<int, int> find(int i, int j, int x, int y){
	int X=x, Y=y;
	if (i<0) {
		i=-i;
		for (int i1=0; i1<i; i1++)
		  if (i1%2==0) X-=(2*x);
		  else X-=2*(m-x);
	} else{
    for (int i1=0; i1<i; i1++)
		  if (i1%2==0) X+=2*(m-x);
		  else X+=2*x;
	}
	if (j<0) {
		j=-j;
		for (int i1=0; i1<j; i1++)
		  if (i1%2==0) Y-=(2*y);
		  else Y-=2*(n-y);
	} else{
    for (int i1=0; i1<j; i1++)
		  if (i1%2==0) Y+=2*(n-y);
		  else Y+=2*y;
	}
	return make_pair(X, Y);
}

int main(){
  freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	
	scanf("%d", &T);
	while (T--){
		scanf("%d%d%d", &n, &m, &D);
		v.clear(); ans=0; sz=0; t++; D*=2;
		
		for (int i=n-1; i>=0; i--){
			scanf("%s", s[i]);
			for (int j=0; j<m; j++)
			  if (s[i][j]=='X') {y=2*i-1; x=2*j-1;}
  	}
		n-=2; m-=2; n*=2; m*=2; P=make_pair(x, y);
		
		p=make_pair(-x, y);
		if (dist(P, p)) ans++;
		p=make_pair(x, -y);
		if (dist(P, p)) ans++;
		p=make_pair(x+2*(m-x), y);
		if (dist(P, p)) ans++;
		p=make_pair(x, y+2*(n-y));
		if (dist(P, p)) ans++;
		
		for (int i=-NN; i<=NN; i++)
		  for (int j=-NN; j<=NN; j++)
				if (i!=0 && j!=0){
					p=find(i, j, x, y); l=0;
					if (dist(p, P)){ l=1;
						for (int k=0; l && k<sz; k++)
				  		if (check(v[k], p, P)) l=0;
					}
					if (l==1) {ans++; sz++; v.push_back(p);}
				}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
