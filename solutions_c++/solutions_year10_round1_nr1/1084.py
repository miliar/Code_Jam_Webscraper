#include "stdio.h"
#include "stdlib.h"
#include "string.h"

typedef __int64 int64;
typedef unsigned __int64 u_int64;
typedef unsigned int     u_int;
typedef u_int64  Type;
typedef unsigned char u_char;

const char* getwinner(u_char* pbroad,u_int N,u_int k);


const u_char B    = 'B';
const u_char R    = 'R';
const u_char Spot = '.';

int main(int argc,char* argv[])
{
	if( argc <= 1)
		return printf("need file name as a  parameter!"); 
	FILE* pf = fopen(argv[1],"r");
	if( pf == NULL)
		return printf("cann't open file");

	u_int T = 0;
	fscanf(pf,"%d\n",&T);

	int i=0,j=0,r=0,k=0;
	for(i=0;i<T;i++)
	{
		u_int N=0,K=0;
		fscanf(pf,"%d %d\n",&N,&K);

		u_char* pbroad = new  u_char[N*N];
		char* buf      = new char[N+2];

		memset(pbroad,Spot,N*N);
		for( j=0;j<N;j++)
		{
			fgets(buf,N+2,pf);

			k=N-1;
			for( r=N-1;r>=0;r--)
			{
				if( buf[r] != Spot )
				{
					pbroad[j*N+k] = buf[r];
					k--;
				}
			}
		}

		const char* winner = getwinner(pbroad,N,K);
		printf("Case #%d: %s\n",i+1,winner);

		delete buf;
		delete pbroad;
	}

	fclose(pf);
	return 0;
}

const char* getwinner(u_char* pbroad,u_int N,u_int K)
{
	int i=0,j=0,r=0,k=0;
	int r_R = 0,r_B=0;

	u_char t  = 0;
	bool   wr = false;
	bool   wb = false;

	for(i=N-1;i>=0;i--)
	{
		r_R = 0;
		r_B = 0;
		for(j=N-1;j>=0;j--)
		{
			// row 
			t = pbroad[i*N+j];
			if( t != Spot )
			{
				if( t == B){
					if(r_R>=K)
						wr = true;
					r_R=0;
					r_B++;
				}else{
					if(r_B>=K)
						wb = true;
					r_B=0;
					r_R++;
				}
			}else
			{
				break;
			}
		}
		if( r_B >= K )
			wb = true;
		if( r_R >= K)
			wr = true;
	}

	for(i=N-1;i>=0;i--)
	{
		r_R = 0;
		r_B = 0;
		for(j=N-1;j>=0;j--)
		{
			// row 
			t = pbroad[j*N+i];
			if( t != Spot )
			{
				if( t == B){
					if(r_R>=K)
						wr = true;
					r_R=0;
					r_B++;
				}else{
					if(r_B>=K)
						wb = true;
					r_B=0;
					r_R++;
				}
			}else
			{
				break;
			}
		}
		if( r_B >= K )
			wb = true;
		if( r_R >= K)
			wr = true;
	}

	for(i=0;i<=N-1;i++)
	{
		r_R = 0;
		r_B = 0;
		for(j=0;j<=i;j++)
		{
			// row 
		    r = N-1-(i-j);
			k = N-1-j;
			t = pbroad[r*N+k];
			if( t != Spot )
			{
				if( t == B){
					if(r_R>=K)
						wr = true;
					r_R=0;
					r_B++;
				}else{
					if(r_B>=K)
						wb = true;
					r_B=0;
					r_R++;
				}
			}else
			{
				if(r_R>=K)
					wr = true;
				if(r_B>=K)
					wb = true;
				r_R=0;
				r_B=0;
			}
		}
		if( r_B >= K )
			wb = true;
		if( r_R >= K)
			wr = true;
	}

	for(i=0;i<=N-1;i++)
	{
		r_R = 0;
		r_B = 0;
		for(j=0;j<=i;j++)
		{
			// row 
			r = i-j;
			k = j;
			t = pbroad[r*N+k];
			if( t != Spot )
			{
				if( t == B){
					if(r_R>=K)
						wr = true;
					r_R=0;
					r_B++;
				}else{
					if(r_B>=K)
						wb = true;
					r_B=0;
					r_R++;
				}
			}else
			{
				if(r_R>=K)
					wr = true;
				if(r_B>=K)
					wb = true;
				r_R=0;
				r_B=0;
			}
		}
		if( r_B >= K )
			wb = true;
		if( r_R >= K)
			wr = true;
	}

	for(i=0;i<=N-1;i++)
	{
		r_R = 0;
		r_B = 0;
		for(j=0;j<=i;j++)
		{
			// row 
			r = N-1-(i-j);
			k = j;
			t = pbroad[r*N+k];
			if( t != Spot )
			{
				if( t == B){
					if(r_R>=K)
						wr = true;
					r_R=0;
					r_B++;
				}else{
					if(r_B>=K)
						wb = true;
					r_B=0;
					r_R++;
				}
			}else
			{
				if(r_R>=K)
					wr = true;
				if(r_B>=K)
					wb = true;
				r_R=0;
				r_B=0;
			}
		}
		if( r_B >= K )
			wb = true;
		if( r_R >= K)
			wr = true;
	}

	for(i=0;i<=N-1;i++)
	{
		r_R = 0;
		r_B = 0;
		for(j=0;j<=i;j++)
		{
			// row 
			r = (i-j);
			k = N-1-j;
			t = pbroad[r*N+k];
			if( t != Spot )
			{
				if( t == B){
					if(r_R>=K)
						wr = true;
					r_R=0;
					r_B++;
				}else{
					if(r_B>=K)
						wb = true;
					r_B=0;
					r_R++;
				}
			}else
			{
				if(r_R>=K)
					wr = true;
				if(r_B>=K)
					wb = true;
				r_R=0;
				r_B=0;
			}
		}
		if( r_B >= K )
			wb = true;
		if( r_R >= K)
			wr = true;
	}

	if( wb==true&&wr==true)
		return "Both";
	else if(wb==true)
		return "Blue";
	else if(wr==true)
		return "Red";
	else
		return "Neither";
}