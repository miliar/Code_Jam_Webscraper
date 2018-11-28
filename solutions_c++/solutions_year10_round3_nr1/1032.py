#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <iostream>
using namespace std;

int le[1001];
int ri[1001];



int	main()
{
	if(!freopen("../../../../Downloads/A-large.in","r",stdin))puts("can't opne"),exit(1);
	//freopen("A_.out","w",stdout);
	int	T , n = 0;
	cin>>T;
	while (T--)
	{
		int r=0;
		int ch=0;
		int N;
		cin>>N;
		for(int i=0;i<N;i++)
		{
			cin>>le[i];
			cin>>ri[i];
		}
		for(int i=0;i<N;i++)
			for(int j=i+1;j<N;j++)
				if((le[j]>le[i]&&ri[j]<ri[i])||(le[j]<le[i]&&ri[j]>ri[i]))
					r++;


		
			printf("Case #%d: %d\n" , ++n,r);
		//cerr<<"case: #"<<n-1<<':'<<r<<endl;
	}


}
