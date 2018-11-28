

#include <iostream>
using namespace std;

int ardat[100][100];
int arcon[100][100];
char ans[100][100];

int n,m,i,ii,mini,temp;
int col,wid;
char cur;

void rec(int y, int x)
{
     ans[y][x] = cur;
     
     if((arcon[y][x]%2==1)&&(ans[y-1][x]=='A')) rec(y-1,x);
     if(((arcon[y][x]>>1)%2==1)&&(ans[y][x-1]=='A')) rec(y,x-1);
     if(((arcon[y][x]>>2)%2==1)&&(ans[y][x+1]=='A')) rec(y,x+1);
     if(((arcon[y][x]>>3)%2==1)&&(ans[y+1][x]=='A')) rec(y+1,x);
 }

int main(){
    
    cin >> n;
    m = 1;
    while(n--){
    printf("Case #%d:\n",m);
    m++;
               
     cin >> col;
     cin >> wid; 
     cur = 'a';
     
     for(i=0;i<col;i++)
      for(ii=0;ii<wid;ii++)
      {
      cin >> ardat[i][ii];
      arcon[i][ii] = 0;
      ans[i][ii] = 'A';
      }
      
     for(i=0;i<col;i++)
      for(ii=0;ii<wid;ii++)
      {
      mini = 10000;
      temp = 0;
      
      if((i>0)&&(ardat[i-1][ii]<ardat[i][ii])&&(ardat[i-1][ii]<mini))
      {
       temp = 1;
       mini = ardat[i-1][ii]; 
      }

      if((ii>0)&&(ardat[i][ii-1]<ardat[i][ii])&&(ardat[i][ii-1]<mini))
      {
       temp = 2;
       mini = ardat[i][ii-1]; 
      }
      
      if((ii<(wid-1))&&(ardat[i][ii+1]<ardat[i][ii])&&(ardat[i][ii+1]<mini))
      {
       temp = 4;
       mini = ardat[i][ii+1]; 
      }
      
      if((i<(col-1))&&(ardat[i+1][ii]<ardat[i][ii])&&(ardat[i+1][ii]<mini))
      {
       temp = 8;
       mini = ardat[i+1][ii]; 
      }
      
      arcon[i][ii] += temp;
      
      if(temp==1) arcon[i-1][ii]+=8;
      if(temp==2) arcon[i][ii-1]+=4;
      if(temp==4) arcon[i][ii+1]+=2;
      if(temp==8) arcon[i+1][ii]+=1;
      
      }
     
     for(i=0;i<col;i++)
      for(ii=0;ii<wid;ii++)
     {
         if(ans[i][ii] == 'A')
         {
         rec(i,ii);
         cur++;
         }                  
     }
     
     for(i=0;i<col;i++)
      for(ii=0;ii<wid;ii++)
      {cout << ans[i][ii];
      if(ii==wid-1) cout << '\n';
      else cout << ' ';}
    }
    
    
}
