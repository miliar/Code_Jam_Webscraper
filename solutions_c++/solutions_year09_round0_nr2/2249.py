#include<iostream>
using namespace std;
#include<fstream>
#include<stdio.h>
//#include<algorithm>
//#include<conio.h>

enum{ north, west, east, south, sink};

void flush(int a[101][101], int x, int y)
{
   for(int i=0; i<x; i++)
     for(int j=0; j<y; j++)
       a[i][j]=-1;
   return;     
}
     
int main()
{
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    
    char ch;
    int N,x,y,n,w,e,s, min,val,ctr, p,q;
    int a[101][101], b[101][101], ans[101][101];
    
//    flush(a,101,101);
    
    fin>>N;
    
    for(int c=1; c<=N; c++)
    {
        fin>>x>>y;

        flush(a,x,y);
        flush(b,x,y);
        flush(ans,x,y);
        
        for(int i=0; i<x; i++)
          for(int j=0; j<y; j++)
             fin>>a[i][j];
        
        for(int i=0; i<x; i++)
        {
          for(int j=0; j<y; j++)
          {
              min = a[i][j];
              val = sink;
              if(i>0 && a[i-1][j] < min)
              {
                     min = a[i-1][j];
                     val = north;
              }
              if(j>0 && a[i][j-1] < min)
              {
                     min = a[i][j-1];
                     val = west;
              }
              if(j<y-1 && a[i][j+1] < min)
              {
                     min = a[i][j+1];
                     val = east;
              }
              if(i<x-1 && a[i+1][j] < min)
              {
                     min = a[i+1][j];
                     val = south;
              }
              b[i][j] = val;
          }
        }

        for(int i=0; i<x; i++)
        {
          for(int j=0; j<y; j++)
		cout<<b[i][j]<<" ";
          cout<<"\n";
        }
        ctr = -1;
        for(int i=0; i<x; i++)
        {
          for(int j=0; j<y; j++)
          {
                 if(ans[i][j] > -1)
                        continue;
                 p = i; q = j;       
                 
                 while(b[i][j] != sink)
                 {
                        switch(b[i][j])
                        {
                             case north : i--; break;
                             case west : j--; break;
                             case east : j++; break;
                             case south : i++; break;
                        }
                 }

                 if(ans[i][j] == -1)
                     ans[i][j] = ++ctr;
                 val = ans[i][j];
                     
                 i = p, j = q;
                 while(b[i][j] != sink)
                 {
                        ans[i][j] = val;
                        switch(b[i][j])
                        {
                             case north : i--; break;
                             case west : j--; break;
                             case east : j++; break;
                             case south : i++; break;
                        }
                 }
                 i = p, j = q;
          }
        }         
            
        fout<<"Case #"<<c<<":\n";
        for(int i=0; i<x; i++)
        {
            for(int j=0; j<y-1; j++)
            {
		    ch = 'a'+ans[i][j];
                    fout<<ch<<" ";
            }
	    ch = 'a'+ans[i][y-1];
            fout<<ch<<"\n";
        }
        
    }
    
//    getch();        
    return 0;
}
