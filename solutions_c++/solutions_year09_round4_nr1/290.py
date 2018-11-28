#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<string>
#include<map>
#include<set>
#include<functional>
#include<utility>
using namespace std;

const int Max = 40;
char mat[Max][Max+1];
int minposs[Max],data[Max];
int n;
int main()
{
	int cases;
	cin>>cases;
	for(int _=1;_<=cases;_++)
	{
		cin>>n;
		for(int i=0;i<n;i++)
		{
			cin>>mat[i];
			int j;
			for(j=n-1;j>=0;j--)
				if(mat[i][j] == '1') break;
			minposs[i] = j;
		}
		int result = 0;
		for(int i=0;i<n;i++)
		{
			int j;
			for(j=i;j<n;j++)
				if(minposs[j] <= i) break;
			for(;j>i;j--)
			{
				swap(minposs[j],minposs[j-1]);
				result++;
			}
		}
		cout<<"Cases #"<<_<<": "<<result<<endl;
	}
	return 0;
}
