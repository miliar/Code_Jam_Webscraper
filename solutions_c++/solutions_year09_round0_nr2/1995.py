#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <iostream>
#include <sstream>
#include <algorithm>

using namespace std;

#define FF first
#define SS second
#define LL long long
#define PL pair<long,long>
#define SoF(x) (long)x.size()
#define FOR(x,y,n) for(x=y;x<n;x++)
#define FR(x,n) FOR(x,0,n)
//#define ROF(x,n,y) for(x=n-1;x>=y;x--)
//#define RF(x,n) ROF(x,n,0)

char lab[100][100];
long alt[100][100];
long n,m;

long lowest(long x,long y){
   if((x<0)||(x>=n)||(y<0)||(y>=m))return -1;
   long d=0,a=alt[x][y];
   if((x-1>=0)&&(alt[x-1][y]<a)){
      d=1;
      a=alt[x-1][y];
   }
   if((y-1>=0)&&(alt[x][y-1]<a)){
      d=2;
      a=alt[x][y-1];
   }
   if((y+1<m)&&(alt[x][y+1]<a)){
      d=3;
      a=alt[x][y+1];
   }
   if((x+1<n)&&(alt[x+1][y]<a)){
      d=4;
      a=alt[x+1][y];
   }
   return d;
}

int main(){
   long i,j,t,tc,x,y,d;
   char l;
   cin>>t;
   stack<PL > work;
   PL pos;
FR(tc,t){
   cin>>n>>m;
   FR(i,n){
      FR(j,m){
         cin>>alt[i][j];
//         cout<<alt[i][j]<<" ";
         lab[i][j]='X';
      }
//      cout<<endl;
   }
   cout<<"Case #"<<tc+1<<": "<<endl;
   l='a';
   FR(i,n){
      FR(j,m){
        if(lab[i][j]=='X'){
         pos.FF=i;
         pos.SS=j;
         work.push(pos);
         while(! work.empty()){
            pos=work.top();
            x=pos.FF;
            y=pos.SS;
//            cout<<x<<"    "<<y<<endl;
            work.pop();
            if(lab[x][y]!=l){
               lab[x][y]=l;
               d=lowest(x,y);
//               cout<<"pos: "<<x<<"x"<<y<<"    lowest: "<<d<<endl;
               switch(d){
                  case 1:
                     pos.FF=x-1; pos.SS=y; work.push(pos); //cout<<"   add: "<<pos.FF<<"x"<<pos.SS<<endl;
                     break;
                  case 2:
                     pos.FF=x; pos.SS=y-1; work.push(pos); //cout<<"   add: "<<pos.FF<<"x"<<pos.SS<<endl;
                     break;
                  case 3:
                     pos.FF=x; pos.SS=y+1; work.push(pos); //cout<<"   add: "<<pos.FF<<"x"<<pos.SS<<endl;
                     break;
                  case 4:
                     pos.FF=x+1; pos.SS=y; work.push(pos); //cout<<"   add: "<<pos.FF<<"x"<<pos.SS<<endl;
                     break;
               }
               if(lowest(x-1,y)==4){
                  pos.FF=x-1; pos.SS=y; work.push(pos);//cout<<"   add: "<<pos.FF<<"x"<<pos.SS<<endl;
               }
               if(lowest(x,y-1)==3){
                     pos.FF=x; pos.SS=y-1; work.push(pos);//cout<<"   add: "<<pos.FF<<"x"<<pos.SS<<endl;
               }
               if(lowest(x,y+1)==2){
                     pos.FF=x; pos.SS=y+1; work.push(pos);//cout<<"   add: "<<pos.FF<<"x"<<pos.SS<<endl;
               }
               if(lowest(x+1,y)==1){
                     pos.FF=x+1; pos.SS=y; work.push(pos);//cout<<"   add: "<<pos.FF<<"x"<<pos.SS<<endl;
               }
            }
            while((! work.empty())&&(lab[work.top().FF][work.top().SS]==l))work.pop();
         }
         l++;
        }
        cout<<lab[i][j]<<" ";
      }
      cout<<endl;
   } 
//   FR(i,n){
 //     FR(j,m){
//         cout<<lab[i][j]<<" ";
//      }
//      cout<<endl;
//   }
}   
   
   return 0;
}
