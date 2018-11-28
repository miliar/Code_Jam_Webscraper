#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;

struct command 
{
	int position;
	char robot;
};

int main ()
{
	ifstream in ("A-large.in");
	ofstream out ("output.txt");
	int T,n,minimumTime,B_current,O_current;
	command *ptr;
	in>> T;
	for (int i=1;i<=T;i++)
	{
		B_current=1;
		O_current=1;
		minimumTime=0;
		in>>n;
		ptr=new command [n];
		for (int k=0;k<n;k++)
			in>>ptr[k].robot>>ptr[k].position;
		for (int k=0;k<n;k++)
		{
			if (ptr[k].robot=='B')
			{
				while (B_current<ptr[k].position)
				{
					minimumTime++;
					B_current++;
					for (int j=k+1;j<n;j++)
					{
						if (ptr[j].robot=='O')
						{
							if (O_current<ptr[j].position)
							{
								O_current++;
							}
							if (O_current>ptr[j].position)
							{
								O_current--;
							}
							break;
						}
					}
				}
				while (B_current>ptr[k].position)
				{
					minimumTime++;
					B_current--;
					for (int j=k+1;j<n;j++)
					{
						if (ptr[j].robot=='O')
						{
							if (O_current<ptr[j].position)
							{
								O_current++;
							}
							if (O_current>ptr[j].position)
							{
								O_current--;
							}
							break;
						}
					}
				}
				if (ptr[k].position==B_current)
				{
					minimumTime++;
					for (int j=k+1;j<n;j++)
					{
						if (ptr[j].robot=='O')
						{
							if (O_current<ptr[j].position)
							{
								O_current++;
							}
							if (O_current>ptr[j].position)
							{
								O_current--;
							}
							break;
						}
					}
				}
			}
			else 
			{
				while (O_current<ptr[k].position)
				{
					minimumTime++;
					O_current++;
					for (int j=k+1;j<n;j++)
					{
						if (ptr[j].robot=='B')
						{
							if (B_current<ptr[j].position)
							{
								B_current++;
							}
							if (B_current>ptr[j].position)
							{
								B_current--;
							}
							break;
						}
						
					}
				}
				while (O_current>ptr[k].position)
				{
					minimumTime++;
					O_current--;
					for (int j=k+1;j<n;j++)
					{
						if (ptr[j].robot=='B')
						{
							if (B_current<ptr[j].position)
							{
								B_current++;
							}
							if (B_current>ptr[j].position)
							{
								B_current--;
							}
								break;
						}
					
					}
				}
				if (ptr[k].position==O_current)
				{
					minimumTime++;
					for (int j=k+1;j<n;j++)
					{
						if (ptr[j].robot=='B')
						{
							if (B_current<ptr[j].position)
							{
								B_current++;
							}
							if (B_current>ptr[j].position)
							{
								B_current--;
							}
							break;
						}	
					}
				}
			}
		}
		out<<"Case #"<<i<<": "<<minimumTime<<endl;
	}
	return 0;
}