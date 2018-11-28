
// (c) Alvaro Salmador 2010

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int N=0;


bool get_input()
{
	static int T = -1;
	
	if (T<0)
		scanf("%d", &T);
	
	if (T>0)
	{
		--T;

		if (scanf("%d", &N)!=1)
			return false;

		return true;
	}
	else
		return false;
}

int count=0;


inline int search(unsigned char* buffer, int len, unsigned char s)
{
	for(int i=0; i<len; ++i) //OPT
		if (buffer[i]==s)
			return i;

	return -1;
}

inline bool isOk(unsigned char* buffer, int len)
{
	if (len==0) return true;
	static bool bb[25];
	for (int i=0; i<len; ++i) bb[i]=false;
	int i;
	for(i=len-1; i>0; i=search(buffer,len,i+1))
	{
		if (bb[i]) break;
		bb[i] = true;
	}

	if (i==0) return true; else return false;
}

void solve(int len, int min, unsigned char* _buffer)
{
	unsigned char buffer[25]; //OPT?
	if (_buffer!=NULL) { for(int z=0; z<len; ++z) buffer[z]=_buffer[z]; }

	//for(int i=len; i<=N; ++i)
	int i;
	if (len==0) i=2; else i=buffer[len-1]+1;
	for(; i<=N; ++i)
	{
		buffer[len] = i;
		if (isOk(buffer,len+1))  //OPT?
			if (i==N) { count++; if (count==100003) count=0; break; }
		solve(len+1, i+1, buffer);
	}
}

int solution[501];

int main()
{
	for(int i=0; i<501; ++i)
		solution[i] = -1;

	for(int ncase=1; get_input(); ++ncase)
	{
		//fprintf(stderr, "\nCase #%d\n", ncase); fflush(stderr);

		if (solution[N]>=0)
			count = solution[N];
		else 
		{
			count = 0;
			solve(0,2,0);
			solution[N] = count;
		}
		printf("Case #%d: %d\n", ncase, count);
	
	}

	return 0;
}

