#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <sstream>

using namespace std;

int main(void)
{
	int t;
	int arr[15];
	string str;
	int i,j;

	cin >> t;
	for (int cas=1; cas<=t; cas++)
	{
		cin >> str;
		for (i=0; i<str.length()-1; i++)
			arr[i]=0;

		bool DONE=false;
		int tot=0;
		long long int val,sgn;
		long long int sum;
		while (!DONE)
		{
			val=str[0]-'0';
			sgn=1;	// 1=+ , -1=-
			sum=0;
			for (i=0; i<str.length()-1; i++)
			{
				if (arr[i]==0)
				{
					val*=10;
					val+=str[i+1]-'0';
				}
				else if (arr[i]==1)
				{
					sum+=sgn*val;
					sgn=1;
					val=str[i+1]-'0';
				}
				else if (arr[i]==2)
				{
					sum+=sgn*val;
					sgn=-1;
					val=str[i+1]-'0';
				}
			}
			sum+=sgn*val;

			if (sum%2==0 || sum%3==0
				|| sum%5==0 || sum%7==0)
				tot++;

			// Incr
			j=str.length()-1;
			do
			{
				j--;
				if (j<0)
					break;

				arr[j]++;
				arr[j]%=3;
			}
			while (arr[j]==0);

			if (j<0)
				DONE=true;
		}
		cout << "Case #" << cas << ": ";
		cout << tot;
		cout << endl;
	}

	return 0;
}