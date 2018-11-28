#include <stdio.h>
#include <deque>

using namespace std;

int main(int argc, char **argv)
{
	if(argc!=2)
	{
		printf("Usage: <prog> <input_file>\n");
		return 1;
	}

	FILE *fin = fopen("a.in","r");
	FILE *fout = fopen("a.out","w");
	
	unsigned long long r,k;
	int n,cnt;
	fscanf(fin,"%d",&cnt);
	for(int i=0;i<cnt;i++)
	{
		fscanf(fin,"%lld %lld %d",&r,&k,&n);
		deque<unsigned long long> q;
		for(int j=0;j<n;j++)
		{
			unsigned long long c;
			fscanf(fin,"%lld",&c);
			q.push_back(c);
		}		

		unsigned long long sum=0;
		for(int j=0;j<r;j++)
		{
			deque<unsigned long long> tq,lq;
			unsigned long long left=k;
			bool more=true;
			for(deque<unsigned long long>::iterator it=q.begin();
				it!=q.end() && left>=0;it++)
			{
				unsigned long long cur = *it;
				if(cur<=left && more)
				{
					left-=cur;
					sum+=cur;					
					tq.push_back(cur);
				}
				else
				{
					more=false;
					lq.push_back(cur);
				}
			}
			q.clear();

			for(deque<unsigned long long>::iterator it=lq.begin();
				it!=lq.end();it++)
				q.push_back(*it);

			for(deque<unsigned long long>::iterator it=tq.begin();
				it!=tq.end();it++)
				q.push_back(*it);
		}
		fprintf(fout,"Case #%d: %lld\n",i+1,sum);
	}
	fclose(fin);
	fclose(fout);
}
