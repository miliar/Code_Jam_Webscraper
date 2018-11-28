#include <fstream>

using namespace std;
char s[80][80];
int N,cases;
int last[80];

int main()
{
	ifstream fin("large.in");
	ofstream fout("output.txt");
	fin >> cases;
	for(int cas=0;cas<cases;cas++)
	{
		fin >> N;
		char c[10];
		fin.getline(c,sizeof(c));
		for(int i=0;i<N;i++)
		{
			fin.getline(s[i],sizeof(s[i]));
		}
		int last[80]={0};
		for(int i=0;i<N;i++)
			for(int j=N-1;j>=0;j--)
			{
				if (s[i][j]=='1')
					{
						last[i]=j;
						break;
					}
			}
		int count=0;
		for(int i=0;i<N;i++)
		{
			if (last[i]>i)
			{
				int j=i+1;
				while (last[j]>i)
				{
					j++;
				}
				int temp=last[j];
				for(int k=j;k>i;k--)
					last[k]=last[k-1];
				last[i]=temp;
				count+=j-i;
			}
		}
		
		fout << "Case #" <<cas+1<<": " << count << "\n";
	}
	return 0;
}