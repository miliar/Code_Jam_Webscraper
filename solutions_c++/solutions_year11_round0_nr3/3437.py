#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int nTest;
	cin>>nTest;
	for(int test = 1; test<=nTest; test++)
	{
		int nInput;
		cin>>nInput;
		vector<int> input;
		int sum(0);
		int xsum(0);
		for(int i=0;i<nInput;i++)
		{
			int tmp;
			cin>>tmp;
			input.push_back(tmp);
			sum += tmp;
			xsum ^= tmp;
		}
		sort(input.begin(),input.end());

		bool result(false);
		for(int i=0; i<nInput && !result ;i++)
		{
			if(input[i] == (xsum^input[i]))
			{
				sum -= input[i];
				result = true;
			}
		}
		if(result)
			cout<<"Case #"<<test<<": "<<sum<<endl;
		else
			cout<<"Case #"<<test<<": "<<"NO"<<endl;
	}
	return 0;
}