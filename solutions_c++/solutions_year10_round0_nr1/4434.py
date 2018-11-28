#include "iostream"
#include "fstream"

using namespace std;

int main()
{
	int N=0;
	int K=0;
	int T=0;
	int chain[60];
	int flag=0;
	int time=1;

	ifstream in("A-small-attempt3.in");
	ofstream out("A-small-attempt3.out");

	in>>T;
	while(time<=T)
	{
		in>>N>>K;
		for(int i1=1;i1<60;i1++)
			chain[i1]=0;
		chain[0]=1;

		for(int i=0;i<K;i++)
		{
			for(int j=0;j<N;j++)
			{
				if(1==chain[2*j])
				{
					if(1==chain[2*j+1])
						chain[2*j+1]=0;
					else
						chain[2*j+1]=1;
				}
			}

			int j2;
			for(j2=0;j2<N;j2++)
			{
				if(0==chain[2*j2+1])
				{
					flag=j2;
					break;
				}
			}
			if(j2==N)
				flag=N;
			//cout<<flag<<" "<<i<<endl;

			for(int j3=0;j3<N;j3++)
			{
				if(j3<=flag)
				{
					chain[2*j3]=1;
				}
				else
				{
					chain[2*j3]=0;
				}
			}
		}

		int jj;
		for(jj=0;jj<N;jj++)
		{
			if(chain[2*jj]==0||chain[2*jj+1]==0)
				break;
		}
		if(jj==N)
		{
			out<<"Case #"<<time<<": ON"<<endl;
		}
		else
		{
			out<<"Case #"<<time<<": OFF"<<endl;
		}
		time++;
	}
	return 0;
}