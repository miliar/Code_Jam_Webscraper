#include "stdio.h"
#include "stdlib.h"
#include "memory.h"
#include "string.h"
#include "math.h"

FILE *fin, *fout;

#define INPUT_FILE_NAME "B-large"
#define INPUT_FILE INPUT_FILE_NAME##".in"
#define OUTPUT_FILE INPUT_FILE_NAME##".out"

#define print(format,...) {fprintf(fout, format, __VA_ARGS__); printf(format, __VA_ARGS__);}

#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define pow2(a) ((a)*(a))

template<class T>
inline void swap(T &a, T &b)
{
	T c;
	c=a;
	a=b;
	b=c;
}

void problem(int nCase);
void init();

void main(int argc, char **argv)
{
	int N,k;
	printf("%s\n", INPUT_FILE);
	fopen_s(&fin, INPUT_FILE, "rt");
	fopen_s(&fout, OUTPUT_FILE, "wt");
	fscanf_s(fin, "%d\n", &N);
	k=0;
	init();
	while(N--)
	{
		++k;
		print("Case #%d: ", k);
		problem(k);
		print("\n");
	}
	fclose(fin);
	fclose(fout);
}

void init()
{
}

typedef struct  
{
	__int64 x,y;
	int top;
}SPos;

void problem(int nCase)
{
	int N,W,L;
	__int64 r[6000];
	SPos pos[6000];
	int index[6000];
	__int64 i,j;
	fscanf_s(fin, "%d", &N);
	fscanf_s(fin, "%d", &W);
	fscanf_s(fin, "%d", &L);
	for (i=0;i<N;++i)
	{
		fscanf_s(fin, "%lld", &r[i]);
		pos[i].top = -1;
		index[i] = i;
	}
	for (i=0;i<N;++i)
	{
		for (j=i+1;j<N;++j)
		{
			if (r[i]<r[j])
			{
				swap(r[i],r[j]);
				swap(index[i],index[j]);
			}
		}
	}
	__int64 x,y;
	bool bTop = false;
	for (i=0;i<N;++i)
	{
		x=y=0;
		if (i>0 && !bTop)
		{
			x = pos[i-1].x+r[i-1]+r[i];
			y = pos[i-1].y;
		}
		if (x>W)
		{
			bTop = true;
		}
		if (bTop)
		{
			for (j=0;j<i;++j)
			{
				if (pos[j].top == -1 && pos[j].y+r[j]+r[i]<L)
					break;
			}
			if (j==i)
			{
				break;
			}
			pos[j].top = i;
			x = pos[j].x;
			y = pos[j].y+r[j]+r[i];
		}
		pos[i].x = x;
		pos[i].y = y;
	}

	for (i=0;i<N;++i)
	{
		if (pos[i].x>W || pos[i].y>L)
			print("kua");
		for (j=i+1;j<N;++j)
		{
			__int64 dis;
			dis = pow2(pos[i].x-pos[j].x)+pow2(pos[i].y-pos[j].y);
			if (dis<pow2(r[i]+r[j]))
				print("kua");
		}
	}

	for (i=0;i<N;++i)
	{
		for (j=0;j<N;++j)
		{
			if (index[j] == i)
			{
				print("%lld %lld ", pos[j].x, pos[j].y);
				break;
			}
		}
	}
}