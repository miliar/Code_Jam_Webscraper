#include <cstdio>
#include <vector>
#include <string>
#include <sstream>
#include <stdlib.h>
#include <iostream>
#include <math.h>
#include <cstring>
#include <ctype.h>

#define inputfilename "a.in"
#define outputfilename "a.out"
#define maxn 15000

using namespace std;

struct node
{
	int g , c;
	int v1,v2;
	int hash;
}a[10005];

int n , v;

int tru(int point)
{
	int res;
	if (a[point].g)
	{
		res = a[point*2].v1+a[point*2+1].v1;
	}//AND
	else
	{
		int r1 = a[point*2].v1+a[point*2+1].v1;
		int r2 = a[point*2].v1+a[point*2+1].v2;
		int r3 = a[point*2].v2+a[point*2+1].v1;
		r1 = min (r1,r2);
		r1 = min (r1,r3);
		res = r1;
	}//OR
	return res;
}
int fal(int point)
{
	int res;
	if (!a[point].g)
	{
		res = a[point*2].v2+a[point*2+1].v2;
	}//OR
	else
	{
		int r1 = a[point*2].v2+a[point*2+1].v2;
		int r2 = a[point*2].v1+a[point*2+1].v2;
		int r3 = a[point*2].v2+a[point*2+1].v1;
		r1 = min (r1,r2);
		r1 = min (r1,r3);
		res = r1;
	}//AND
	return res;
}
int search(int point)
{
	if (a[point].hash) return 0;
	a[point].hash = 1;
	search(point*2);
	search(point*2+1);
	
	if (!(point == 1 && v == 0))
	{
		int r1 = tru(point);
		int r2 = maxn;
		if (a[point].c)
		{
			 r2 = 1;
			a[point].g = ! a[point].g;
			r2+=tru(point);
			a[point].g = ! a[point].g;
		}
		a[point].v1 = min(r1,r2);
		if (a[point].v1 > maxn) a[point].v1 = maxn;
	}// 1;
	if (!(point ==1 && v == 1))
	{
		int r1 = fal(point);
		int r2 = maxn ;
		if (a[point].c)
		{
			r2= 1;
			a[point].g = ! a[point].g;
			r2+=fal(point);
			a[point].g = ! a[point].g;
		}
		a[point].v2 = min(r1,r2);
		if (a[point].v2 > maxn) a[point].v2 = maxn;
		
	}//0
	return 0;
}

int main ()
{
	freopen(inputfilename , "r" , stdin);
	freopen(outputfilename , "w" , stdout);

	int number ,times;
	cin >> number;
//	memset(a, 0 , sizeof(a));
	for (times = 0 ;times < number ; times ++)
	{
		cin >> n >> v;
		int i;
		for (i = 1 ; i <= (n-1)/2 ; i++)
		{
			cin>>a[i].g>>a[i].c;
//			a[i].leaf = 0;
			a[i].hash = 0;
		}
		int b = (n-1)/2+1;
		for (i = 0 ; i < (n+1)/2 ; i++)
		{
			int v;
			cin  >> v;
			if (v) { a[i+b].v1 = 0; a[i+b].v2 = maxn;}
			else {a[i+b].v1 = maxn ; a[i+b].v2 = 0;}
	//		a[i+b].leaf = 1;
			a[i+b].hash = 1;
		}
		search(1);
		cout <<"Case #"<<times+1<<": "; 
		if (v)
		{
			if (a[1].v1 >= maxn) cout << "IMPOSSIBLE"<<endl;
			else cout <<a[1].v1<<endl;
		}
		else
		{
			if (a[1].v2 >= maxn) cout <<"IMPOSSIBLE"<<endl;
			else cout <<a[1].v2<<endl;
		}
	}


	fclose(stdin);
	fclose(stdout);

	return 0;
}

 
