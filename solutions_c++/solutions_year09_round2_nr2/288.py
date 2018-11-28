#include <algorithm>
#include <iostream>

using namespace std;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t, c_in;
	cin>>t;
	for(c_in=1;c_in<=t;c_in++)
	{
		char num[50];
		cin>>num;
		int start=0;
		int end=strlen(num);
		if(!next_permutation(num+start, num+end))
		{
			num[end]='0';
			end++;
			sort(num+start, num+end);
			while(num[start]=='0') start++;
			num[0]=num[start];
			num[start]='0';
		}
		num[end]=0;
		cout<<"Case #"<<c_in<<": "<<num<<endl;
	}
	return 0;
}
