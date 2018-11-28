#include<iostream>
#include<cstdio>
#include<vector>
using namespace std;

FILE *fp,*fp2;

void Init()
{
	fp = fopen("B-large.in","r");
	fp2 = fopen("B-large.out","w");
}

void Close()
{
	fclose(fp);
	fclose(fp2);
}

int data[109];

int main(void)
{
	Init();

	int i,T,cases;

	fscanf(fp,"%d",&cases);

	int n,s,p;

	for(T=1;T<=cases;T++)
	{
		int count = 0;
		vector<int> v1,v2,v3,v4;
		fscanf(fp,"%d %d %d",&n,&s,&p);
		for(i=1;i<=n;i++)
		{
			fscanf(fp,"%d",&data[i]);
		}
		if(p >= 2)
		{
			for(i=1;i<=n;i++)
			{
				if(data[i] > 3*(p-1))
					v1.push_back(data[i]);
				else if(data[i] == 3*(p-1) || data[i] == 3*(p-1)-1)
					v2.push_back(data[i]);
				else if(data[i] >= 2)
					v3.push_back(data[i]);
				else
					v4.push_back(data[i]);
			}
			if(s>=v2.size())
				count = v1.size() + v2.size();
			else
				count = v1.size() + s;
		}
		else
		{
			for(i=1;i<=n;i++)
			{
				if(data[i] >= p)
					count++;
			}
		}
		fprintf(fp2,"Case #%d: %d\n",T,count);
	}
	Close();

	return 0;
}