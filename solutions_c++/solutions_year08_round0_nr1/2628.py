#include <iostream>
#include <fstream>
using namespace std;


int main()
{
	ifstream fin("D:\\tests\\1\\in.txt");
	ofstream fout("D:\\tests\\1\\out.txt");
	int tc = 0;
	
	fin>>tc;
	for(int i=0;i<tc;++i)
	{
		int s, q;
		char a[102][102] = {""};
		int b[1002] = {0};
		int r[102][1002] = {0};
		int tot[1002] = {0};
		fin>>s;
		fin.get();
		cout<<s;		
		for(int j=0;j<s;++j)
		{
			fin.getline(a[j], 102);
			printf("%s\n", a[j]);
		}
		(fin>>q).get();
		char curr[102];
		cout<<q;
		for(int j=0;j<q;++j)
		{
			fin.getline(curr, 102);
			printf("%s\n", curr);
			for(int d=0;d<s;++d)
				if(strcmp(curr, a[d])==0)
				{
					b[j]=d+1;					
					break;
				}
		}
		for( int j=0;j<q;++j)
			cout<<"b["<<j<<"]="<<b[j]<<", ";
		cout<<"\n";
		
		int num = 0;
		if( s>0 && q>0 )
		{
			for(int k=0;k<s;++k)
			{
				cout<<k+1<<": ";
				for(int j=q-1;j>=0;--j)
				{
					if(b[j]==k+1)
						r[k][j]=0;
					else
						if( j==q-1 ) r[k][j]=1;
						else r[k][j] = r[k][j+1]+1;
					cout<<r[k][j]<<" ";
				}
				cout<<"\n";
			}
			for(int j=0;j<q;)
			{
				int max = -1;
				for(int k=0;k<s;k++)
					if( r[k][j]>max ) max = r[k][j];
				if( max==-1 )
					j++;
				else
					j+=max;
				if( j<q )
					num++;
			}
		}
		fout<<"Case #"<<i+1<<": "<<num<<"\n";

	}

	fin.close();
	fout.close();

	return 0;
}