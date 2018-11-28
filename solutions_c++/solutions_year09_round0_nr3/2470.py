#include <string>
#include <iomanip>
#include <iostream>

using namespace std;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t, c_no, i, j;
	string line;
	scanf("%d%*c",&t);
	for(c_no=1;c_no<=t; c_no++)
	{
		getline(cin, line);
		int len=line.size();
		int here[20]={1};
		char welcome[20]="welcome to code jam";
		for(i=0;i<len;i++)
		{
			for(j=18;j>=0;j--)
			{
				if(line[i]==welcome[j]) here[j+1]=(here[j+1]+here[j])%1000;
			}
		}
		cout<<"Case #"<<c_no<<": "<<setfill('0')<<setw(4)<<here[19]<<endl;
	}
	return 0;
}
