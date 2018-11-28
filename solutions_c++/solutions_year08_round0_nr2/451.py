#include <cstdio>
#include <algorithm>

using namespace std;

#define MAXN 220

int m,n;
int matn[MAXN],matm[MAXN];
bool mrkn[MAXN],mrkm[MAXN];
bool tab[MAXN][MAXN];//adj de n em m

bool match(int v){
    
    int i;
    mrkn[v] = true;
    
    for(i=0;i<m;i++){
        
        if(mrkm[i] || !tab[v][i]) continue;
        /*direto*/
        if(matm[i] < 0){
            matm[i] = v;
            matn[v] = i;
            return true;   
        }
        
        mrkm[i] = true;
        /*remove esse matching e tenta*/
        if(match(matm[i])){
            matm[i] = v;
            matn[v] = i;
            return true;   
        }   
        
    }
    
    return false;   
    
}

/*matching hungaro 0-1, tab construido*/
int hungarian01(){
    
    int i,j;
        
    for(i=0;i<n;i++)
        matn[i] = -1;   
    for(i=0;i<m;i++)
        matm[i] = -1;
        
    for(i=0;i<n;i++){
            
        for(j=0;j<n;j++)
            mrkn[j] = false;   
        for(j=0;j<m;j++)
            mrkm[j] = false;
            
        match(i);
    }
    
    int ret = 0;
    for(i=0;i<n;i++){
        if(matn[i] >= 0) ret++;    
    }
        
    return ret;
    
}

int main(){
    
    int i,j;
    int a,b;
    int na,nb;
    int t,lp;
    int dep[MAXN],arr[MAXN];
    int turn;
    
    scanf("%d",&t);
    
    for(lp=1;lp<=t;lp++){
        scanf("%d",&turn);
        scanf("%d %d",&na,&nb);
        
        n = m = na+nb;
        
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                tab[i][j] = false;    
            }    
        }
        
        for(i=0;i<n;i++){
            scanf("%d:%d",&a,&b);
            dep[i] = 60*a+b;
            scanf("%d:%d",&a,&b);
            arr[i] = 60*a+b;
        }
        
        for(i=0;i<na;i++){
            for(j=na;j<m;j++){
                if(arr[i]+turn <= dep[j]) tab[i][j] = true;    
            }    
        }
        
        for(i=na;i<n;i++){
            for(j=0;j<na;j++){
                if(arr[i]+turn <= dep[j]) tab[i][j] = true;    
            }    
        }
        
        hungarian01();
        
        int ra=na,rb=nb;
        
        for(i=0;i<n;i++){
            if(matn[i] >= 0){
                if(matn[i] < na) ra--;
                else rb--;    
            }    
        }
        
        printf("Case #%d: %d %d\n",lp,ra,rb);
            
    }
    
    return 0;
    
}
