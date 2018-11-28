#include <fstream>
using namespace std;
ifstream in("input.txt");
ofstream out("output.txt");
int t;
long long int n;
int pd,pg;
long long int d;
int a[]={1,2,4,5,10,20,25,50,100};
int main()
{
	in >> t;
	for (int x=1;x<=t;x++)
	{
		in >> n >> pd >> pg;
		d=100;
		for (int i=0;i<9;i++) if (pd%a[i]==0) d=100/a[i];
		if (d<=n && (pg!=0 || pg==0 && pd==0) && (pg!=100 || pg==100 && pd==100)) out << "Case #" << x << ": Possible" << "\n";
		else out << "Case #" << x << ": Broken" << "\n";
	}
	return 0;
}
