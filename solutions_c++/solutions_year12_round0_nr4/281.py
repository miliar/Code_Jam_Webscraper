#include <iostream>
#include <cmath>
#include <string>
#include <deque>
#include <algorithm>

using namespace std;

int n,m,d;
char map[40][40];

#define MAX 300

short field[MAX][MAX];

deque<int> X;
deque<int> Y;
bool used[MAX][MAX];
int dx[]={-1,1,0,0};
int dy[]={0,0,-1,1};

int Abs(int x){
    return (x>=0)?x:-x;    
}

int Nod(int a,int b){
    if (!b) return a;
    else return Nod(b,a%b);    
}

int GetCell(int n,int m,int lx,int ly,int x,int y,int typ){
    if (typ==2 || typ == 3){
        return field[lx+x][ly+m-y-1];
    }    
    if (typ==0 || typ==1){
        return field[lx+n-x-1][ly+y];    
    }   
    
    return 0; 
}

int main(void){
    freopen("D-small-attempt1.in","r",stdin);
    //freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    int test;
    scanf("%i",&test);
    
    
    for (int z=0;z<test;z++){
        scanf("%i %i %i\n",&n,&m,&d);
        
        for (int i=0;i<n;i++){
            for (int j=0;j<m;j++) scanf("%c",&map[i][j]);
            scanf("\n");    
        } 
        int D = 2*d;
        for (int i=0;i<MAX;i++)
            for (int j=0;j<MAX;j++) used[i][j]=field[i][j]=0;
        
        int posx=0;
        int posy=0;
        
        for (int i=1;i<n-1;i++){
            for (int j=1;j<m-1;j++){
                field[D+i-1][D+j-1]=(map[i][j]=='X')?1:2;
                if (map[i][j]=='X'){
                    posx=D+i-1;
                    posy=D+j-1;    
                }    
            }    
        }
        int N = n-2;
        int M = m-2;
        
        //reflections

        used[D][D]=1;
        X.push_back(D);
        Y.push_back(D);
        while (X.size()>0){
            int xx = X.front();
            X.pop_front();
            int yy = Y.front();
            Y.pop_front();
            for (int k=0;k<4;k++){
                int nx = xx + dx[k]*N;
                int ny = yy + dy[k]*M;
                if (nx>=0 && ny>=0 && nx+N<MAX && ny+M<MAX && !used[nx][ny]){
                    X.push_back(nx);
                    Y.push_back(ny);
                    used[nx][ny]=1;
                    for (int i=0;i<N;i++)
                        for (int j=0;j<M;j++){
                            field[nx+i][ny+j]=GetCell(N,M,xx,yy,i,j,k);    
                        }
                }                    
            }                        
        }
        
        
        //Check images
        int ans = 0;
        int d2 = d*d;
        for (int i=D-d;i<D+N+d;i++)
            for (int j=D-d;j<D+M+d;j++){
                if (!(i>=D && j>=D && i<D+N && j<D+M)){
                    if (field[i][j]&1){
                        int dist = ((i-posx)*(i-posx)+(j-posy)*(j-posy));
                        if (d2<dist) continue;
                        

                        int DelX = -i+posx;
                        int DelY = -j+posy;
                        int dd = Nod(Abs(DelX),Abs(DelY));
                        DelX=DelX/dd;
                        DelY=DelY/dd;
                        int xxx = i + DelX;
                        int yyy = j + DelY;    
                        bool yes = true;
                        //printf("first [%i,%i] = %i\n",xxx,yyy,field[xxx][yyy]);
                        while (!(xxx==posx && yyy==posy)){
                            //printf("! [%i,%i] = %i\n",xxx,yyy,field[xxx][yyy]);
                            if (field[xxx][yyy]&1){                                
                                yes = false;    
                            }        
                            xxx+=DelX;
                            yyy+=DelY;
                        }                        
                        if (yes){
                            //printf("%i,%i -> %i %i\n",i,j,posx,posy);
                            ans++;
                            //printf("%i %i\n",DelX,DelY);
                            field[i][j]=3;    
                        }
                    }        
                }
            }
        
        /*for (int i=0;i<50;i++){
            for (int j=0;j<50;j++){
                printf("%i",(int)field[i][j]);                    
            }    
            printf("\n");
        }*/

        
        printf("Case #%i: ",z+1);
        printf("%i\n",ans);
    }    
    
    return 0;    
}
