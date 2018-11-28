#include <cstdio>
#include <cstring>
using namespace std;

int N,C[1000];

int rec(int loc, int a, int b, int suma, int sumb)
{
	if(loc == N)
	{
		if(a == b && suma > 0 && sumb > 0)
			return suma;
		else
			return -1;
	}
	
	int x = rec(loc+1,a^C[loc],b,suma+C[loc],sumb);
	int y = rec(loc+1,a,b^C[loc],suma,sumb+C[loc]);
	if(x > y)
		return x;
	return y;
}

void process_case()
{
	int check = rec(0,0,0,0,0);
	if(check == -1)
		printf("NO\n");
	else
		printf("%d\n", check);
}


void handle_input()
{
	scanf("%d", &N);
	for(int i = 0; i < N; i++)
		scanf("%d", &C[i]);
}



int main()
{
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++)
	{
		handle_input();
		printf("Case #%d: ", i);
		process_case();
	}
}