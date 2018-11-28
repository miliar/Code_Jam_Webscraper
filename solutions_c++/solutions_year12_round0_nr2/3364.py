#include <fstream>

using namespace std;

void createscores(int a[]);
bool elevate(int a[],int p);
int main()
{
	int t,n,s,p,max;
	int scores[100][4];
	ifstream ifile("small.in");
	ofstream ofile("output");
	ifile.seekg(0,ios::beg);
	ofile.seekp(0,ios::beg);
	ifile>>t;
	 
	for(int i = 0; i < t ; i++)
	{
		ifile>>n;
		ifile>>s;
		ifile>>p;
		max = 0;
		for(int j = 0; j < n; j++)
		{
			ifile>>scores[j][0];
			createscores(scores[j]);
			if(s > 0)
			{
				bool b = elevate(scores[j],p);
				if(b)
					s--;
			}
		}
		for(int j = 0; j < n; j++)
			if(scores[j][1] >= p )
				max++;
		ofile<<"Case #"<<i+1<<": "<<max<<endl;

	}
	ifile.close();

	ofile.close();
}
void createscores(int a[])
{
	for(int i = 1; i < 4; i++)
		a[i] = a[0]/3;
	int mod = a[0]%3;	
	if(mod == 1)
		a[1]++;
	else if(mod == 2)
	{
		a[1]++;
		a[2]++;
	}
}
bool elevate(int a[],int p)
{
	if(a[1] != p-1)
		return false;
	int mod = a[0] % 3;
	if(mod == 0)
	{
		if(a[1] == 10 || a[3] == 0)
			return false;
		a[1]++;
		a[3]--;
		return true;
	}
	if(mod == 1)
	{
		return false;
	}	
	if(mod == 2)
	{
		if(a[1] == 10 || a[2] == 0)
			return false;
		a[1]++;
		a[2]--;
		return true;
	}
	return false;
}