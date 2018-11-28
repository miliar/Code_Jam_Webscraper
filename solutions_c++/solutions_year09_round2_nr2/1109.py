#include<iostream>
#include<cstring>
#include<string>
#include<algorithm>
#include<queue>
#include<stack>
#include<cmath>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	for(int k=1;k<=t;k++)
	{
		string str;
		cin>>str;
		string str1=str;;
		next_permutation(str1.begin(),str1.end());
		printf("Case #%d: ",k);
		if(str1>str)
			cout<<str1<<endl;
		else
		{
			str1+='0';
			sort(str1.begin(),str1.end());
			for(int i=0;i<str1.length();i++)
			{
				if(str1[i]!='0')
				{
					swap(str1[i],str1[0]);
					break;
				}
			}
			cout<<str1<<endl;
		}
	}
	return 0;
}
