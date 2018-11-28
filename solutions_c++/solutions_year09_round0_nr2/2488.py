#include <iostream>
using namespace std;

int map[105][105];
int map2[105][105];
int H,W;

bool is_basin(int i,int j){
    if(map[i-1][j]<map[i][j])return false;
    if(map[i+1][j]<map[i][j])return false;
    if(map[i][j-1]<map[i][j])return false;
    if(map[i][j+1]<map[i][j])return false;
    return true;
}
bool flow(int i,int j,int i2,int j2){
    int a=map[i][j],b=map[i2][j2];
    if(a<=b)return false;
    if(i>0&&map[i-1][j]<b)return false;
    if(i<H&&map[i+1][j]<b)return false;
    if(j>0&&map[i][j-1]<b)return false;
    if(j<W&&map[i][j+1]<b)return false;

    if(i>0&&map[i-1][j]==b){
        if(i-1!=i2||j!=j2)
        return false;
        return true;
    }
    if(j>0&&map[i][j-1]==b){
        if(i!=i2||j-1!=j2)
        return false;
        return true;
    }
    if(j<W&&map[i][j+1]==b){
        if(i!=i2||j+1!=j2)
        return false;
        return true;
    }
    return true;
}
void mark(int i,int j){
    if(map2[i-1][j]==0&&flow(i-1,j,i,j)){
        map2[i-1][j]=map2[i][j];
        if(i-1!=0)mark(i-1,j);
    }
    if(map2[i][j-1]==0&&flow(i,j-1,i,j)){
        map2[i][j-1]=map2[i][j];
        if(j-1!=0)mark(i,j-1);
    }
    if(map2[i][j+1]==0&&flow(i,j+1,i,j)){
        map2[i][j+1]=map2[i][j];
        if(j!=W)mark(i,j+1);
    }
    if(map2[i+1][j]==0&&flow(i+1,j,i,j)){
        map2[i+1][j]=map2[i][j];
        if(i!=H)mark(i+1,j);
    }
}
int main(){
    int N;
    cin>>N;
    for(int i=0;i<N;++i){
            cin>>H>>W;
            char c[30];
            memset(c,0,sizeof(c));
            for(int j=0;j<=H+1;++j){
                for(int k=0;k<=W+1;++k){
                    map2[j][k]=0;
                    if(j==0||j==H+1||k==0||k==W+1){
                        map[j][k]=1000000;
                        continue;
                    }
                    cin>>map[j][k];
                }
            }
            int basin=1;
            for(int j=1;j<=H;++j){
                for(int k=1;k<=W;++k){
                    if(is_basin(j,k)==true){
                        map2[j][k]=basin++;
                        mark(j,k);
                    }
                }
            }
            cout<<"Case #"<<i+1<<":"<<endl;
            basin='a';
            c[map2[1][1]]=basin++;
            for(int j=1;j<=H;++j){
                for(int k=1;k<=W;++k){
                    if(c[map2[j][k]]>='a')
                    cout<<c[map2[j][k]]<<" ";
                    else {
                        c[map2[j][k]]=basin++;
                        cout<<c[map2[j][k]]<<" ";
                    }
                }
                cout<<endl;
            }
    }
    return 0;
}
