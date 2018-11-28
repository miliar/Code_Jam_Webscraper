#include<iostream>
#include<fstream>
using namespace std;
struct TA
{
	int val,next;
};

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");
	int T,test;
	in >> T;
	for (test=0;test<T;test++)
	{
		int N,k,R;
		int g[1000];
		TA xdk[1000];
		in >> R >> k >> N;
		for (int i=0;i<N;i++)
			in >> g[i];
		for (int i=0;i<N;i++)
		{
			xdk[i].val=0;
			int cur=i;
			while (true)
			{
				if (xdk[i].val+g[cur]<=k)
					xdk[i].val+=g[cur];
				else
					break;
				cur++;
				if (cur==N)
					cur=0;
				if (cur==i)
					break;
			}
			xdk[i].next=cur;
		}
		int circle_sum=0,long_circle=0;
		bool was[1000];
		for (int i=0;i<N;i++)
			was[i]=false;
		int cur=0;
		while (true)
		{
			if (was[cur])
				break;
			was[cur]=true;
			//long_circle++;
			//circle_sum+=xdk[cur].val;
			cur=xdk[cur].next;
		}
		int res=0;
		int tmp=0;
		while (true)
		{
			if (tmp==cur)
				break;
			res+=xdk[tmp].val;
			R--;
			tmp=xdk[tmp].next;
		}
		while (true)
		{
			circle_sum+=xdk[tmp].val;
			long_circle++;
			tmp=xdk[tmp].next;
			if (tmp==cur)
				break;
		}

		res+=circle_sum*(int)(R/long_circle);
		R%=long_circle;
		while (true)
		{
			if (R==0)
				break;
			res+=xdk[cur].val;
			cur=xdk[cur].next;
			R--;
		}
		out << "Case #" << test+1 << ": " << res << endl;
	}
	return 0;
}