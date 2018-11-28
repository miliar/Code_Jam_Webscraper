#include <fstream>
#include <cstring>
#include <vector>

using namespace std;

int main()
{
	ifstream dat("input.txt");
	ofstream sol("output.txt");
	int n;
	char line[501]={0},str[]={"welcome to code jam"};
	dat >> n;
	dat.getline(line,500,'\n');
	for(int i=0;i<n;i++)
	{
		dat.getline(line,500,'\n');
		int ans[21]={0};
		ans[0]=1;
		int j,t;
		for(j=0;j<strlen(line);j++)
		{
			for(t=0;t<strlen(str);t++)
			{
				if (str[t]==line[j]) ans[t+1]=(ans[t+1]+ans[t])%10000;
			}
		}
		sol << "Case #" << i+1 << ": ";
		if (ans[19]<10) sol << "000";
		else
		{
			if (ans[19]<100) sol << "00";
			else
				if (ans[19]<1000) sol << "0";
		}
		sol << ans[19]%10000 << endl;
	}
	return 0;
}