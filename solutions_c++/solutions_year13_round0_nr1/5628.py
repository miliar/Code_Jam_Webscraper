#include <iostream>
#include <string.h>
#include <stdio.h>
using namespace std;

char  a[6][6];
int b[6][6],c[6][6],dot;
int dig[2],row[4],col[4];
#define F(i) for(i=1;i<5;i++)
void check()
{   int i,j;
	F(i)
		{
		F(j)
			{
			if(a[i-1][j-1]=='X')
			    {
			      b[i][j]+=b[i][j-1]+1; 
			      c[i][j]+=c[i-1][j]+1;
			       		
			    }
			else if(a[i-1][j-1]=='O')
			    {
			    	b[i][j]+=b[i][j-1]-1;
			    	c[i][j]+=c[i-1][j]-1;
			    }
			else if(a[i-1][j-1]=='T')
				{
					if(b[i][j-1] > 0) b[i][j]+=b[i][j-1]+1;
					else if (b[i][j-1] < 0) b[i][j] += b[i][j-1] - 1;
					if(c[i-1][j] >0 ) c[i][j]+=c[i-1][j]+1;
					else c[i-1][j]+=c[i-1][j]-1;

				}
			else 
			    {
			    dot=1;
			    b[i][j]+=b[i][j-1];
			    c[i][j]+=c[i-1][j];
			    }

			}
		}


}




int main()
{
int t=0,i=0,j,test=1;
string s;
getline(cin,s);
while(s[i]!='\0')
	{t=t*10 + s[i]-'0';i++;}
//cout<<t;
while(test<=t)
{
dot=0;
memset(b,0,36*sizeof(int));
memset(c,0,36*sizeof(int));
for(i=0;i<4;i++)
gets(a[i]);
check();/*
for(i=0;i<4;i++)
{
	for(j=0;j<4;j++) {cout<<b[i+1][j+1]<<" ";}
	cout<<"\n";
} 

for(i=0;i<4;i++)
{
	for(j=0;j<4;j++) {cout<<c[i+1][j+1]<<" ";}
	cout<<"\n";
} */

cout<<"Case #"<<test<<": ";
int f=1;
for(i=1;i<=4;i++)
{if(b[i][4]==4 ||c[4][i]==4)
     {cout<<"X won\n";f=0;break;}
 else if(b[i][4]==-4|| c[4][i]==-4)
 	 {cout<<"O won\n";f=0;break;}
 else if( b[i][4]==3 && a[i-1][0]=='T' )
 	 {cout<<"X won\n";f=0;break;}
 else if( b[i][4]==-3 && a[i-1][0]=='T' )
 	 {cout<<"O won\n";f=0;break;}
 else if( c[4][i]==3 && a[0][i-1]=='T' )
 	 {cout<<"X won\n";f=0;break;}
 else if( c[4][i]==-3 && a[0][i-1]=='T' )
 	 {cout<<"O won\n";f=0;break;}
}
if(f){
i=0;
while(i<4)
{	if(a[i][i]=='X'|| a[i][i]=='.')
    break;
    i++;
}
if(i==4)  {cout<<"O won\n";f=0;}
else if(f)
{
	i=0;
while(i<4)
{	if(a[i][i]=='O'|| a[i][i]=='.')
    break;
    i++;
}
if(i==4)  {cout<<"X won\n";f=0;}
} 
}

//for another diagonal...
if(f){
i=0;
while(i<4)
{	if(a[i][3-i]=='X'|| a[i][3-i]=='.')
    break;
    i++;
}
if(i==4)  {cout<<"O won\n";f=0;}
else if(f)
{
	i=0;
while(i<4)
{	if(a[i][3-i]=='O'|| a[i][3-i]=='.')
    break;
    i++;
}
if(i==4)  {cout<<"X won\n";f=0;}
} 
}


if(f && dot) cout<<"Game has not completed";
else if(f) cout<<"Draw\n";
cout<<" "<<f;
getline(cin,s);
test++;
}
cin>>t;
	

}