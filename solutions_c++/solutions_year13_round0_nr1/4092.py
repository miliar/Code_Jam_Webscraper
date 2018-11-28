#include<cstdio>
#include <cctype>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
#include <deque>
#include <math.h>
#include<stdio.h>
#include<memory.h>
using namespace std;


typedef stringstream ss;
typedef vector<string> vs;
typedef vector<int> vi;
typedef long long int64;

#define PI 3.14159265
#define pb push_back
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define fornm(i,n,m) for (int i=n; i<=(int)(m); i++)
#define forn(i,n) for (int i=0; i<(int)(n); i++)
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)

int dx[]={1,1,0},dy[]={0,1,1};
#define MAXIMO 10000

int main()
{
	//freopen("A-small-attempt0.in", "r", stdin); 	freopen("respuestaS.out", "w+", stdout);

	freopen("A-large.in", "r", stdin);  	freopen("respuestaLL.out", "w+", stdout);

    int T, n;
    string vacio;
    cin>>T;
    string str;
    char V[4][4];
    
    fornm(tc,1,T)
    {
	  int N;
     
     memset(V,'.',sizeof(V));
     int jt=0;
     int pts =0;
     forn(i,4)
     {
        
        cin >> str;
        forn(j,4)
       {
          V[i][j]=str[j];       
        if(str[j]=='.')
         pts++;
        }
     }
	 int contO=0;
	 int contX=0;
	 int contL = 0; 
	 bool ganador = false;
	 forn(i,4)
	 {
		  contO=0;
		  contX=0;
		  forn(j,4)
		   {
		   	if(V[i][j]=='O' || V[i][j]=='T')contO++;
		   	if(V[i][j]=='X' || V[i][j]=='T')contX++;
		   }
	   if(contO==4)
	   {
	   	 cout<<"Case #"<<tc<<": O won";
	   	 ganador=true;
	   	 break;
	   }
	   else if(contX==4)
	   {
	   	 cout<<"Case #"<<tc<<": X won";
	   	 ganador=true;
	   	 break;
	   }
	 }
	if(!ganador)
	{
		forn(j,4)
		 {
			  contO=0;
			  contX=0;
			  forn(i,4)
			   {
			   	if(V[i][j]=='O' || V[i][j]=='T')contO++;
			   	if(V[i][j]=='X' || V[i][j]=='T')contX++;
			   }
		   if(contO==4)
		   {
		   	 cout<<"Case #"<<tc<<": O won";
		   	 ganador=true;
		   	 break;
		   }
		   else if(contX==4)
		   {
		   	 cout<<"Case #"<<tc<<": X won";
		   	 ganador=true;
		   	 break;
		   }
		 }	
	}
	if(!ganador)
	{
		 contO=0;
		contX=0;
		forn(i,4)
		{
			   	if(V[i][i]=='O' || V[i][i]=='T')contO++;
			   	if(V[i][i]=='X' || V[i][i]=='T')contX++;
		}
		if(contO==4)
		   {
		   	 cout<<"Case #"<<tc<<": O won";
		   	 ganador=true;
		   }
		 else  if(contX==4)
		   {
		   	 cout<<"Case #"<<tc<<": X won";
		   	 ganador=true;
		   }
		
	}
	if(!ganador)
	{
		contO=0;
		contX=0;
		forn(i,4)
		{
			   	if(V[i][3-i]=='O' || V[i][3-i]=='T')contO++;
			   	if(V[i][3-i]=='X' || V[i][3-i]=='T')contX++;
		}
		if(contO==4)
		   {
		   	 cout<<"Case #"<<tc<<": O won";
		   	 ganador=true;
		   }
		 else  if(contX==4)
		   {
		   	 cout<<"Case #"<<tc<<": X won";
		   	 ganador=true;
		   }
		
	}
	if(!ganador && pts==0)
	  cout<<"Case #"<<tc<<": Draw";
	else if(!ganador && pts!=0)
	  cout<<"Case #"<<tc<<": Game has not completed";
	  
	  cout<<endl;
	 
	}
	
	return 0;
}
