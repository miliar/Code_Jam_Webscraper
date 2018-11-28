#include <stdio.h> 
#include <stdlib.h> 
#include <ctype.h> 
#include <string.h> 
#include <math.h> 
#include <algorithm>
#include <functional>
#include <vector> 
#include <set>
#include <queue>
#include <string> 
#include <iostream> 
#include <sstream>  
using namespace std; 

#define fo(i,n) for(i=0;i<(n);++i)
#define fo1(i,y,n) for(i=y; i<(n) ;i++)
#define pb push_back

typedef vector<int> vi ; 
typedef vector<string> vs ; 
typedef vector<double> vd ;  

int main()
{
	FILE *in=fopen("A-large.in","r");
	FILE *out=fopen("output.txt","w");
	int q,Q,n,N,O,B,m1;
	char ch[5];
	fscanf(in,"%d",&q);
	for(Q=1;Q<=q;Q++)
	{
		int Opos = 1;
		int Bpos = 1;
		int ans = 0;
		B=0;
		O=0;
		fscanf(in,"%d",&n);
		for(N=0; N<n; N++)
		{
			fscanf(in,"%s%d",ch,&m1);
			if(ch[0]=='O')
			{
				if(B==0)
				{
					ans += abs( Opos - m1)+1;
					O += abs( Opos - m1)+1;
				}
				else if(abs( Opos - m1)>B)
				{
					ans += abs( Opos - m1)-B+1;
					O += abs( Opos - m1)-B+1;
					B = 0;
				}
				else 
				{
					ans++;
					O = 1;
					B=0;
				}
				Opos = m1;
			}
			else
			{
				if(O==0)
				{
					ans += abs( Bpos - m1)+1;
					B += abs( Bpos - m1)+1;
				}
				else if(abs( Bpos - m1)>O)
				{
					ans += abs( Bpos - m1)-O+1;
					B += abs( Bpos - m1)-O+1;
					O = 0;
				}
				else 
				{
					ans++;
					O=0;
					B = 1;
				}
				Bpos = m1;
			}
		}
		fprintf(out,"Case #%d: %d\n",Q,ans);
	}
	return 0;
}















