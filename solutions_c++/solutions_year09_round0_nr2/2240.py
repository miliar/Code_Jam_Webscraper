#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int T;
int H,W;

int m[102][102];
char a[102][102];
bool v[102][102];
char bj;
int s_x, s_y;

int min_neighbor(int i, int j){
    int min= 1<<20;
    if(min>m[i-1][j])
        min=m[i-1][j];
    if(min>m[i+1][j])
        min=m[i+1][j];
    if(min>m[i][j+1])
        min=m[i][j+1];
    if(min>m[i][j-1])
        min=m[i][j-1];
    return min;
}

void find_sink(int i, int j, char c){
    int min_n=min_neighbor(i,j);
//    cout<<i<<' '<<j<<' '<<min_n<<' '<<c<<endl;
   
    a[i][j]=c;
    if(m[i][j]<=min_n){
        s_x=i, s_y=j;
        return;
    }

    if((i-1)>=1 && (i-1)<=H){
        if(m[i-1][j]==min_n){
            find_sink(i-1, j, c);
            return;
        }
    }
    
    if((j-1)>=1 && (j-1)<=W){
        if(m[i][j-1]==min_n){
            find_sink(i, j-1, c);
            return;
        }
    }
    
    if((j+1)>=1 && (j+1)<=W){
        if(m[i][j+1]==min_n){
            find_sink(i, j+1, c);
            return;
        }
    }
    
    if((i+1)>=1 && (i+1)<=H){
        if(m[i+1][j]==min_n){
            find_sink(i+1, j, c);
            return;
        }
    }    
}

void find_range(int i, int j, char c){   
    v[i][j]=true;
    a[i][j]=c;    
    if((i+1)>=1 && (i+1)<=H && v[i+1][j]==false){
        if(m[i][j]==min_neighbor(i+1, j)
           && m[i][j]<m[i+1][j])
            find_range(i+1, j, c);
    }
    if((j+1)>=1 && (j+1)<=W && v[i][j+1]==false){
        if(m[i][j]==min_neighbor(i, j+1)
           && m[i][j]<m[i-1][j+1]
           && m[i][j]<m[i][j+1])
            find_range(i, j+1, c);
    }
    if((j-1)>=1 && (j-1)<=W && v[i][j-1]==false){
        if(m[i][j]==min_neighbor(i, j-1)
           && m[i][j]<m[i-1][j-1]
           && m[i][j]<m[i][j-2]
           && m[i][j]<m[i][j-1])
            find_range(i, j-1, c);
    }
    if((i-1)>=1 && (i-1)<=H && v[i-1][j]==false){
        if(m[i][j]==min_neighbor(i-1, j)
           &&m[i][j]<m[i-2][j]
           &&m[i][j]<m[i-1][j-1]
           &&m[i][j]<m[i-1][j+1]
           && m[i][j]<m[i-1][j])
            find_range(i-1, j, c);
    }
}
int main()
{
    ifstream in("B-large.in");
//    ifstream in("sample.in");
    
    in>>T;
    for(int i=1;i<=T;i++){
        in>>H>>W;
        for(int j=1;j<=H;j++){
            for(int k=1;k<=W;k++){
                in>>m[j][k];
//                cout<<m[j][k]<<' ';
            }
//            cout<<endl;
        }
        for(int j=0;j<=H;j++)
            m[j][0]=100010, m[j][W+1]=100010;
        for(int j=0;j<=W;j++)
            m[0][j]=100010, m[H+1][j]=100010;
        memset(a,0,sizeof(a));
        memset(v,0,sizeof(v));
        bj='a';
        for(int j=1;j<=H;j++){
            for(int k=1;k<=W;k++){
                if(v[j][k]==false){
                    find_sink(j,k,bj);
                    find_range(s_x,s_y,bj);
                    bj=bj+1;
                }
            }
        }

        cout<<"Case #"<<i<<":"<<endl;
        for(int j=1;j<=H;j++){
            for(int k=1;k<W;k++){
                cout<<a[j][k]<<' ';
            }
            cout<<a[j][W]<<endl;
        }
    }
    return 0;
}
