#include<iostream>
#include<vector>
#include<string>
#include<fstream>
using namespace std;
int main()
{
	int L,D,N;
	ifstream in("d:/study/gcj/A-large.in");
	ofstream out("d:/study/gcj/A-large.out");
	in>>L>>D>>N;
	vector<string> dic(D);
    for(int i1=0;i1<D;i1++)
		in>>dic[i1];
	vector<string> sea(N);
	for(int i2=0;i2<N;i2++)
		in>>sea[i2];
	for(int i3=0;i3<N;i3++)
	{
		vector<string> group(L);
		for(int t1=0;t1<L;t1++) group[t1]="";
		int p=0;
		for(int j=0;j<sea[i3].length();j++)
		{
			if(sea[i3][j]=='(')
			{
				while(sea[i3][++j]!=')') group[p]+=sea[i3][j];
				p++;
			}else
				group[p++]+=sea[i3][j];
		}

			vector<int> flags(D);
			for(int t2=0;t2<D;t2++) flags[t2]=1;

			for(int m=0;m<L;m++)
			{
				
					for(int q=0;q<D;q++)
					{
						if(flags[q]==1)
						{
							if(group[m].find(dic[q][m])==string::npos) 
								flags[q]=0;
						}
					}
				
			}
			int ret=0;
			for(int t3=0;t3<D;t3++) if(flags[t3]==1) ret++;
			out<<"Case #"<<i3+1<<": "<<ret<<endl;

		

	}
	return 0;

}
