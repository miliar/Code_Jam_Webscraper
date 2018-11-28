#include <cstdio>
#include <iostream>

using namespace std;

int size,tst,test,k,ans;
int a[300][300],b[100][100];
bool nfound,good;

void clear(int s){
    for(int i=0;i<s+1;i++)
        for(int j=0;j<s+1;j++)
            a[i][j] = -1;
}

void set(int x,int y){
    for(int i=0; i<k; i++)
        for(int j=0; j<k; j++)
            a[x+i][y+j] = b[i][j];
}


bool eq2(int a,int b){
    return a==-1 || b==-1 || a==b;
}

bool eq(int x,int y){
//    fprintf(stderr,"<a[%d][%d]==%d, a[%d][%d]==%d> ",x,y,a[x][y],size-x-1,size-y-1,a[size-x-1][size-y-1]);
    return eq2(a[x][y],a[y][x]) && eq2(a[x][y],a[size-1-y][size-1-x]);
}


int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&tst);
    for(int test=1;test<=tst;test++){
        cerr << "!!!!"<<test << " ";
        clear(200);
        scanf("%d",&k);
        for(int i=0;i<2*k-1;i++){
            if(i<k)
                for(int j=0;j<i+1;j++)
                    scanf("%d",&b[j][k-i+j-1]);
            else
                for(int j=0;j<2*k-i-1;j++)
                    scanf("%d",&b[i-k+j+1][j]);//,cerr << b[i-k+j+1][j];
        }        
        nfound = true;
        for(size = k;nfound;size++){
            cerr << size;
            for(int x = 0; (x <= size-k) && nfound==true; x++)
                for(int y = 0; (y <= size-k) && nfound==true; y++){
                    clear(size+1);
//                    cerr <<x<<y;
                    set(x,y);
                    good = true;
                    
                         
                            //~ for(int q=0;q<size;q++){
            //~ for(int w=0;w<size;w++)
                //~ fprintf(stderr,"%3d",a[q][w]);
                    //~ fprintf(stderr,"\n");
        //~ }
                    //~ fprintf(stderr,"\n");
                    
                    
                    for(int q=0; q<size && good; q++)
                        for(int w=0; w<size && good; w++){
                            good &= eq(q,w);
//                            if (!eq(q,w))
//                                cerr <<q<<w<<"fail ";
                        }
                    if(good){
                        nfound = false;
                        ans = size;
                        y=1000;x=1000;
                        continue;
                    }                    
                }
            }
        cerr << k << " "<<ans <<"\n";
        printf("Case #%d: %d\n",test,ans*ans-k*k);
    }
}
