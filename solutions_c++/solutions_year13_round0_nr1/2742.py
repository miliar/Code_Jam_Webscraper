#include<fstream>
#include<iostream>
#include<sstream>
#include<bitset>
#include<deque>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<vector>
#include<algorithm>
#include<iterator>
#include<string>
#include<cassert>
#include<cctype>
#include<climits>
#include<cmath>
#include<cstddef>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>

#define TIMER 0 
#define MAX 4
#define xwin "X won"
#define owin "O won"
#define draw "Draw"
#define notc "Game has not completed"

using namespace std;

char inp[MAX][MAX];

char * solve(){

		int oc,xc,tc,ec=0;
	    for(int i=0;i<MAX;i++)
		{	oc=0;xc=0;tc=0;
			for (int j=0;j<MAX;j++) 
			{   switch(inp[i][j]){
				case 'O':
					  oc++;break;
				case 'X':
					  xc++;break;
				case 'T':
					  tc++;break;
				case '.':
					  ec++;	break;
				}
			}
			if(oc==4 || (oc==3 && tc==1))
				return owin;
			if(xc==4 || (xc==3 && tc==1))
				return xwin; 
		}

		 for(int i=0;i<MAX;i++)
		{	oc=0;xc=0;tc=0;
			for (int j=0;j<MAX;j++) 
			{   switch(inp[j][i]){
				case 'O':
					  oc++;break;
				case 'X':
					  xc++;break;
				case 'T':
					  tc++;break;
				case '.':
					  ec++;	break;
			}
			}
			if(oc==4 || (oc==3 && tc==1))
				return owin;
			if(xc==4 || (xc==3 && tc==1))
				return xwin; 
		}
		 oc=0;xc=0;tc=0;
		 for(int i=0;i<MAX;i++)
		{	
			switch(inp[i][i]){
				case 'O':
					  oc++;break;
				case 'X':
					  xc++;break;
				case 'T':
					  tc++;break;
				case '.':
					  ec++;	break;
			}
			if(oc==4 || (oc==3 && tc==1))
				return owin;
			if(xc==4 || (xc==3 && tc==1))
				return xwin; 
		}
		 oc=0;xc=0;tc=0;
		 int ix=3,iy=0;
		 for(int l=0;l<MAX;l++)
		 {
			switch(inp[ix--][iy++]){
				case 'O':
					  oc++;break;
				case 'X':
					  xc++;break;
				case 'T':
					  tc++;break;
				case '.':
					  ec++;	break;
			}
			if(oc==4 || (oc==3 && tc==1))
				return owin;
			if(xc==4 || (xc==3 && tc==1))
				return xwin; 
		}
		if(ec==0)
			return draw;
		else
			return notc;
}


int main(){
	int T=0;
	scanf("%d",&T);
	 for(int t=1;t<=T;t++){
	     for(int i=0;i<MAX;i++)
           scanf("%s",&inp[i]);      
		
        printf("Case #%d: %s\n",t,solve());
	}	
	return 0;
}
