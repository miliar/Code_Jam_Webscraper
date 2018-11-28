#include <fstream>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;
ifstream in("input.txt");
ofstream out("output.txt");
long long int t,n,f,s;
vector <long long int> a;
vector <long long int> b;
int main()
{
	in >> t;
	for (int x=1;x<=t;x++)
	{
		in >> n;
		a.resize(n);
		for (int i=0;i<n;i++) in >> a[i];
		sort(a.begin(),a.end());
		b.assign(30,0);
		for (int i=0;i<n;i++) for (int j=0;j<30;j++) b[j]+=(a[i]>>j)%2;
		f=0;
		for (int j=0;j<30 && f==0;j++) f=b[j]%2;
		if (f==1) out << "Case #" << x << ": NO\n";
		else
		{
			s=0;
			for (int i=1;i<n;i++) s+=a[i];
			out << "Case #" << x << ": " << s << "\n";
		}
	}
	return 0;
}
