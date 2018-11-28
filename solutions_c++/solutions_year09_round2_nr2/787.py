#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int N;
	scanf("%d",&N);
	int cnt = 0;
	while( N-- )
	{
		vector<int> num;
		string number;
		cin>>number;
		for(int i=0;i<number.length();i++)
			num.push_back(number[i]-'0');
		bool f = true;
		for(int i=0;f && i+1<num.size();i++)
			if(num[i]<num[i+1]) f = false;
		if(f)
		{
			int nz = 1;
			vector<int> temp;
			for(int i=0;i<num.size();i++)
				if(num[i]==0) nz++; else temp.push_back(num[i]);
			sort(temp.begin(),temp.end());
			for(int i=0;i<nz;i++)
				temp.insert(temp.begin()+1,0);
			num = temp;
		}
		else
			next_permutation(num.begin(),num.end());
		printf("Case #%d: ", ++cnt);
		for(int i=0;i<num.size();i++)
			cout<<num[i];
		cout<<endl;


	}
	return 0;
}
