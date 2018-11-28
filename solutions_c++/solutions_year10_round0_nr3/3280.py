#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	ifstream fin ("c-small.in");
	ofstream fout ("c-small.out");
	int T;
	fin >> T;
	for (int tt=0;tt<T;tt++)
	{
		int k,R,N,Euro=0;
		fin >> R >> k >> N;
		int *groups=new int[N];
		for (int i=0;i<N;i++)
		{
			fin >> groups[i];
		}
		int x=0, ppl=0;
		for (int p=0;p<R;p++)
		{
			int startX=x;
			bool isRev=false;
			while (true)
			{

				if (x==N) 
				{
					x=0;
					isRev=true;
				}
				if (x==startX && isRev) break;
				int temp=groups[x];
				if (ppl+temp<=k) ppl+=temp;
				else
				{
					break;
				}
				x+=1;
			}
			Euro+=ppl;
			ppl=0;
		}
		fout << "Case #" << tt+1 << ": " << Euro <<endl;
	}

}