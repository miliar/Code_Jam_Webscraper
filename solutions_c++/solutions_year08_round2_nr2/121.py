#include<iostream>
#include<vector>
using namespace std;
bool a[1023];
void init()
{
	a[1]=a[0]=1;
	for(int i=2;i<1000;i++)
	{
		if(!a[i])
		for(int j=i*i;j<1000;j+=i)
		{
			a[j]=1;
		}
	}
}
int f[10000];
inline int fin(int k)
{
	if(k==f[k]) return k;
	return f[k]=fin(f[k]);
}
vector<int>v;
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small.out","w",stdout);
	int cas,test=1,A,B,n,i,j,k,sum;
	scanf("%d",&cas);
	init();
	while(cas--)
	{
		cin>>A>>B>>n;
		if(A>B) swap(A,B);
		for(j=A;j<=B;j++)
		{
			f[j]=j;
		}
		for(i=n;i<=B;i++)
		{
			if(!a[i])
			{

			   for(j=A;j<=B;j++)
				{
					if(j%i==0)
					{
						v.push_back(j);
					}
				}
			}
			for(j=1;j<v.size();j++)
			{
				f[fin(v[j])]=fin(v[0]);
			}
			v.clear();
		}
		sum=0;
			for(j=A;j<=B;j++)
			{
				if(fin(j)==j) sum++; 
			}
		printf("Case #%d: %d\n",test++,sum);
	}
	return 0;
}