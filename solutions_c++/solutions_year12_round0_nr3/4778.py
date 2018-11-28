#include<iostream>
#include<fstream>
#include <cstdlib>
#include <conio.h>


using namespace std;

void testword(string s);
int inset(int x, int a)
{
	int j, tests, countss ,b;
	for(j = 1; j <= tests; j++)
	{
	countss = 0;
	cin >> a >> b;
	}
}


int main()
{
    int tests = 0,i,l,l1,l2,j;
    cin >> tests;
    int a,b,z,x,c,t,countss=0;
    fstream fout("output.txt", ios::out);

/*inputting */
for(j = 1; j <= tests; j++)
{
	countss = 0;
	cin >> a >> b;
	
for(i=a;i<=b;i++)
{
	int p=i;
	t=0;
	int q[3]={0,0,0};
	
    
    while(t!=3)
	{
	q[t]=p%10;
	p=p/10;
	t++;
	}
	
	int sca, src;
	src = 0;
	for(sca=0; sca < 10; sca++)
	           src++;
	
	if(q[2]==0&&q[1]!=0)
	{
	z=q[1]*10+q[0];
	x=q[1]+q[0]*10;
	if((z>i&&z<=b))
	{countss++;}
	if((x>i&&x<=b))
	{countss++;}
	}
	else if(q[2]!=0)
	{
	
	z=q[2]*100+q[1]*10+q[0];
	x=q[1]*100+q[0]*10+q[2];
	c=q[0]*100+q[1]+q[2]*10;
	
    
    if((z>i&&z<=b))
	{countss++;}
	
    if(x>i&&x<=b)
	{countss++;}
	
    if((c>i&&c<=b))
	{countss++;}
	
	}
	
	
}
fout <<"Case #"<<(j)<<": "<<countss<< "\n";
}

return 0;
}
	

