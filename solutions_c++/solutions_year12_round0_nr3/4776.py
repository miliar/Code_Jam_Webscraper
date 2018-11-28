#include<cstdio>
#include<vector>
#define MAX 2000005
using namespace std;

int t,A,B,i,j,k,l,m,res;
bool vis[MAX];
vector<int> f,s;

int main(){
    scanf("%d",&t);
    for(i=1; i<=t; ++i){
	printf("Case #%d: ",i);
	res=0;
	scanf("%d%d",&A,&B);
	for(j=A; j<=B; ++j)
	    for(k=j+1; k<=B; ++k){
	    int a=k;
	    int b=j;
	    f.clear();
	    s.clear();
	    while(a>0){
		f.push_back(a%10);
		a/=10;
	    }
	    while(b>0){
		s.push_back(b%10);
		b/=10;
	    }
	    for(l=0; l<f.size(); ++l) s.push_back(s[l]);
	    for(l=0; l<f.size(); ++l){
		int ile=0;
		for(m=0; m<f.size(); ++m)
		    if(f[m]==s[l+m]) ++ile;
		if(ile==f.size()){
		    ++res;
		    break;
		}
	    }
	    
	}
	printf("%d\n",res);
    }
    return 0;
}