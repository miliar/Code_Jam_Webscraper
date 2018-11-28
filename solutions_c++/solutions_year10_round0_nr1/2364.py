#include<cstdio>
#include<stack>

using namespace std;

bool solve(void);

int n,m;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int ca = 0 ; ca < t ; ++ca){
		scanf("%d%d",&n,&m);
		printf("Case #%d: ",ca+1);
		if(solve()){
			printf("ON\n");
		}
		else{
			printf("OFF\n");
		}
	}
	return 0;
}

bool solve(void){
	for(int i = 0 ; i < n ; ++i){
		if(m%2){
			m /= 2;
		}
		else{
			return 0;
		}
	}
	return 1;
}
