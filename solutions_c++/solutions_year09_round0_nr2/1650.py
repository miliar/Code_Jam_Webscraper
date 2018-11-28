#include <iostream>
using namespace std;

const int maxsize = 101;

const int setsize = maxsize*maxsize;
int set[setsize];
char color[setsize];

void build()
{
    for(int i=0;i<setsize;++i){
        set[i] = -1;
        color[i] = '.';
    }
}

void join(int c1,int r1,int c2,int r2)
{
    int i = c1*maxsize+r1;
    int j = c2*maxsize+r2;

   if( set[i]<set[j] ){
       set[i] = j;
   }else{
       if(set[i]==set[j])
           set[i]--;
       set[j]=i;
   }
}

int find(int c,int r)
{
    int i = c*maxsize+r;

    while( set[i]>0 ){
        i = set[i];
    }

    return i;
}

int map[maxsize][maxsize];

void solve()
{
    int t;
    cin>>t;

    int case_cnt = 0;

    while(t--){
        int h,w;
        cin>>h>>w;
        for(int i=1;i<=h;++i){
            for(int j=1;j<=w;++j){
                cin>>map[i][j];
            }
        }

        build();

        for(int r=1;r<=h;++r){
            for(int c=1;c<=w;++c){
                int lc = c;
                int lr = r;
                if( (r-1)>=1&&(r-1)<=h){
                    if( map[r-1][c]<map[lr][lc] ){
                        lr = r-1;
                        lc = c;
                    }
                } 

                if( (c-1)>=1&&(c-1)<=w){
                    if( map[r][c-1]<map[lr][lc] ){
                        lc = c-1;
                        lr = r;
                    }
                } 
                
                if( (c+1)>=1&&(c+1)<=w){
                    if( map[r][c+1]<map[lr][lc] ){
                        lc = c+1;
                        lr = r;
                    }
                } 

                if( (r+1)>=1&&(r+1)<=h){
                    if( map[r+1][c]<map[lr][lc]){
                        lr = r+1;
                        lc = c;
                    }
                } 

                if( lr!=r||lc!=c){
                    join(lc,lr,c,r);
                }
            }
        } // end of build graph

        cout<<"Case #"<<++case_cnt<<": "<<endl;
        char ch = 'a';

        for(int r=1;r<=h;++r){
            for(int c=1;c<=w;++c){
                int t = find(c,r);
                if(color[t]=='.'){
                    color[t] = ch;
                    ch++;
                }
                if(c==1)
                    cout<<color[t];
                else
                    cout<<" "<<color[t];
            }
            cout<<endl;
        }
    }
}


int main()
{
    solve();
}



