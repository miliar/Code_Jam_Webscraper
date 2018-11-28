

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
#define EPS  1e-8
#define SET(NAME)   (memset(NAME,-1,sizeof(NAME)))
#define CLR(NAME)   (memset(NAME,0,sizeof(NAME)))
#define max(a,b) ((a)>(b)?(a):(b))
#define INPUT freopen("contest/A-large.in","rt",stdin);
#define OUTPUT freopen("contest/out.txt","w",stdout);
//--------------------------------------------------------
int N,ar[1000];
char str[1000];
int findValu(){

	int i,ret=0;
	for(i=0;i<N;i++)
		if(str[i]=='1')
			ret=i+1;
	return ret;
}
int findPos(int i){

	for(int k=i;k<N;k++)
		if(ar[k]<=i)
			return k;
}
void process(){


	int i,res=0,pos,j,tmp;
	for(i=0;i<N;i++)
	if(ar[i]>i+1){
	
		pos=findPos(i+1);
		res+=pos-i;
		tmp=ar[pos];
		for(j=pos;j>i;j--)
			ar[j]=ar[j-1];
		ar[i]=tmp;
	
	}
	cout<<res<<endl;
}
int main()
{
	int t,i,cas=1;
	INPUT
	OUTPUT
	cin>>t;
	while(t--){
	
		cin>>N;
		for(i=0;i<N;i++){
			scanf("%s",str);
			ar[i]=findValu();
		}
		printf("Case #%d: ",cas++);
		process();
	}		
	return 0;
}
