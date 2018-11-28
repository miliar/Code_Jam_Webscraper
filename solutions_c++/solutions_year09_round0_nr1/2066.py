

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main()
{
	int l,d,n;
	ifstream inf("A-large.in.txt");
	ofstream outf("out.txt");

	vector<string> vsw;
	inf>>l>>d>>n;
	for(int i=0;i<d;i++)
	{
		string str;
		inf>>str;
		vsw.push_back(str);
	}
	//n<=500
	for(int i=0;i<n;i++)
	{
		vector<string> vsp(l);
		string str;
		inf>>str;
		int flag=0;
		for(int j=0,t=0;j<int(str.length());j++)
		{
			if(str[j]=='(')
			{			
				flag=1;
				continue;
			}
			if(str[j]==')')
			{			
				t++;
				flag=0;
				continue;
			}
			vsp[t]+=str[j];
			if(!flag)
				t++;
		}
		int K=0;
		//d<=5000
		for(int j=0;j<d;j++)	//Æ¥ÅäµÚj¸ö
		{
			bool pipei=true;
			//l<=15
			for(int k=0;k<l;k++)
			{
				if(vsp[k].find_first_of(vsw[j][k])==string::npos)
				{
					pipei=false;
					break;
				}
			}
			if(pipei)
				K++;
		}
		outf<<"Case #"<<i+1<<": "<<K<<endl;
	}
	return 0;
}

