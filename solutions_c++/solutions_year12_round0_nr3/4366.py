#include<iostream>
#include<fstream>
#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<algorithm>
#include<functional>
using namespace std;

int shift(int n,int L)
{
	char arr_temp[10];
	char arr[10];
	itoa(n,arr_temp,10);
	int length = strlen(arr_temp);
	int dif = 0;
	if((dif = L-length)!=0)
	{
		for(int i=0;i<dif;i++)
		{
			arr[i]='0';
		}
		arr[dif] = '\0';
		strcat(arr,arr_temp);
	}
	else
	{
		strcpy(arr,arr_temp);
	}

	if(length == 1)
		return n;
	else
	{
		char t = arr[L-1];
		for(int i=L-2;i>=0;i--)
		{
			arr[i+1] = arr[i];
		}
		arr[0] = t;
		return atoi(arr);
	}
}

int countPair(int n)
{
	if(n==1)
		return 0;
	else if(n<1)
		return -1;
	else
	{
		return n*(n-1)/2;
	}
}

int main()
{/*
	ifstream in("C-small-attempt1.in");
	cin.rdbuf(in.rdbuf());
	ofstream out("a.out");
	cout.rdbuf(out.rdbuf());
	*/
	
	int T,A,B;
	cin>>T;
	
	for(int n=0;n<T;n++)
	{
		cin>>A>>B;
		char a[10];
		itoa(A,a,10);
		int L = strlen(a);

		vector<int> record;
		vector<int>::iterator pos;

		int total = 0;

		for(int i=A;i<=B;i++)
		{
			//cout<<"consider "<<i<<": "<<endl;
			if((pos = find(record.begin(),record.end(),i))!=record.end())
				continue;

			int r[10];
			int cur = i;
			int result = 1;
			for(int j=0;j<L-1;j++)
			{
				r[j] = shift(cur,L);
				if(r[j]!=i&&r[j]>=A&&r[j]<=B)
				{
					if((pos = find(record.begin(),record.end(),r[j]))==record.end())
					{
						record.push_back(r[j]);
						result++;
						//cout<<i<<"   "<<r[j]<<endl;
					}
				}

				cur = r[j];
			}
			total+=countPair(result);
		}

		cout<<"Case #"<<n+1<<": "<<total<<endl;
	}

		

//	system("pause");
	return 0;
}