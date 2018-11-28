#include<iostream.h>
#include<fstream.h>
int main()
{
	ifstream ifile("B-small.txt");
	ofstream ofile("fiout.txt");
	int te, n, sur, p, t[100],count=0;
	ifile>>te;
	for(int j=0;j<te;j++)
	{
		count=0;
		ifile>>n>>sur>>p;
		for(int i=0; i<n; i++)
		{
			ifile>>t[i];
			if((t[i]==0)&&(p==0))
			{	count++;
			}
			if(t[i]==0)
				continue;
			if((t[i]/3)>=p)
				count++;
			else
			{
				if((t[i]/3)==(p-1))
				{
					if((t[i]%3)!=0)
						count++;

					else
					{	if(sur!=0)
						{
							count++;
							sur--;
						}

					}
				}

				if(((t[i]/3)==(p-2))&&((t[i]%3)==2))
				{

					if(sur!=0)
					{
						count++;
						sur--;
					}

				}
			}
		}
		ofile<<" Case #"<<j+1<<": "<<count<<"\n";
	}

	ifile.close();
	ofile.close();
	return 0;
}
