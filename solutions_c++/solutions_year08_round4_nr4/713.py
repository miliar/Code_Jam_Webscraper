#include <iostream>
#include <algorithm>
using namespace std;

char ss[1050],pp[1050];
int a[]={1,2,3,4,5};

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("12.out","w",stdout);
	int i,nca,k,len,x,y,lmin,f,ca;
	scanf("%d",&nca);
	for(ca=1;ca<=nca;ca++)
	{
		scanf("%d%s",&k,ss);
		len = strlen(ss);
		lmin = len;
		do 
		{
			for(i=0;i<len;i++)
			{
				x = i/k;
				y = i%k;
				pp[i] = ss[x*k+a[y]-1];
			}
			pp[len]='\0';
			f= 1;
			for(i=1; i<len; i++)
				if(pp[i] != pp[i-1])
					f++;
			if(f<lmin)	lmin = f;
		}while(next_permutation(a,a+k));

		printf("Case #%d: %d\n",ca,lmin);
	}
	return 0;
}