#include<cstdio>
#include<cstring>
#include<algorithm>
#include<map>
using namespace std;

int test,n,list[100],Case;
map<int,int> hash;
map<int,int>::iterator it;

int gcd(int a,int b){
	if (!b) return a;
	return gcd(b,a%b);
}
int lcm(int a,int b){
	return a/gcd(a,b)*b;
}
int main(){
	freopen("i.txt","r",stdin);
	for (scanf("%d",&test);test--;){
		printf("Case #%d: ",++Case);
		scanf("%d",&n);
		if (n==1){
			puts("0");
			continue;
		}
		hash.clear();
		int cnt=0,tot=0;
		hash[2]=1;
		for (int i=3;i<=n;i++){
			int p=2,tmp=i;
			for (;p*p<=tmp;p++) if (tmp%p==0){
				int res=0;
				for (;tmp%p==0;tmp/=p,res++);
				if (!hash.count(p)) hash[p]=res;
					else{
						if (res>hash[p]) hash[p]=res;
					}
			}
			if (tmp>1){
				if (!hash.count(tmp)) hash[tmp]=1;
			}
		}
		cnt=hash.size();
		for (it=hash.begin();it!=hash.end();it++) tot+=(it->second);
		printf("%d\n",tot-cnt+1);
	}
	return 0;
}

