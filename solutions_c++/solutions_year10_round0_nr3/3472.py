#include<iostream>
#include<cmath>
#include<fstream>
using namespace std;

int main()
{
	ifstream in("C-small-attempt1.in");
	ofstream out("out.txt");
	int T;
	long int R,k,N;
	long int g[10];
	long int gh[10][2];
	in>>T;
	//cin>>T;
	T++;
	for(int i=1;i<T;i++)
	{
		in>>R>>k>>N;
	//	cin>>R>>k>>N;
		for(int j=0;j<N;j++)
		{
			in>>g[j];
			//cin>>g[j];
		}
		memset(gh,0,20*sizeof(long int));
		for(int m=0;m<N;m++)
		{
			for(int y=m;;)
			{
				int v = gh[m][0]+g[y];
				if(v<=k)
					gh[m][0] = v;
				else break;
				y=(y+1)%N;
				if(y==m)
					break;
			}
			gh[m][1]=y;
		}
		long int ex=0;
		for(int r0=0,x=0;r0<R;r0++)
		{
			ex+=gh[x][0];
			x=gh[x][1];
		}
		out<<"Case #"<<i<<": "<<ex<<endl;
	}

	
}