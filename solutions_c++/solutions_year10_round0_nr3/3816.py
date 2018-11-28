#include<iostream>
using namespace std;

int main()
{
	freopen("C-small-attempt2.in","r",stdin);
    freopen("large.out","w",stdout);

	int allnum;
	cin>>allnum;//
	for(int allcount=0;allcount<allnum;allcount++)
	{
		long R,k,N;
		cin>>R;//
		cin>>k;
		cin>>N;
		long *p;
		p = new long[N];
		for(long a=0;a<N;a++)
		{
			cin>>p[a];
		}
		//如果组和小于等于木马数，直接输出组和乘以次数
		long sum = 0;
		for(long b1=0;b1<N;b1++)
		{
			sum+=p[b1];
		}
		if(sum<=k)
		{
			cout<<"Case #"<<allcount+1<<": "<<sum*R<<endl;
			delete []p;
			continue;
		}
		sum=0;
		long *towhich;
		towhich = new long[N];
		long *contentnum;
		contentnum = new long[N];
		for(long b=0;sum<=k;b++)
		{
			/*if(b==N)
				b=0;*/
			sum+=p[b];
		}
		b--;
		sum-=p[b];
		towhich[0]=b;//下一轮起始位置
		contentnum[0]=sum;//包含人数
		for(long c=1;c<N;c++)
		{
			sum-=p[c-1];//减上一位置人数
			for(long d=towhich[c-1];sum<=k;d++)//加上一位置末尾位置的人数
			{
				if(d==N)
					d=0;
				sum+=p[d];
			}
			d--;
			sum-=p[d];
			towhich[c]=d;
			contentnum[c]=sum;
		}
		long pos=0;
		long all=0;
		for(long e=0;e<R;e++)
		{
			all+=contentnum[pos];
			pos=towhich[pos];
		}
		cout<<"Case #"<<allcount+1<<": "<<all<<endl;
		delete []towhich;
		delete []contentnum;
	}
	return 0;
}