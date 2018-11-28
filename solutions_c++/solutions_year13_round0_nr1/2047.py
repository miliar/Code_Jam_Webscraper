#include <iostream>
#include <cstdio>
#include <algorithm> 
#include <string>
#include <vector>
#include <queue>
#include <functional>
#include <cmath>
#include <sstream>


#define NMAX 4
#define MMAX 10000

typedef long long int ll;



using namespace std;

int main(){ int z,o,j,n,sol,x,i; char c,s[NMAX][NMAX]; bool flag; 
cin>>z;
for (o=0;o<z;o++){sol=-1;
	for(j=0;j<4;j++)for(i=0;i<4;i++){cin>>s[j][i];}
	cout<<"Case #"<<o+1<<": ";
	for(j=0;j<4;j++){ x=0; for(i=0;i<4;i++)if((s[j][i]=='X')||(s[j][i]=='T')) x++; if(x==4) sol=1;}
	for(i=0;i<4;i++){ x=0; for(j=0;j<4;j++)if((s[j][i]=='X')||(s[j][i]=='T')) x++; if(x==4) sol=1;}

	x=0; for(j=0;j<4;j++){if((s[j][j]=='X')||(s[j][j]=='T')) {x++;}}  if(x==4) sol=1; 
	x=0; for(j=0;j<4;j++){if((s[j][3-j]=='X')||(s[j][3-j]=='T')) {x++;}}  if(x==4) sol=1;

	if (sol==1) cout<<"X won";

	for(j=0;j<4;j++){ x=0; for(i=0;i<4;i++)if((s[j][i]=='O')||(s[j][i]=='T')) x++; if(x==4) sol=2;}
	for(i=0;i<4;i++){ x=0; for(j=0;j<4;j++)if((s[j][i]=='O')||(s[j][i]=='T')) x++;  if(x==4) sol=2;}

	x=0; for(j=0;j<4;j++){if((s[j][j]=='O')||(s[j][j]=='T')) {x++;}}  if(x==4) sol=2; 
	x=0; for(j=0;j<4;j++){if((s[j][3-j]=='O')||(s[j][3-j]=='T')) {x++;}}   if(x==4) sol=2;
	
	if (sol==2) cout<<"O won";

	flag=false;
	if (sol==-1){for(j=0;j<4;j++)for(i=0;i<4;i++){if(s[j][i]=='.')flag=true;}
		if (flag==true)cout<<"Game has not completed";else cout<<"Draw";
		}

cout<<"\n"; }
return 0;}

		
