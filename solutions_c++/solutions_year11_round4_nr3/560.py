#include<cstdio>
#include<set>
#include<algorithm>
#include<vector>
using namespace std;
const int MAX=1000001;
int arr[MAX];
vector<long long> p;
set<long long> S;
long long N;
void genprimes(){
	int i,j;
	for(i=3;i*i<MAX;i+=2)
	{
		for(j=i;j*i<MAX;j+=2)
		{ 
			arr[i*j]=1;
		} 
	}
	p.push_back(2);
	for(i=3;i<=MAX;i+=2) if(arr[i]==0) p.push_back(i);//,printf("%d,",i);
}

void doit(){
	int i;
	for(i=0;i<p.size() and (p[i]*p[i]<=N);i++){
		long long x=p[i];
		while(x*p[i]<=N) {
			x=x*p[i];
			S.insert(x);
		}
	}
	S.insert(1);
}

int main(){
	int no;
genprimes();
	scanf(" %d",&no);
	int tc;
	for(tc=1;tc<=no;tc++){
		printf("Case #%d: ",tc);
		scanf(" %lld",&N);
		int i;
		S.clear();
		if(N==1) {printf("0\n");continue; }
		doit();
		printf("%lld\n",(long long)S.size());
	
	}
	return 0;
}


