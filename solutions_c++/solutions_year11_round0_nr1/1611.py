#include<iostream>
#include<cstring>
#include<cstdio>

using namespace std;

int b,o,lastb,lasto,incer,banyak,kasus;
char kata[5];

int abso(int x)
{
	if (x >= 0) return x;
	return -x;
}

int main()
{
	scanf("%d",&kasus);
	for (int l=1;l<=kasus;l++)
	{
		b = o = 0;
		lastb = lasto = 1;
		scanf("%d",&banyak);
		
		for (int i=0;i<banyak;i++)
		{
			scanf("%s",kata);
			scanf("%d",&incer);
			if (kata[0] == 'O')
			{
				int jauh = abso(incer-lasto);
				o = max(b,o+jauh)+1;
				lasto = incer;
			}
			else
			{
				int jauh = abso(incer-lastb);
				b = max(o,b+jauh)+1;
				lastb = incer;
			}
		}
		
		printf("Case #%d: %d\n",l,max(b,o));
	}
	return 0;
}
