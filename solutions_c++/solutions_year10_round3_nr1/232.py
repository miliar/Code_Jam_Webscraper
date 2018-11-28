
#include <stdlib.h>
#include <stdio.h>

struct Line {
/*public:
	Line() {}*/

	int a, b;
};


int N=0;
Line* lines;



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

		lines = new Line [N];

		for(int i=0; i<N; ++i)
		{
			scanf("%d %d", &lines[i].a, &lines[i].b);
		}

		return true;
	}
	else
		return false;
}

inline int sign(int m)
{
	return (m>=0)?1:0;
}

int main()
{
	for(int ncase=1; get_input(); ++ncase)
	{
		int count = 0;
		//fprintf(stderr, "\nCase #%d\n", ncase); fflush(stderr);
		printf("Case #%d: ", ncase);

		for(int i=0; i<N; ++i)
		{
			for(int j=i+1; j<N; ++j)
			{
				if (sign(lines[i].a-lines[j].a)!=sign(lines[i].b-lines[j].b))
					count++;
			}
		}

		printf("%d\n", count);

		delete [] lines;
	}

	return 0;
}