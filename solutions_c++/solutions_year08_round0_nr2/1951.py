#include <iostream>
#include <algorithm>

using namespace std;


struct point{
	int a,b;
} res;

struct state{
	int time;
	bool begin,A;
} trains[100];

int len,T;


void run()
{
	res.a=0;
	res.b=0;
	int a = 0, b = 0;
	for(int i=0; i<len; i++)
	{
		if(trains[i].A)
		{
			if(trains[i].begin)
			{
				if(a!=0)
					a--;
				else
					res.a++;
			}
			else
				a++;
		}
		else
		{
			if(trains[i].begin)
			{
				if(b!=0)
					b--;
				else
					res.b++;
			}
			else
				b++;
		}
	}
}


int bool_to_int(bool x)
{
	if(x)
		return 0;
	else
		return 1;
}


void push_stdin(bool begin, bool A)
{
	int h,m;
	scanf("%d:%d",&h,&m);
	trains[len].A=A;
	trains[len].begin=begin;	
	trains[len++].time=h*60+m+T*bool_to_int(begin);
}


void get_stdin(bool flag)
{
	push_stdin(true,flag);
	push_stdin(false,!flag);
}


bool cmp(const state & A, const state & B)
{
	return A.time<B.time || ( A.time==B.time &&  !A.begin && B.begin);
}


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test_count;
	scanf("%d",&test_count);
	for(int test_num=1; test_num<=test_count; test_num++)
	{
		int na,nb;
		scanf("%d %d %d\n",&T,&na,&nb);
		len = 0;
		for(int i=0; i<na; i++)
			get_stdin(true);
		for(int i=0; i<nb; i++)
			get_stdin(false);
		sort(trains,trains+len,cmp);
		run();
		printf("Case #%d: %d %d\n",test_num,res.a,res.b);
	}		
	return 0;
}