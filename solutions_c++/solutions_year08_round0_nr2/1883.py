#include <fstream>

using namespace std;

int A[30][2];
int B[30][2];

int readTime(istream& in)
{
	int h,m;
	char colon;
	in>>h>>colon>>m;
	return h*60 + m;
}

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	
	int N;
	fin>>N;
	for(int c=0;c<N;c++)
	{
		int T,NA,NB;
		fin>>T>>NA>>NB;
		
		for(int i=0;i<NA;i++)
		{
			A[i][0]=readTime(fin);
			A[i][1]=readTime(fin);
		}
		for(int i=0;i<NB;i++)
		{
			B[i][0]=readTime(fin);
			B[i][1]=readTime(fin);
		}
		
		int ac = 0;
		int bc = 0;
		int a0 = 0;
		int b0 = 0;
		for(int t=0;t<24*60;t++)
		{
			for(int i=0;i<NB;i++)
			{
				if(B[i][1] + T == t)
					ac++;
			}
			for(int i=0;i<NA;i++)
			{
				if(A[i][1] + T == t)
					bc++;
			}
			
			for(int i=0;i<NA;i++)
			{
				if(A[i][0] == t)
				{
					if(ac==0)
						a0++;
					else
						ac--;
				}
			}
			for(int i=0;i<NB;i++)
			{
				if(B[i][0] == t)
				{
					if(bc==0)
						b0++;
					else
						bc--;
				}
			}
		}
		fout<<"Case #"<<(c+1)<<": "<<a0<<" "<<b0<<endl;
	}
	return 0;
}
