#include <cstdio>
#include <map>
#include <algorithm>

using namespace std;

int ncases, t, a1, a2, b1, b2;
map < pair<int,int>, bool > win;

bool iswin(int a, int b)
{
	if(b>a)
	{
		int temp=a;
		a=b;
		b=temp;
	}
	
	map<pair<int,int>, bool>::iterator f=win.find(pair<int,int>(a,b));
	if(f!=win.end())
		return (*f).second;
	
	if(a==b || a<=0 || b<=0)
	{
		win[pair<int,int>(a,b)]=false;
		return false;
	}
	if(a%b==0)
	{
		win[pair<int,int>(a,b)]=true;
		return true;
	}
	
	//subtract kB from A
	for(int k=1; k*b<=a; k++)
		if(!iswin(a-k*b, b))
		{
			win[pair<int,int>(a,b)]=true;
			return true;
		}
	
	win[pair<int,int>(a,b)]=false;
	return false;
}

int main()
{
	scanf("%d", &ncases);
	for(t=0; t<ncases; t++)
	{
		scanf("%d %d %d %d", &a1, &a2, &b1, &b2);
		int sum=0;
		for(int i=a1; i<=a2; i++)
			for(int j=b1; j<=b2; j++)
				if(iswin(i,j))
					sum++;
		printf("Case #%d: %d\n", t+1, sum);
	}
}
