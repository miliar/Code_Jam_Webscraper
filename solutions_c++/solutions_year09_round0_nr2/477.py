#include<iostream>
using namespace std;
int arr[100][100],H,W,cnt;
char label[100][100];
bool vis[100][100];
bool if_min(int x,int y,int x1,int y1){
     int mn=arr[x][y];
     int posx=-1,posy=-1;
     if(x-1>=0 && arr[x-1][y]<mn)
     posx=x-1,posy=y,mn=arr[x-1][y];
     if(y-1>=0 && arr[x][y-1]<mn)
     posx=x,posy=y-1,mn=arr[x][y-1];
     if(y+1<W && arr[x][y+1]<mn)
     posx=x,posy=y+1,mn=arr[x][y+1];
     if(x+1<H && arr[x+1][y]<mn)
     posx=x+1,posy=y,mn=arr[x+1][y];
     if(posx==x1 && posy==y1)
     return true;
     return false;}
     
void start_labeling(int x,int y){
     label[x][y]=(char)('a'+cnt);
     vis[x][y]=true;
     if(x-1>=0 && arr[x-1][y]>arr[x][y] && if_min(x-1,y,x,y))
     start_labeling(x-1,y);
     if(y-1>=0 && arr[x][y-1]>arr[x][y] && if_min(x,y-1,x,y))
     start_labeling(x,y-1);
     if(y+1<W && arr[x][y+1]>arr[x][y] && if_min(x,y+1,x,y))
     start_labeling(x,y+1);
     if(x+1<H && arr[x+1][y]>arr[x][y] && if_min(x+1,y,x,y))
     start_labeling(x+1,y);}
     
void find_sink(int x,int y){
     label[x][y]=(char)('a'+cnt);
     vis[x][y]=true;
     int mn=arr[x][y];
     int posx=-1,posy=-1;
     if(x-1>=0 && arr[x-1][y]<mn && !vis[x-1][y])
     posx=x-1,posy=y,mn=arr[x-1][y];
     if(y-1>=0 && arr[x][y-1]<mn && !vis[x][y-1])
     posx=x,posy=y-1,mn=arr[x][y-1];
     if(y+1<W && arr[x][y+1]<mn && !vis[x][y+1])
     posx=x,posy=y+1,mn=arr[x][y+1];
     if(x+1<H && arr[x+1][y]<mn && !vis[x+1][y])
     posx=x+1,posy=y,mn=arr[x+1][y];
     if(posx==-1)
     start_labeling(x,y);
     else
     find_sink(posx,posy);}
     
     
int main(){
    int T,cs;
    cin>>T;
    for(cs=0;cs<T;cs++){
    int i,j;
    cin>>H>>W;
    for(i=0;i<H;i++){
    for(j=0;j<W;j++){
    cin>>arr[i][j];
    vis[i][j]=false;}}
    cnt=0;
    for(i=0;i<H;i++){
    for(j=0;j<W;j++){
    if(!vis[i][j]){
    find_sink(i,j);
    cnt++;}}}
    cout<<"Case #"<<cs+1<<": \n";
    for(i=0;i<H;i++){
    for(j=0;j<W;j++){
    cout<<label[i][j];
    if(j<W-1)
    cout<<" ";}
    cout<<"\n";}}}
    
    
                     
    
