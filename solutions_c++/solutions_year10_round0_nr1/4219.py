#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

class item
{
public:
	bool power;
	bool flag;
	
	item()
	{
		power = false;
		flag = false;
	}
};

int input()
{
	int T = 0;
	int N = 0;
	int K = 0;
	vector<item> vit;

	ifstream fin("A-small-attempt3.in");
	ofstream fout("A-small-practice.out");
	
	if(fin==NULL || fout==NULL)
	{
		cout<<"Open file fails!"<<endl;
		exit(1);
	}
	int i = 0, j = 0;
	int num = 0;
	bool tem = false;

	int count = 0;
	vit.resize(1000);

	fin>>T;
	while(fin>>N)
	{
		fin>>K;

		vit.resize(N+2);
		vit[1].power = true;
		vit[1].flag = false;
		for(j=2; j<N+2; j++)
		{
			vit[j].power = false;
			vit[j].flag = false;
		}
		i++;

		count = 0;
		for(j=0; j<K; j++)
		{
			num = 1;
			tem = true;
			while(num<N+1 && tem)
			{
				vit[num].flag = !vit[num].flag;
				tem = vit[num+1].power;
				vit[num+1].power = vit[num].power && vit[num].flag;
				num++;
			}
			num = 1;
			while(vit[num].power)
			{
				vit[num+1].power = vit[num].flag;
				num++;
			}
		}
		
		cout<<"Case #"<<i<<": ";
		fout<<"Case #"<<i<<": ";
		if(vit[N+1].power)
		{
			cout<<"ON"<<endl;
			fout<<"ON"<<endl;
		}
		else
		{
			cout<<"OFF"<<endl;
			fout<<"OFF"<<endl;
		}
	}

	return 0;
}

int main()
{
	input();
	return 0;
}