

//#pragma warning(disable:4786)
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<string>
#include<cctype>
#include<iostream>
#include<stack>
#include<set>
#include<list>
#include<map>
#include<queue>
#include<vector>
#include<algorithm>
using namespace std;
//-------------------------------------------------------
typedef pair<int,int> ii;
typedef vector<int> vi;
#define pb push_back
#define sz(c) (c).size()
#define all(c) (c).begin(),(c).end()
#define vtr(c,i) for(vi::iterator i=c.begin();i!=c.end();i++)
#define INF  (1<<30)
#define EPS  1e-10
#define SET(NAME)   (memset(NAME,-1,sizeof(NAME)))
#define CLR(NAME)   (memset(NAME,0,sizeof(NAME)))
#define max(a,b) ((a)>(b)?(a):(b))
#define INPUT freopen("contest/D-small-attempt1.in","rt",stdin);
#define OUTPUT freopen("contest/out.txt","w",stdout);
//--------------------------------------------------------
class circle{
public:
	double x,y,r;
}ar[50];
int N;
double Distance(circle a,circle b){

	return sqrt( (a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y));
}
double radi(int i,int j){

	return (Distance(ar[i],ar[j])+ar[i].r+ar[j].r)/2.0;
}

double  process(){

	double res=INF*1.0;

	
	if(N==1)		return ar[0].r;
	if(N==2)		
	return max(ar[0].r,ar[1].r);

	res=min(res, max(radi(0,1),ar[2].r) );
	res=min(res, max(radi(0,2),ar[1].r) );
	res=min(res, max(radi(1,2),ar[0].r) );
	
	return res;
}
int main()
{
	INPUT
	OUTPUT
	int t,i,cas=1;
	cin>>t;
	while(t--){
	
		cin>>N;
		for(i=0;i<N;i++)		
			cin>>ar[i].x>>ar[i].y>>ar[i].r;
		
		printf("Case #%d: ",cas++);
		printf("%.6lf\n",process()+EPS);
		
	
	}	
	return 0;
}
