#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
#include<set>

#define ffor(i,n) for(int i=0; i<n; i++)
#define rep(i,n) for(int i=1; i<=n; i++)
#define forit(it,n) for(typeof(n.begin()) it=n.begin(); it!=n.end(); it++)
#define scf(n) scanf("%d", &n);
#define psh push_back
#define mkp make_pair
#define frs first
#define sec second
#define pii pair<int,int>
#define INF 1000000000
#define LL long long
#define LD long double

using namespace std;
const int xam=1000100;

int wyn(int cells, vector<int> &v)
{
    vector<int> wall;
    int war=0;
    wall.psh(0); wall.psh(cells+1);
    
    forit(it,v)
    {
	wall.psh(*it);
	sort(wall.begin(), wall.end()); //forit(iit, wall) printf("%d ", *iit); printf("\n");
	typeof(v.begin()) p=lower_bound(wall.begin(), wall.end(), *it);
// 	printf("p %d %d %d\n", *(p-1), *p, *(p+1));
	war+=*(p+1)-*p-1;
	war+=*p-*(p-1)-1;
// 	printf("war %d\n", war);
    }
//     forit(it,v) printf("%d ", *it); printf("%d\n\n", war);
    return war;
}

int play(int t)
{
    int cells;
    int free,a;
    int maxi=INF;
    vector<int> v; //realesed
    scanf("%d%d", &cells, &free);
    ffor(i,free) {scanf("%d", &a); v.psh(a);}
    
    sort(v.begin(), v.end()); //forit(it,v) printf("%d ", *it);
    a=wyn(cells, v);
    if(a<maxi) maxi=a;
    while(next_permutation(v.begin(),v.end()))
    {
	a=wyn(cells, v);
	if(a<maxi) maxi=a;
    }
    
    printf("Case #%d: %d\n", t,maxi);
}

int main()
{
    int t;
    scanf("%d", &t);
    rep(i,t) play(i);

    return 0;
}