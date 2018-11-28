#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cstring>

using namespace std;
#define sz 10005

long table[sz+5];
bool g[sz][sz];

long find(long a,long b){
    long i,j,k,l,pro,ans = 0,rec,len,cnt;
    char tmp[10],ch;
    for( i = a; i <= b; i++){
        table[i] = 0;
    }
    for(i=a; i<= b; i++){
        for(j=a; j<= b; j++){
            g[i][j] = false;
        }
    }

    for(i = 1; i <= 9; i++){
        pro = i;
        while(pro <= b){
            table[pro] = -1;
            pro *= 10;
            pro += i;
        }
    }
    for(i=a; i <= b; i++){
        if(table[i] != -1){
            sprintf(tmp,"%ld",i);
            len = strlen(tmp);
            cnt = len - 1;
            while(cnt--){
                ch = tmp[len-1];
                for(j=len-1; j >= 1; j--){
                    tmp[j] = tmp[j-1];
                }
                tmp[0] = ch;
                if(tmp[0] != '0'){
                    rec = atol(tmp);
                    if(rec >= a && rec <= b && rec != i){
                        if( !g[i][rec] ){
                            ans++;
                            //printf("%ld >> %ld\n",i,rec);
                            g[i][rec] = g[rec][i] = true;
                        }
                    }
                }
            }
        }
    }
    return ans;
}


int main(){
    long t,i,j,k,l,cas=1,rec,a,b;

    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);

    scanf("%ld",&t);
    getchar();

    while(t--){
        scanf("%ld %ld",&a,&b);
        printf("Case #%ld: ",cas++);
        printf("%ld\n",find(a,b));
    }

    return 0;
}
