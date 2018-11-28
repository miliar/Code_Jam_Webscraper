#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#define LL (long long int)

using namespace std;


int t,h,w,res,resost=0;
int T[105][105];
int BYL[105][105];
int IN[105][105];
set<long long int> M;
set<int> S;

void idz(int x,int y,int a)
{
     // cout<<"idz"<<x<<" "<<y<<endl; 
     int kier=0;
     if(T[x][y-1]<a){kier=1; a=T[x][y-1];}
     if(T[x-1][y]<a){kier=2; a=T[x-1][y];}
     if(T[x+1][y]<a){kier=3; a=T[x+1][y];}
     if(T[x][y+1]<a){kier=4; a=T[x][y+1];}
    if(!BYL[x][y]) {S.insert(x+1000*y); BYL[x][y]=1;}
     if(kier==0){ if(IN[x][y]==0){resost++; res=resost; IN[x][y]=res;} else res=IN[x][y];}
     else
     switch(kier)
     {
     case 1: idz(x,y-1,a);   break;  
     case 2: idz(x-1,y,a);   break;   
     case 3: idz(x+1,y,a);   break;   
     case 4: idz(x,y+1,a);   break;      
                 
     }  
    return; 
}

int main(int argc, char *argv[])
{
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
     scanf("%d%d", &h,&w);  
     for(int k=0;k<=h;k++){T[0][k]=999999;T[w+1][k]=999999;}
     for(int k=0;k<=w;k++){T[k][0]=999999;T[k][h+1]=999999;}
      for(int y=1;y<=h;y++)
      for(int x=1;x<=w;x++)
     { IN[x][y]=0; BYL[x][y]=0;}
     resost=0;
      M.clear(); S.clear();
     for(int y=1;y<=h;y++)
             for(int x=1;x<=w;x++)
                      {
                                  scanf("%d",&T[x][y]);
                                  M.insert(-(LL(T[x][y])*10000000+x+1000*y));
                      }
             
          while(!M.empty())
          {
          S.clear();
     
          int x=abs(*M.begin())%1000;                 
          int y=abs((*M.begin())%10000000)/1000;                 
          int a=abs(*M.begin())/10000000;
        //  cout<<x<<" "<<y<<endl;
          idz(x,y,a);
          // cout<<"HOP";
          while(!S.empty())
          {
               M.erase(M.find(-(LL(10000000)*T[*S.begin()%1000][*S.begin()/1000]+(*S.begin()%1000)+1000*(*S.begin()/1000))));
               IN[*S.begin()%1000][*S.begin()/1000]=res;
               S.erase(S.begin());
          }
          }
      printf("Case #%d:\n",i);  
      char CHAR[30];
      for(int i=1;i<30;i++)CHAR[i]='7';
     // CHAR[IN[1][1]]='a';
      char ost='a'-1; 
      for(int y=1;y<=h;y++)
              {
               for(int x=1;x<=w;x++)  {
                       if(CHAR[IN[x][y]]!='7') 
                       printf("%c ",CHAR[IN[x][y]]);
               else
                    {
                      ost++;
                      CHAR[IN[x][y]]=ost;    
                      printf("%c ",CHAR[IN[x][y]]);  
                     }
                 //    cout<<IN[x][y];
                     }
      printf("\n");
                   }   
           
    }
    
    
   // system("PAUSE");
    return EXIT_SUCCESS;
}
