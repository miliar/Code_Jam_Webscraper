#include<iostream>
#include<string.h>
#include<fstream>
#define max_size 101
#define max_engine 101
#define max_query 1001
using namespace std;
ifstream fin("A-large.in");
ofstream fout("ans.txt");

int main()
{
	int cas;
	while(fin>>cas)
	{
		for(int output=1;output<=cas;output++)
		{
			fout<<"Case #"<<output<<": ";
			int s,q;
			//system("pause");
			fin>>s;
			char engine[s][max_size];
			//system("pause");
			fin.getline(engine[0],max_size);
			for(int i=0;i<s;i++)
				fin.getline(engine[i],max_size);
			fin>>q;
			char query[q][max_size];
			fin.getline(query[0],max_size);
			for(int i=0;i<q;i++)
				fin.getline(query[i],max_size);
			int ans[s][q];
			cout<<s<<" "<<q<<endl;
			for(int i=0;i<s;i++)
			{
				if(strcmp(query[0],engine[i]) == 0)
					ans[i][0]=2;
				else
					ans[i][0]=0;
				//cout<<i<<" "<<q<<endl;
				//system("pause");
			}
			for(int i=1;i<q;i++)
			{
				for(int j=0;j<s;j++)
				{
					int mini=999999999;
					if(strcmp(query[i],engine[j]) == 0)
					{
						for(int k=0;k<s;k++)
							if(k != j && ans[k][i-1] < mini)
								mini = ans[k][i-1];
						ans[j][i] = (ans[j][i-1]+2) > (mini+1) ? (mini+1) : (ans[j][i-1]+2);
					}
					else
					{
						for(int k=0;k<s;k++)
							if(k != j && ans[k][i-1]<mini)
								mini = ans[k][i-1];
						ans[j][i] = (ans[j][i-1]) > (mini+1) ? (mini+1) : (ans[j][i-1]);
					}
					//cout<<ans[j][i]<<" "; 
				}
				//cout<<endl;
			}
			/*for(int i=0;i<s;i++)
			{
				for(int j=0;j<q;j++)
					cout<<ans[i][j]<<" ";
				cout<<endl;
			}*/
			//system("pause");
			int mini=999999999;
			if(q == 0)
				mini = 0;
			for(int k=0;k<s;k++)
				if(ans[k][q-1]<mini)
					mini = ans[k][q-1];
			fout<<mini<<endl;
		}
	}
	return 0;
}

