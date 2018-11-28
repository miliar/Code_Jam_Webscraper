#include<iostream>
#include<fstream>
#include<vector>
#include<string>
using namespace std;
int d[10];
int cmp[10];
int main()
{
	ofstream fout("A.out");
	int N;
	cin>>N;
	int i,j,k;
	int num,tmp;
	bool flag;
	for(i=0;i<N;++i)
	{
		cin>>num;
		for(j=0;j<10;++j)
		{
			d[j]=0;
			cmp[j]=0;
		}
		tmp=num;
		while(tmp>0)
		{
			d[tmp%10]++;
			tmp/=10;
		}
		bool found=false;
		for(j=num+1;j<=100000000;++j)
		{
			for(k=0;k<10;++k) cmp[k]=0;
			tmp=j;
			flag=true;
			while(tmp>0)
			{
				cmp[tmp%10]++;
				tmp/=10;
			}
			for(k=1;k<10;++k)
			{
				//if(num==9 && j==19)cout<<cmp[k]<<endl;
				if(cmp[k]!=d[k])
				{
				flag=0;
				break;
				}
			}
			if(flag)
			{
				fout<<"Case #"<<(i+1)<<": "<<j<<endl;
				found=true;
				break;
			}
		}
		if(!found)cout<<"Not Found: "<<i<<endl;
	}
	return 0;
}

	
