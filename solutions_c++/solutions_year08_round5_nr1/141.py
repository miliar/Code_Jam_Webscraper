#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

const int maxn=3300;
char maz[maxn*2+1][maxn*2+1];

int gi(){
    int t; scanf(" %d ",&t);
    return t;
}

vector<char> route;
void readRoute(){
    route.clear();
    for(int n=gi(); n--;){
        char buf[34];
        int r;
        scanf(" %s %d ", buf, &r);
        for(;r--;){
            for(int i=0; buf[i]!=0; i++)
                route.push_back(buf[i]);
        }
    }
}

int count(char c){
    int cnt=0;
    for(int i=0; i<route.size(); i++)
        cnt+=(route[i]==c);
    return cnt;
}

int main(){
    for(int test=1, t=gi(); test<=t; test++){
        readRoute();
        int rcou=count('R'), lcou=count('L');
        int ox[]={0,1,0,-1}, oy[]={1,0,-1,0};
        int x=maxn, y=maxn, d=0;;
        //memset(
        int sumf=0;
        int mix=1000000, miy=1000000, mx=-1000000, my=-1000000;
        for(int i=0; i<route.size(); i++){
            if(route[i]=='F'){
                if(rcou>lcou){
                    if(d==0)
                        maz[x][y]=1;
                    else if(d==1)
                        maz[x][y-1]=1;
                    else if(d==2)
                        maz[x-1][y-1]=1;
                    else if(d==3)
                        maz[x-1][y]=1;
                }
                else if(rcou<lcou){
                    if(d==0)
                        maz[x-1][y]=1;
                    else if(d==1)
                        maz[x][y]=1;
                    else if(d==2)
                        maz[x][y-1]=1;
                    else if(d==3)
                        maz[x-1][y-1]=1;
                }
                else 
                    cerr<<"mamy problem: rcou==lcou"<<endl;

                if(d==0)
                    sumf+=x;
                else if(d==2)
                    sumf-=x;
                
                x+=ox[d];
                y+=oy[d];
            }
            else if(route[i]=='R')
                d=(d+1)%4;
            else
                d=(d+3)%4;

            mix=min(mix,x);
            miy=min(miy,y);
            mx=max(x,mx);
            my=max(y,my);
        }

        mix-=10;
        miy-=10;
        mx+=9;
        my+=9;

        sumf=abs(sumf);
        for(int y=miy; y<my; y++){
            for(int x=mix; x<mx; x++)
                if(maz[x][y]<=0)
                    maz[x][y]--;
                else if(maz[x][y]==1)
                    break;
            for(int x=mx-1; x>=mix; x--)
                if(maz[x][y]<=0)
                    maz[x][y]--;
                else if(maz[x][y]==1)
                    break;
        }
        for(int x=mix; x<mx; x++){
            //cout<<x<<endl;
            for(int y=miy; y<my; y++)
                if(maz[x][y]<=0)
                    maz[x][y]--;
                else if(maz[x][y]==1)
                    break;
            for(int y=my-1; y>=miy; y--)
                if(maz[x][y]<=0)
                    maz[x][y]--;
                else if(maz[x][y]==1)
                    break;
        }
        /*
         for(int y=miy-2; y<=my+2; y++){
            for(int x=mix-2; x<=mx+2; x++)
                cout<<maz[x][y];
            cout<<endl;
        }
        */
         int cf=0;
         for(int y=miy; y<my; y++)
            for(int x=mix; x<mx; x++)
                if(maz[x][y]>=-1)
                    cf++;
         printf("Case #%d: %d\n", test, cf-sumf);
         for(int y=miy-2; y<=my+2; y++)
            for(int x=mix-2; x<=mx+2; x++)
                maz[x][y]=0;
       //cout<<sumf<<endl;
       // for(int x=0; x<2*maxn+1; x++)
            //for(int y=0; y<2*maxn+1; y++)

    }
    return 0;
}
