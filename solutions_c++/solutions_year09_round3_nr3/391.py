#include <iostream>
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
#define SMALL -1000000000

using namespace std;

bool mas[10002];
int n,p,q,a,qs[100],temp[100];

int main()
{
freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);
scanf("%d", &n);
fr(i,n)
	{

	scanf("%d%d", &p, &q);

	fr(j,q)
		{
		scanf("%d", &qs[j]);
		temp[j] = qs[j];
		}
	int minim = BIG;
	while(true)
	{
	memset(mas,0,sizeof(mas));
	mas[0] = mas[p+1] = true;
	int sum = 0;
	fr(j,q)
		{
		a = temp[j];
//		cout<<"Next: "<<a<<endl;
		mas[a] = true;
		int r = a+1;
//		cout<<"To the right: ";		
		while(!mas[r])
			{
//			cout<<r<<" ";
			r++;
			sum++;
			}
//		cout<<endl;
//		cout<<"To the left: ";
		int l = a-1;
		while(!mas[l])
			{
//			cout<<l<<" ";
			l--;
			sum++;
			}	
//		cout<<endl;
//		cout<<"Current sum: "<<sum<<endl;	
		}	
	next_permutation(temp,temp+q);
	bool p = true;
	minim = mn(minim,sum);
	fr(j,q)
		if(temp[j]!=qs[j])
			{
			p = false;
			break;			
			}
	if(p) break;
	}
	printf("Case #%d: %d\n", i+1, minim);
	}
return 0;
}
