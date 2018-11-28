#include <fstream>
#include <iostream>
#include <vector>
#include <string>
using namespace std;


long long min3(long long a,long long b,long long c)
{
   return a*b*c;
 }
 long long Ca3(long long a)
 { return a*(a-1)*(a-2)/6;
 }
int main(int argc,char* argv[])
{
    ifstream ifs(argv[1]);
    ofstream ofs(strcat(argv[1],".out"));
    int N;
    ifs>>N; 
    int i,j;
    for(i=0;i<N;i++)
    {long long grid[3][3]={{0,0,0},{0,0,0},{0,0,0}};
     
     long long n,A,B,C,D,x0,y0,M;
     ifs>>n>>A>>B>>C>>D>>x0>>y0>>M;
    
     grid[x0%3][y0%3]++;
       long long X=x0,Y=y0;
      for(j=0;j<n-1;j++) 
      {X = (A * X + B) % M;
       Y = (C * Y + D) % M;
       grid[X%3][Y%3]++;
      }
      long long sum=0;
      sum+=min3(grid[0][0],grid[0][1],grid[0][2]);
      sum+=min3(grid[1][0],grid[1][1],grid[1][2]);
      sum+=min3(grid[2][0],grid[2][1],grid[2][2]);
     
      sum+=min3(grid[0][0],grid[1][0],grid[2][0]);
      sum+=min3(grid[0][1],grid[1][1],grid[2][1]);
      sum+=min3(grid[0][2],grid[1][2],grid[2][2]);
      
       
      sum+=min3(grid[0][0],grid[1][1],grid[2][2]);
      sum+=min3(grid[0][1],grid[1][2],grid[2][0]);
      sum+=min3(grid[1][0],grid[2][1],grid[0][2]);
        
      sum+=min3(grid[0][2],grid[1][1],grid[2][0]);
      sum+=min3(grid[0][1],grid[1][0],grid[2][2]);
      sum+=min3(grid[0][0],grid[2][1],grid[1][2]);
     
      sum+=Ca3(grid[0][0]); sum+=Ca3(grid[0][1]); sum+=Ca3(grid[0][2]);
      sum+=Ca3(grid[1][0]); sum+=Ca3(grid[1][1]); sum+=Ca3(grid[1][2]);
      sum+=Ca3(grid[2][0]); sum+=Ca3(grid[2][1]); sum+=Ca3(grid[2][2]);
    
   //  vector<int> tmp(NS);
       ofs<<"Case #"<<i+1<<": "<<sum<<endl;
          
    }
    ifs.close();
    ofs.close();
    cout<<"press any key to continue\n";
    getchar();
}
