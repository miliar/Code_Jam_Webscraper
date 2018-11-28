#include <fstream>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

struct rect{
	int x1,y1,x2,y2;
};

bool compare(rect a, rect b)
{
	return (a.x1<b.x1);
}

int a[102][102]={0};

bool iss()
{
	int b[102][102]={0};
	bool ans=false;
	for(int i=1;i<=100;i++)
		for(int j=1;j<=100;j++)
		{
			if ((a[i-1][j]==1)&&(a[i][j-1]==1))
			{
				b[i][j]=1;
				ans=true;
			}
			if ((a[i][j]==1)&&((a[i-1][j]==1)||(a[i][j-1]==1)))
			{
				b[i][j]=1;
				ans=true;
			}
		}
	for(int i=1;i<=100;i++)
	{
		for(int j=1;j<=100;j++)
		{
			//cout << a[i][j];
			a[i][j]=b[i][j];
		}
		//cout << endl;
	}
	//system("pause");
	return ans;
}

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int t;
	fin >> t;
	for(int cases=1;cases<=t;cases++)
	{
		int r;
		fin >> r;
		vector <rect> bact;
		for(int i=0;i<r;i++)
		{
			rect temp;
			fin >> temp.x1 >>temp.y1 >> temp.x2 >> temp.y2 ;
			for(int l1=temp.x1;l1<=temp.x2;l1++)
				for(int l2=temp.y1;l2<=temp.y2;l2++)
					a[l1][l2]=1;
			bact.push_back(temp);
		}
		/*sort(bact.begin(),bact.end();compare);
		for(int i=0;i<bact.size();i++)
		{

		}*/
		int sec=0;
		while (iss())
			sec++;
		fout << "Case #" << cases <<": " << ++sec << endl;
	}
}