#include <iostream>
#include <cstdio>
#include <string>
#include <cmath>
#include <algorithm>
#include <set>
#include <vector>
#include <map>

#define mn(a,b) ((a<b) ? (a) : (b))        		
#define mx(a,b) ((a<b) ? (b) : (a))			
#define ab(a) ((a<0) ? (-(a)) : (a))			
#define fr(a,b) for(int a=0; a<b; ++a)			
#define fe(a,b,c) for(int a=b; a<c; ++a)		
#define fw(a,b,c) for(int a=b; a<=c; ++a)		
#define df(a,b,c) for(int a=b; a>=c; --a)		
#define BIG 1000000000	
#define MAX_STRING 100000
#define PB push_back
#define MP make_pair

using namespace std;

int m[2000],p,t,two;
char buf[10000];
bool mas[2000];

int main()
{
freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);
scanf("%d\n", &t);
fw(test,1,t)
	{
	scanf("%d\n", &p);
	two = 1;
	fr(i,p)
		two*=2;
	fr(i,two)
		scanf("%d", &m[i]);
	scanf("\n");
	fr(i,p)
		gets(buf);
	memset(mas,0,sizeof(mas));
	fr(i,two)
		{
		int pos = two-1+i;
		pos = (pos-1)/2;
		fr(j,m[i])
			{
//			cout<<"Loop pos: "<<pos<<endl;
			pos = (pos-1)/2;
			}
//		cout<<"Pre-pos: "<<pos<<endl;
		fr(j,p-m[i])
			{
			mas[pos] = true;
			if(pos==0) break;
			pos = (pos-1)/2;
			}
		}	
	int res = 0;
	fr(i,two-1)
		if(mas[i]) res++;
	printf("Case #%d: %d\n", test,res);		
	}
return 0;
}
