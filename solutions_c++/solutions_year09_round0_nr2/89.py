#include<iostream>
#include<fstream>
using namespace std;
int g[110][110];
char c[110][110];
char table[27];
int now;
int t,h,w;
int x[5],y[5];
char solve(int l , int m )
 {
  if (c[l][m]!='=') return c[l][m];
  int minus=10000000;
  int ok=0;
 // cout<<"l="<<l<<"m="<<m<<endl;
  for (int i=1 ; i<= 4 ; i++)
   {
   	  	 if  (l+x[i] < 1 || l+x[i]>h)  continue;
	     if  (m+y[i]<1   || m+y[i]>w )  continue;
	 
   	  	if (g[l+x[i]][m+y[i]]<g[l][m] && g[l+x[i]][m+y[i]]<minus )
		   {	 minus=g[l+x[i]][m+y[i]];
		         ok=i;
		   }   
    
   } 	
     // cout<<"ok="<<ok<<endl;
	 //    getchar();  
   if (ok==0) {now++ ; c[l][m]=table[now]; return table[now];}
   else { c[l][m]=solve(l+x[ok],m+y[ok]); return c[l][m];};
 }
int main()
 { ifstream fin;
 fin.open("b.in");
 ofstream  fout;
 fout.open("b.out");
    fin>>t;
    x[1]=-1; y[1]=0;
    x[2]=0; y[2]=-1;
    x[3]=0; y[3]=1;
    x[4]=1; y[4]=0;
    for (int i=1; i<= 26; i++)
     {
	  table[i] = 'a'+i-1;		 
     }
	for( int  test = 1; test <= t; test++)
	 {
	  	 fin>>h>>w;
	  	 now=0;
	  	 memset(c,'=',sizeof(c));
	  	 for (int i = 1; i <= h ;i++)
	  	     for (int j = 1; j <= w ; j++ )
	  	      {
			   	 fin>>g[i][j];  
     
				  };
   	 	      
   	 	   for (int i = 1 ; i<= h; i++)
	        for (int j = 1 ; j <= w ;j++)
	   	      {
			    if (c[i][j]=='=') 
			    	c[i][j]=solve(i,j);	  	  	        
		       }  
			   fout<<"Case #"<<test<<":"<<endl; 
		     for (int i = 1 ; i<= h; i++)
		     {
     	        for (int j = 1 ; j <= w ;j++)   
		             fout<<c[i][j]<<" " ;      
			fout<<endl;
			 }
		   }		  
 //system("pause");
 }
