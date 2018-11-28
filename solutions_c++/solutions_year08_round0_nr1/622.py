#include <stdio.h>
#include <map>
#include <string>
#include <iostream>
using namespace std;
map <string,int> hash;
map <string,int> sign;
string s[1001];
string q[10001];

int main(int argc, char *argv[])
{
	freopen("A-big.in","r",stdin);
	freopen("A-big.out","w",stdout);
	int n,sn,qn;
	cin>>n;
	int count;
	int ret;
	for (int i=0; i<n; i++)
	{
		ret = 0;
		count = 0;
		hash.clear();		
		sign.clear();
		cin>>sn;
		getchar();
		for (int j=0; j<sn; j++)
		{
			getline(cin,s[j]);
		//	cout<<s[j]<<endl;
			hash[s[j]] = 1;
		}
		
		cin>>qn;
		getchar();
		for (int j=0; j<qn; j++)
		{
			getline(cin,q[j]);
		//	cout<<q[j]<<endl;
			if (hash[q[j]] == 1)
			{
				if (sign[q[j]] == 0)
				{
				//	cout<<q[j]<<" create"<<endl;
					sign[q[j]] = 1;
					count++;
				}
			}
			if (count >= sn)
			{
				ret++;
				count = 0;
				sign.clear();
				sign[q[j]] = 1;
			//	cout<<q[j]<<" new"<<endl;
				count++;
			}
		}
		printf("Case #%d: %d\n", i+1, ret);
	}
//	printf("abc");
	fclose(stdin);
	fclose(stdout);
	return 0;
}
