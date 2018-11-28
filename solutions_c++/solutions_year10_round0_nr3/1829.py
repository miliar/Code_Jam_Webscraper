// pr1.cpp : Defines the entry point for the console application.
//

#include <iostream>
using namespace std;
struct P{
 __int64	val, sum, kol;
};
int main()
{

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	__int64 r, k, n, s, shag, vsego=0;
	int i, t,j;
	P mas[1005];
	cin>>t;
	for (j =1; j <= t; j++)
	{
		vsego=0;
		cin>>r>>k>>n;
		for (i = 0; i <n; i++)
			cin>>mas[i].val;
		for (i = 0; i <n; i++)
		{
			int o = i;
			s = mas[i].val;
			shag = (i+1)%n;
			while(s+mas[shag].val<=k)
			{
				if (o == shag) break;
				s+=mas[shag].val;
				shag = (shag+1)%n;
			}
			
			mas[i].sum = s;
			mas[i].kol = shag;
		}
		shag = 0;
		for (i = 0; i < r; i++)
		{
			vsego+=mas[shag].sum;
			shag = mas[shag].kol;
		}
		cout<<"Case #"<<j<<": "<<vsego<<endl;
	}
	return 0;
}

