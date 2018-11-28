#include <iostream>
#include <fstream>
using namespace std;

void main()
{ 
  ofstream outfile( "A-large.out" );
  ifstream infile( "A-large.in" );
  int t, n, i, j, butc, time, lefttime, tmp,curO,curB;
  int but[200];
  char bot[200];
  char c;
  infile>>t;
  for (i=1;i<=t;i++)
  {
    infile>>n;
    for (j=1; j<=n; j++){infile>>c>>butc; bot[j]=c; but[j]=butc;};
    time = 0;
    lefttime = 0;
    curO = curB =1;
    for (j=1; j<=n;j++)
    { 
      if (bot[j]=='O')
      { tmp=j+1;
        while((bot[tmp]!='B')&&(tmp<=n)) tmp++;
        //if (tmp<=n)  
        if (but[j]==curO) 
        { time = time +1;
          if (tmp<=n)
          { if (but[tmp]>curB) curB++;
            if (but[tmp]<curB) curB--;
          };
        }
        else 
        { time =time +1+abs(but[j]-curO); 
		  lefttime = 1+abs(but[j]-curO);
		  curO=but[j];
          if (tmp<=n)
          { if (lefttime>=abs(but[tmp]-curB))
            {curB=but[tmp];}
            else
            { if (but[tmp]>curB) curB+=(lefttime);
              if (but[tmp]<curB) curB-=(lefttime);
            }
          }   
        };
      }
      else
      {tmp=j+1;
        while((bot[tmp]!='O')&&(tmp<=n)) tmp++;
        //if (tmp<=n)  
        if (but[j]==curB) 
        { time = time +1;
          if (tmp<=n)
          { if (but[tmp]>curO) curO++;
            if (but[tmp]<curO) curO--;
          };
        }
        else 
        { time =time +1+abs(but[j]-curB); 
		  lefttime = 1+abs(but[j]-curB);
		  curB=but[j];
          if (tmp<=n)
          { if (lefttime>=abs(but[tmp]-curO))
            {curO=but[tmp];}
            else
            { if (but[tmp]>curO) curO+=(lefttime);
              if (but[tmp]<curO) curO-=(lefttime);
            };
          };
        };     
      };
        
        
        
      };
      outfile<<"Case #"<<i<<": "<<time<<endl; 
    };
  };