#include <fstream>

using namespace std;

int a[1001];
int b[1001];
int n;
int REZ;

int main()
{
	ifstream f("A-large.in");
	ofstream f2("output.out");

	int T;
	f>>T;
	for(int TEST=0;TEST<T;TEST++)
	{
		REZ=0;
		f>>n;
		for(int i=0;i<n;i++)
			f>>a[i]>>b[i];

		for(int i=0;i<n;i++)
		{
			for(int y=0;y<n;y++)
			{
				if(a[i]<a[y] && b[i]>b[y])
				{
					REZ++;
				}
			}
		}
		f2<<"Case #"<<TEST+1<<": "<<REZ<<endl;
	}

	f.close();
	f2.close();
	return 0;
}
