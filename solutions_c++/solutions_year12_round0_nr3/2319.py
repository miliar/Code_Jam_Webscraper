#include <iostream>
#include <fstream>
#include <string>
using namespace std;

#define Dmax 2000000
#define Tmax 50
#define DDmax 7


int digit(int num)
{
	int di=0;
	while (num>0)
	{
		num=num/10;
		di++;
	}
	return di;
}

int main()
{
	char * filenamein="C-large.in";
	char * filenameout="C-large.out";
	ifstream fin(filenamein);
	ofstream fout(filenameout);

	int T;
	int range[Tmax][2];
	bool *flag=new bool[Dmax];
	int dd[3][DDmax];

	fin >> T;
	for (int i=0; i<T; i++)
	{
		fin >> range[i][0];
		fin >> range[i][1];
	}
	fin.close();

	for (int i=0; i<T; i++)
	{
		int total=0;
		for (int j=range[i][0]; j<=range[i][1]; j++)
		{
			flag[j]=0;
		}
		int num=range[i][0];
		int dr=digit(num);
		int di=dr;
		while (num>0)
		{
			di--;
			dd[0][di]=num%10;
			num=num/10;
		}

		num=range[i][1];
		di=dr;
		while (num>0)
		{
			di--;
			dd[1][di]=num%10;
			num=num/10;
		}	

		for (int j=range[i][0]; j<=range[i][1]; j++)
		{
			if (!flag[j])
			{
				flag[j]=1;
				num=j;
				di=dr;
				while (num>0)
				{
					di--;
					dd[2][di]=num%10;
					num=num/10;
				}

				int circlenum=1;
				for (int k=1; k<dr; k++)
				{
					if (dd[2][k]!=0)
					{
						bool flag1=1;
						for (int l=0; l<dr; l++)
						{
							if (dd[2][(k+l)%dr]>dd[0][l])
								break;
							else if (dd[2][(k+l)%dr]<dd[0][l])
							{
								flag1=0;
								break;
							}
						}
						if (!flag1)
						continue;
						bool flag2=1;
						for (int l=0; l<dr; l++)
						{
							if (dd[2][(k+l)%dr]<dd[1][l])
								break;
							else if (dd[2][(k+l)%dr]>dd[1][l])
							{
								flag2=0;
								break;
							}
						}
						if (!flag2)
						continue;
						int newval=0;
						for ( int l=0; l<dr; l++)
						{
							newval=newval*10+dd[2][(k+l)%dr];
						}
						if (!flag[newval])
						{
							circlenum++;
							flag[newval]=1;
						}
					}
				}
				total+=circlenum*(circlenum-1)/2;
			}
		}
		fout << "Case #" << i+1 << ": ";
		fout << total <<endl;
	}
	fout.close();
	delete flag;
	return 0;
}