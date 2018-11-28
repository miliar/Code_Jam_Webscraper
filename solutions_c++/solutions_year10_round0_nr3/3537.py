#include<fstream.h>
#include<conio.h>
void main()
{
	int T=0,R=0,num=0,count=0,k=0,N=0,arr[10] = {0},g[10] = {0};
	long int cost = 0;
	char ch;
	ifstream fin;
	fin.open("input.txt");
	ofstream fout;
	fout.open("output.txt");
	fin>>T;
	for(int i=1;i<=T;i++)
	{
		cost = 0;
		count = 0;
		fin.get(ch);
		fin>>R;
		fin.get(ch);
		fin>>k;
		fin.get(ch);
		fin>>N;
		for(int j=0;j<N;j++)
		{
			fin.get(ch);
			fin>>g[j];
		}
		for(j=1;j<=R;j++)
		{
			if(count)
			{
				for(int r=count;r<N;r++)
					g[r-count] = g[r];
				for(r=0;r<count;r++)
					g[N-count+r] = arr[r];
			}
			for(int x=0;x<10;x++)
				arr[x] = 0;
			num = k;
			count = 0;
			for(int m=0;m<N;m++)
			{
				if(num-g[m]<0)
					break;
				else
				{
					num = num - g[m];
					arr[m] = g[m];
					cost = cost + g[m];
					count = m+1;
				}
			}
		}
		fout<<"Case #"<<i<<": "<<cost<<"\n";
	}
	getch();
}