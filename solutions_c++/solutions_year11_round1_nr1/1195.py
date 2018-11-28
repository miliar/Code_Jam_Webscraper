#include <stdio.h>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>
#include <limits.h>


using namespace std;
int ni() { int a; scanf( "%d", &a ); return a; }
double nf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; string ns() { scanf( "%s", sbuf ); return sbuf; }
long long nll() { long long a; scanf( "%lld", &a ); return a; }

int T,Pd,Pg,pd,pg;
__int64 N;

deque<__int64> poss();

int by100(int n){
	if(n%2 == 0){
		n /=2;
		if(n%2 == 0){
			n /=2;
		}
	}
	if(n%5 == 0){
		n /= 5;
		if(n%5 == 0){
			n /= 5;
		}
	}
	return n;
}

void result(bool res,int t){
	printf( "Case #%d:", t + 1);
	if(res){
		printf(" %s\n", "Possible");
	}else{
		printf(" %s\n", "Broken");
	}
}

int main( )
{
	freopen( "D:\\input.txt", "r", stdin );
	freopen( "D:\\output.txt", "w", stdout );
	T = ni();
	for(int t = 0; t < T; ++ t )
	{
		N = nll();
		Pd = ni();
		Pg = ni();
		if(Pd == 0) 
			if(Pg == 100) 
			{result(false,t); continue; }
			else
			{result(true,t); continue;}
		if(Pd == 100) 
			if(Pg ==0) 
			{result(false,t); continue; }
			else
			{result(true,t); continue;}

		pd = by100(Pd);
		pg = by100(Pg);
		__int64 temp = N * Pd / 100 / pd * pd;
		if(temp == 0)
			{result(false,t);continue;}
		else
		{
			if(Pg == 100)
				{result(false,t); continue; }
			if(Pg == 0)
				{result(false,t); continue; }
			{result(true,t); continue; }
		}

	}
	return 0;
}
