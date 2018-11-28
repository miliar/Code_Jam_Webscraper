#include <iostream>
#include <vector>
#include <string>
using namespace std;

int pass_test(vector<int>& arr, vector<int>& mat)
{
	for(int i=0;i<arr.size();i++)
	{
		if(arr[i]<=mat[i]) continue;

		for(int j=i+1;j<mat.size();j++)
		{
			if(arr[i]<=mat[j])
			{
				arr.erase(arr.begin()+i);
				mat.erase(mat.begin()+j);
				return j-i;
			}
		}
	}
	return 0;
}


int main()
{
	int v;
	cin>>v;
	for(int c=1;c<=v;c++)
	{

		int n;
		cin>>n;
		vector<int> arr;
		vector<int> mat;
		for(int i=0;i<n;i++)
		{
			string s;
			cin>>s;
			int last1=n;
			while(last1--)
			{
				if(s[last1]=='1') break;
			}
			last1++;
			arr.push_back(last1);
			mat.push_back(i+1);
		}
		int sum=0;
		while(true)
		{
			int cur = pass_test(arr,mat);
			if(cur==0) break;
			sum+=cur;
		}
		cout<<"Case #"<<c<<": "<<sum<<endl;
	}
}