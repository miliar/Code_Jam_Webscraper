#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

void main()
{
	ifstream ifs("A-large.in");
	ofstream ofs("A-large.out");

	int t,r,c;
	int i,j,k;
	ifs>>t;
	for(i=0; i<t; i++)
	{
		vector<string> pic;
		string str;

		ifs>>r>>c;

		for(j=0; j<r; j++)
		{
			ifs>>str;
			pic.push_back(str);
		}

		for(j=0; j<r; j++)
		{
			for(k=0; k<c; k++)
			{
				if(pic[j][k]=='#')
				{
					if(j+1<r && k+1<c && pic[j+1][k]=='#' && pic[j][k+1]=='#' && pic[j+1][k+1]=='#')
					{
						pic[j+1][k+1]=pic[j][k]='/';
						pic[j+1][k]=pic[j][k+1]='\\';
					}
					else
						break;
				}
			}
			if(k<c)
				break;
		}
		ofs<<"Case #"<<i+1<<":"<<endl;
		if(j<r)
		{
			ofs<<"Impossible"<<endl;
		}
		else
		{
			for(j=0; j<r; j++)
				ofs<<pic[j]<<endl;
		}
	}
}