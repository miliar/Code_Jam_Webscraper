#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

string get_(int n)
{
	string res;
	int base = 10;
	while(n>0)
	{
		int k1 = n % base;
		n /= base;
		res.push_back('0'+k1);
	}
	while(res.size()<4)
		res.push_back('0');

	string res2;

	for(int i=3;i>=0;i--)
		res2.push_back(res[i]);

	return res2;
}

int main()
{
	int N;
	cin>>N;
	string target = "welcome to code jam";
	int t_size = target.size();
	string str;
	getline(cin,str);

	for(int i=1;i<=N;i++)
	{
		
		getline(cin,str);
		int s_size = str.size();
		int **t = new int*[t_size+1];
		for (int j=0;j<=t_size;j++)
		{
			*(t+j) = new int[s_size+1];
			memset(*(t+j),0,(s_size+1)*sizeof(int));
		}
		
		
		for(int j=s_size-1;j>=0;j--)
		{
			if(target[t_size-1] == str[j])
				t[t_size-1][j] = t[t_size-1][j+1]+1;
			else
				t[t_size-1][j] = t[t_size-1][j+1];
		}
	


		/*
		if(str[s_size-1] == target[t_size-1])
			t[t_size-1][s_size-1] = 1;
		*/
		/*
		for(int j=t_size-1;j>=0;j--)
		{
			if(str[s_size-1] == target[j])
				t[j][s_size-1] = t[j+1][s_size-1]+1;
			else
				t[j][s_size-1] = t[j+1][s_size-1];
		}
		*/
		
		
		for(int j=t_size-2;j>=0;j--)
		{
			for(int k=s_size-2;k>=0;k--)
			{
				for(int q=k;q<s_size;q++)
				{
					if(target[j]==str[q])
					{
						t[j][k] += t[j+1][q+1];
						t[j][k] %= 10000;
					}
						
				}
			}
		}
		

		cout<<"Case #"<<i<<": "<<get_(t[0][0])<<endl;

		for(int j=0;j<=t_size;j++)
			delete[] *(t+j);
		delete[] t;
	}

	//system("pause");
	return 1;
}