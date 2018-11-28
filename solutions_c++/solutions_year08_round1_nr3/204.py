#include <cstdio>
#include <iostream>
using namespace std;
char *ans[] = {"XXX","XXX","027","143","751","935","607","903","991","335","047","943","471","055","447","463","991","095","607","263","151","855","527","743","351","135","407","903","791","135","647"};
int main()
{
	int tn,n,casen=1;
	scanf("%d",&tn);
	while (tn--)
	{
		scanf("%d",&n);
		printf("Case #%d: %s\n",casen++,ans[n]);
	}
	return 0 ;
}
