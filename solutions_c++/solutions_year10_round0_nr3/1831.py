//Author  :   MAK(Kader)
//Problem no:  
//Title:  Cse DU

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
#define min(a,b) ((a)<(b)?(a):(b))

struct type{
	long long int sum,nxt_id;
};
long long int T,R,K,N;
long long int Tsum;
int A[1003];
int step=500;
type next_map[1002],r_map[1002];

type Next_ind(int ind,int k){

	long long int sum=0,i;
	for(i=ind;k>0;i=(i+1)%N){
		k-=A[i];
		if(k<0) break;
		sum+=A[i];
		
	}
	type ret;
	ret.sum=sum;
	ret.nxt_id=i;
	return ret;
}
type next_ind(int ind,int k){

	long long int res=0;
	type ret;
	if(k>=Tsum){
		ret.nxt_id=ind;
		ret.sum=Tsum;
		return ret;
	}
	
	ret=Next_ind(ind,k);
	ret.sum+=res;
	return ret;
}
type next_n_round(int ind,int n){

	type ret;

	long long sum=0;
	int i,cur=ind;
	for(i=0;i<n;i++){
	
		sum+=next_map[cur].sum;
		cur=next_map[cur].nxt_id;
	}
	ret.sum=sum;
	ret.nxt_id=cur;
	return ret;
}
void save_next_map(){

	int i;
	for(i=0;i<N;i++){
		next_map[i]=next_ind(i,K);
	}
}
void save_next_n_round(){

	
	int i;
	for(i=0;i<N;i++){
		r_map[i]=next_n_round(i,step);
	}
}
void process(){

	save_next_map();
	save_next_n_round();
	
	long long int cur=0,sum=0;
	int i,left;
	for(i=0;i<R;i+=step){
		if(i+step>R) break;
		sum+=r_map[cur].sum;
		cur=r_map[cur].nxt_id;
		
	}

	left=R-i;
	for(i=0;i<left;i++){
		sum+=next_map[cur].sum;
		cur=next_map[cur].nxt_id;
	}
	cout<<sum<<endl;
}
int main()
{
	freopen("code_jam/C-large.in","rt",stdin);
	freopen("code_jam/out.txt","wt",stdout);
	int i,cas=1;
	cin>>T;
	while(T--){
	
		cin>>R>>K>>N;
		Tsum=0;
		for(i=0;i<N;i++){					
			cin>>A[i];
			Tsum+=A[i];
		}
		printf("Case #%d: ",cas++);
		process();
	}		
	return 0;
}
