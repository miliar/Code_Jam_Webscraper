#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(){
	int n;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	fin>>n;
	for(int i=0; i<n; i++){
		int s,q;
		int flag[100],num,result = 0;
		memset(flag,0,sizeof(flag));
		fin>>s;
		string ENGINE[100];
		char buffer[100];
		fin.getline(buffer,200);
		for(int j=0;j<s;j++)
		{
			fin.getline(buffer,200);
			ENGINE[j]=buffer;
		}
		fin>>q;
		fin.getline(buffer,200);
		string QUERY[1000];
		num = s;
		for(int j=0;j<q;j++)
		{
			fin.getline(buffer,200);
			QUERY[j]=buffer;
			for(int k=0;k<s;k++)
				if(QUERY[j] == ENGINE[k])
				{
					if (flag[k] == 0)
					{
						flag[k]=1;
						num--;
						if (num == 0)
						{
							memset(flag, 0, sizeof(flag));
							flag[k] = 1;
							num = s - 1;
							result ++;
						}
					}
				}

			
		}
		
		cout<<"Case #"<<i+1<<": "<<result<<"\n";//answer;
		fout<<"Case #"<<i+1<<": "<<result<<"\n";//answer;

	}
	fin.close();
	fout.close();
}