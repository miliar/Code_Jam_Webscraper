#include<iostream>
#include<cstdio>
#include<fstream>
#include<algorithm>
#include<cmath>
#include<vector>
#include<map>
#include<cstring>
#include<math.h>
#include<string>

using namespace std;

struct node{
      int x,y;
};
node a[200];
int tot,p[2],t[2],n;
string s;

int main(){
      freopen("A-large.in","r",stdin);
      freopen("out.txt","w",stdout);
      cin>>tot;
      for (int ca=1;ca<=tot;ca++){
            cin>>n;
            for (int i=1;i<=n;i++){
                  char c; 
                  int k;
                  cin>>c>>k;
                  a[i].x=k;
                  a[i].y=(c=='O');
            }
            p[0]=p[1]=1;
            t[0]=t[1]=0;
            int ans=0;
            for (int i=1;i<=n;i++){
                  int time;
                  int turn=a[i].y;
                  int other=turn^1;
                  if (abs(a[i].x-p[turn])>t[turn]) time=abs(a[i].x-p[turn])-t[turn]; else time=0;
                  t[turn]=0;
                  p[turn]=a[i].x;
                  time+=1;
                  ans+=time;
                  t[other]+=time;
            }
            cout<<"Case #"<<ca<<": "<<ans<<endl;
      }
}
