#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#pragma comment(linker, "/STACK:167772160")
typedef long long int64;
using namespace std;
int n,i,j,k,x[1001],num,o,t;
double uns;
bool z[1001];
int main()
{
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	cin>>t;
	for(o=0;o<t;o++)
	{
	uns=0;
	cin>>n;
	for(i=1;i<=n;i++)
		cin>>x[i];

	memset(z,false,sizeof(z));
	for(i=1;i<=n;i++)
		if(z[i]==false)
		{
			z[i]=true;
			num=1;
			k=x[i];
			while(k!=i){num++;z[k]=true;k=x[k];z[k]=true;}

			if(num-1)
			uns+=num;
		}
		printf("Case #%d: %.6f\n",o+1,uns);
	}

}