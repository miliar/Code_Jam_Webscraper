//#include <iostream>
#include <stdio.h>
//#include <math.h>
//#include <iomanip>
//#include <utility>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;


int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int n, p, k, l, times(0), i, frec, dep;
	__int64 types;
	vector<int> fre;
	//cin>>n;
	scanf("%d",&n);
	while(times++ < n)
	{
		types = 0;
		fre.clear();
		//cin>>p>>k>>l;
		scanf("%d%d%d",&p,&k,&l);
		if(p*k<l)
		{
			//cout<<"Case #"<<times<<": Impossible\n";
			printf("Case #%d: Impossible\n",times);
		}
		for(i=0;i<l;i++)
		{
			//cin>>frec;
			scanf("%d",&frec);
			fre.push_back(frec);
		}
		sort(fre.begin(),fre.end(),greater<int>());
		dep=0;
		for(i=0; i<l; i++)
		{
			if(i%k==0)
			{
				dep++;
			}
			types+= fre[i]*dep;
		}
		//cout<<"Case #"<<times<<": "<<types<<endl;
		printf("Case #%d: %I64u\n",times,types);
	}
	
	return 0;
}