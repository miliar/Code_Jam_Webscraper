#include<stdio.h>
#include<iostream>
using namespace std;
__int64 candy[1001];
int main()
{
	int T,N;
	//ofstream fout("C:/GoogleCJ/C-small.out.txt");
	FILE *f;
	cin>>T;
	f=fopen("C:/GoogleCJ/C-small.out.txt","w");
	for(int i=0;i<T;i++)
	{
		cin>>N;
		for(int j=0;j<N;j++)
			scanf("%I64d",&candy[j]);
		int good=candy[0];
		for(j=1;j<N;j++)
		{
			good=good^candy[j];
		}
		if(good!=0)
		{
			//fout<<"Case #"<<i+1<<": "<<"NO"<<"\n";
			fprintf(f,"Case #%d: NO\n",i+1);
			cout<<"Case #"<<i+1<<": "<<"NO"<<"\n";
			continue;
		}
		__int64 sum=0,min=1000001;
		for(j=0;j<N;j++)
		{
			sum+=candy[j];
			if(min>candy[j])
			{
				min=candy[j];
			}
		}
		sum-=min;
		//fout<<"Case #"<<i+1<<": "<<sum<<"\n";  
		fprintf(f,"Case #%d: %I64d\n",i+1,sum);
		cout<<"Case #"<<i+1<<": ";
		printf("%I64d\n",sum);

	}
	fclose(f);
	return 0;
}