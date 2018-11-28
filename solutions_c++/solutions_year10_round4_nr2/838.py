#include <iostream>
#include <fstream>

using namespace std;

int prices[1050][1050];
int miss[1050];
int tb[1050];
int put2[11]={1,2,4,8,16,32,64,128,256,512,1024};
int used[1050];
long long price;

bool satisfied(int n)
{
	for(int i=0;i<put2[n];i++)
		if ((n-tb[i])>=miss[i])
			return false;
	return true;
}

bool este_smysl(int i, int j,int n)
{
	for(int k=j*put2[i+1];k<j*put2[i+1]+put2[i+1];k++)
		if (miss[k]<n-tb[k])
			return true;
	return false;
}

void buy(int i, int j)
{
	price++;
	for(int k=j*put2[i+1];k<j*put2[i+1]+put2[i+1];k++)
		tb[k]++;
}

int main()
{
	int t;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	fin >> t;
	for(int cases=0;cases<t;cases++)
	{
		int n;
		fin >> n;
		for(int i=0;i<put2[n];i++)
		{
			fin >> miss[i];
			tb[i]=0;
			used[i]=false;
		}
		for(int i=0;i<n;i++)
			for(int j=0;j<put2[n-i-1];j++)
				fin >> prices[i][j];
		price=0;
			for(int i=n-1;i>=0;i--)
				for(int j=0;j<put2[n-i-1];j++)
					if (este_smysl(i,j,n))
						buy(i,j);

		fout<< "Case #" <<  cases+1 <<": " << price << endl;
	}

}
