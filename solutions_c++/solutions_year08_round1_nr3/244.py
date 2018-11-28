#include<iostream>
using namespace std;
string a[]={"0","005","027","143","751","935","607","903","991","335","047","943","471",
"055","447","463","991","095","607","263","151","855","527","743","351","135","407","903",
"791","135","647"};
int main()
{
	int t,n;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for(int i=1;i<=t;++i)
	{
		scanf("%d",&n);
		cout << "Case #"<<i<<": " << a[n] << endl;
	}
}
