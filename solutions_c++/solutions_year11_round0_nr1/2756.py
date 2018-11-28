#include <cstdio>
using namespace std;

int n,na,nb;
int A[1000],B[1000];
bool isA[1000];

void process_case()
{
	int last_ta = 0;
	int last_tb = 0;
	int loca = 1, locb = 1;
	int idxa = 0, idxb = 0;
	int dist;
	int tot_time = 0;
	for(int i = 0; i < n; i++)
	{
		if(isA[i])
		{
			dist = A[idxa]-loca;
			loca = A[idxa++];
			if(dist < 0)
				dist *= -1;
			int t = tot_time - last_ta;
			dist -= t;
			if(dist < 0)
				dist =0;
			tot_time += dist+1;
			last_ta = tot_time;
		}
		else
		{
			dist = B[idxb]-locb;
			locb = B[idxb++];
			if(dist < 0)
				dist *= -1;
			int t = tot_time - last_tb;
			dist -= t;
			if(dist < 0)
				dist = 0;
			tot_time += dist+1;
			last_tb = tot_time;
		}
		//printf("%d %d %d %d %d\n", loca, last_ta, locb, last_tb, tot_time);
	}
	printf("%d\n", tot_time);
}


void handle_input()
{
	na = 0;
	nb = 0;
	scanf("%d", &n);
	
	int x;
	char s[4];
	for(int i = 0; i < n; i++)
	{
		scanf("%s %d", s, &x);
		if(s[0] == 'B')
		{
			isA[i] = true;
			A[na++] = x;
		}
		else
		{
			isA[i] = false;
			B[nb++] = x;
		}
	}
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