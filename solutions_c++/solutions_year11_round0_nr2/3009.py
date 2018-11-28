#include<stdio.h>

char combine[256][256], opposed[256][256];

int f(char x)
{
	return (int)x;
}

class Stack
{
public:
	char vector[101];
	int top;
	Stack()
	{
		top = 0;
	}

	int Combining()
	{
		if(combine[f(vector[top])][f(vector[top-1])]!=0)
		{
			vector[top-1] = combine[f(vector[top])][f(vector[top-1])];
			top--;
			return 1;
		}
		return 0;
	}

	void Clear()
	{
		top = 0;
	}

	void Clearing()
	{
		for(int i = top - 1; i > 0; i--)
		{
			if(opposed[f(vector[top])][f(vector[i])] == 1)
				Clear();
		}
	}

	void Push(char x)
	{
		top++;
		vector[top] = x;
		if(!Combining())
		{
			Clearing();
		}
	}

	char Pop()
	{
		top--;
		return vector[top+1];
	}

	void Show()
	{
		printf("[");
		if(top>0)
		{
			printf("%c", vector[1]);
			for(int i = 2; i <= top; i++)
			{
				printf(", %c", vector[i]);
			}
		}
		printf("]\n");
	}

};

void init()
{
	for(int i = 0; i<256; i++)
		for(int j = 0; j<256; j++)
		{
			opposed[i][j] = 0;
			combine[i][j] = 0;
		}
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	scanf("%d",&T);
	for(int cases = 1; cases <= T; cases++)
	{
		init();
		int C, D, N;
		Stack Q;
		char comb[4], op[3], full[101];
		scanf("%d",&C);
		if(C>0)
		{
			for(int i = 0; i<C; i++)
			{
				scanf("%s", comb);
				combine[f(comb[0])][f(comb[1])] = comb[2];
				combine[f(comb[1])][f(comb[0])] = comb[2];
			}
		}
		scanf("%d",&D);
		if(D>0)
		{
			for(int i = 0; i<D; i++)
			{
				scanf("%s", op);
				opposed[f(op[0])][f(op[1])] = 1;
				opposed[f(op[1])][f(op[0])] = 1;
			}
		}
		scanf("%d",&N);
		if(N>0)
			scanf("%s", full);

		for(int i = 0; i<N; i++)
		{
			Q.Push(full[i]);
		}

		printf("Case #%d: ", cases);
		Q.Show();
		//algorithm
	}
	return 0;
}