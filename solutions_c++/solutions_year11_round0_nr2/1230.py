#include<iostream>
#include<map>

using namespace std;

int base_elements[]={'Q','W','E','R','A','S','D','F'};
char combine[256][256];
char opposite[256];
int counter[256];
char els[10000];
int N;

void clear_counter(){
    for(int i=0;i<sizeof(base_elements)/sizeof(base_elements[0]);i++)
        counter[base_elements[i]]=0;
}

void clear_all(){
    N=0;
    int n=sizeof(base_elements)/sizeof(base_elements[0]);
    clear_counter();
    for(int i=0;i<256;i++){
        opposite[i]=' ';
        for(int j=0;j<256;j++)
            combine[i][j]=' ';
    }
}

int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("x.out","w",stdout);
    int tc,c,d,n;
    char x,y,z;
    scanf("%d",&tc);
    for(int t=1;t<=tc;t++){
        clear_all();
        scanf("\n%d%c",&c,&x);
        for(int i=0;i<c;i++){
            scanf("%c%c%c",&x,&y,&z);
            combine[x][y]=z;
            combine[y][x]=z;
        }
        scanf("%d%c",&d,&x);
        for(int i=0;i<d;i++){
            scanf("%c%c",&x,&y);
            opposite[x]=y;
            opposite[y]=x;
        }
        scanf("%d%c",&n,&x);
        for(int i=0;i<n;i++){
            scanf("%c",&x);
            els[N++]=x;
            counter[x]++;
            if(N>1){
                y=els[N-2];
                z=combine[x][y];
                if(z==' '){
                    z=opposite[x];
                    if(z!=' '&&counter[z]>0){
                        N=0;
                        clear_counter();
                    }
                }
                else{
                    counter[x]--;
                    counter[y]--;
                    els[N-2]=z;
                    N--;
                }
            }
        }
        printf("Case #%d: [",t);
        for(int i=0;i<N;i++)
            if(i)printf(", %c",els[i]);
            else printf("%c",els[i]);
        printf("]\n");
    }
    return 0;
}
