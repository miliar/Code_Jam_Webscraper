//SORU
//PROGRAM C++

/*
	ID: semihbasrik
	LANG: C++
	TASK:
*/
#include<iostream>
#include<fstream>
#include<algorithm>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<list>
#include<cstdio>
#include<cstring>
#include<string>
#include<cmath>
#include<cstdlib>
#include<vector>
#include<climits>
#define mp make_pair
#define pb push_back
#define st first
#define nd second
#define wait system("pause");
#define lint long long int
#define ABS(a)	 ( (a)>0 ? (a) : -(a) )
#define KARE(a)	 ( (a)*(a) )
#define MAX(a,b) ( (a)>(b) ? (a) : (b) )
#define MIN(a,b) ( (a)<(b) ? (a) : (b) )
#define INF		 INT_MAX
#define cin fin
#define cout fout
using namespace std;
ifstream fin("B-small-attempt0.in");
ofstream fout("B-small-attempt0.out");

int T,N,S,P,A[105];

int minor(int x){ 
	if(x<=1)	return 0;
	if(x==2)	return 1;
	return (x/3)+(x%3!=0);
}
int major(int x){
	if(x<=2)	return -1;
	return (x/3+1)+(x%3==2); 
}

int solve(){
	int i,tmp,res=0,syc=0,V[105]={0};
	set< pair<int,int> >ST;
	set< pair<int,int> >::iterator it;
	for(i=1;i<=N;i++)
		if( A[i]%3!=1 ){
			tmp=major(A[i]);
			if( tmp>=P )
				ST.insert( mp( tmp,i ) );
		}
	for( it=ST.begin();syc!=S && it!=ST.end();it++,syc++,res++)
		V[it->nd]=1;
	for(i=1;i<=N;i++)
		if(V[i]==0 && minor(A[i])>=P )
			res++;
	return res;
}

void read(){
	int i,j;
	cin>>T;
	for(i=1;i<=T;i++){
		cin>>N>>S>>P;
		for(j=1;j<=N;j++)
			cin>>A[j];
		cout<<"Case #"<<i<<": "<<solve()<<endl;
	}
//	wait;
}

int main(){
	read();
}
