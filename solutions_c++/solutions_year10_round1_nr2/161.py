#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXN = 110;
const int MAXC = 256;
const int INF = 1000000000;

int resp[MAXN][1+MAXC];

int mdif(int a,int b){
    if(a > b){
	return mdif(b,a);
    }
    return (b-a);
}

int escada(int a,int b,int m){
    if(a > b){
	return escada(b,a,m);
    }
    
    if(a == b){
	return 0;
    }
    
    return (b-a-1)/m;
}

int main(){
    int t;
    scanf("%d",&t);
    
    for(int lp=1;lp<=t;++lp){
	int cd,ci,m,n;
	scanf("%d %d %d %d",&cd,&ci,&m,&n);
	vector<int> col(n);
	for(int i=0;i<n;++i){
	    scanf("%d",&col[i]);
	}
	
	for(int i=0;i<n;++i){
	    for(int j=0;j<=MAXC;++j){
		resp[i][j] = INF;
	    }
	}
	
	for(int i=0;i<MAXC;++i){
	    resp[0][i] = mdif(i,col[0]);
	}
	resp[0][MAXC] = cd;
	
	for(int i=0;i<n-1;++i){
	    for(int j=0;j<MAXC;++j){
		resp[i+1][j] = min(resp[i+1][j],resp[i][j] + cd); //deletando pixel i+1
		
		if(m == 0){ //soh pode mudar o i+1 pra cor j
		    resp[i+1][j] = min(resp[i+1][j],resp[i][j] + mdif(j,col[i+1]));
		}
		else{
		    for(int k=0;k<MAXC;++k){ //cor k no pixel i+1
			resp[i+1][k] = min(resp[i+1][k],resp[i][j] + mdif(k,col[i+1]) + ci*escada(j,k,m));
		    }
		}
	    }
	    resp[i+1][MAXC] = resp[i][MAXC] + cd;
	    for(int k=0;k<MAXC;++k){
		resp[i+1][k] = min(resp[i+1][k],resp[i][MAXC] + mdif(k,col[i+1]));
	    }
	    
	}
	
	int ret = INF;
	for(int i=0;i<=MAXC;++i){
	    ret = min(ret,resp[n-1][i]);
	}
	
	printf("Case #%d: %d\n",lp,ret);
	
    }
    
    return 0;
}