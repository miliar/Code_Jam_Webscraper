#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <fstream>
using namespace std;

int n;
vector<vector<int>> data;
vector<vector<int>> nums;
vector<int> a;

void get_data(ifstream &inp);
int solv(int i);

int main()
{	
	string st;
	ifstream indata;
	cout << "Name of the file with the data: " << endl;
	cin >> st;
	indata.open(st.c_str());
	if (!indata.is_open())
	{
	cout << "Wrong file!" << endl;
	return 1;
	}
	get_data(indata);
	cout << "Name the file with the output: " << endl;
	cin >> st;
	ofstream out(st.c_str());
	if(!out) {
	cout << "Cannot open file.\n";
	return 1;
	}
	for (int i=0; i<n ;i++)
	{
		a.clear();
		solv(i);
		out << "Case #" << i+1 << ": ";
	//	cout << "Case #" << i+1 << ": ";
		for(int j=0; j<a.size(); j++)
		{
			out << a[j];
	//		cout << a[j];
		}
		out << endl;
	//	cout << endl;
	}
	return 0;
}

int solv(int i)
{
	int bo=0;
	for(int j=0; j<nums[i].size()-1; j++)
	{
		if(bo==0)
		if(nums[i][j]>nums[i][j+1])
		{
			int g;
			for(int y=nums[i].size()-1; y>j+1; y--)
			{
				//cout << " first " << nums[i][y] << endl;
				data[i][nums[i][y]]--;
				a.push_back(nums[i][y]);
			}
			for(int y=0; y<10; y++)
			{
				if (bo!=1)
				if (data[i][y]>0)
					if(y>nums[i][j+1])
					{
						//cout << "data[i][y]: " << data[i][y] << endl;
						bo=1;
						g=y;
						cout << " i " << i << " g " << g << endl;
						//cout << " G " << g << " num "<<nums[i][j] <<" num2 "<<nums[i][j+1]<< endl;
					}
			}
			if (bo!=1)
				bo=2;
			if (bo==1){
			//for(int y=nums[i].size()-1; y>j+1; y--)
			//{
			//	//cout << " first " << nums[i][y] << endl;
			//	data[i][nums[i][y]]--;
			//	a.push_back(nums[i][y]);
			//}
			a.push_back(g);
			data[i][g]--;
			for(int y=0; y<10; y++)
			{
				while(data[i][y]>0){
				data[i][y]--;
				a.push_back(y);
				//cout << " last " << y << endl;
				}
			}
			}
		}
	}
	//new 0
	if(bo!=1)
	{
		a.clear();
		for(int u=1; u<10; u++)
		{
			if(a.size()==0)
			if (data[i][u]!=0)
			{
				a.push_back(u);
				data[i][u]--;
				a.push_back(0);
			}
		}
		for(int u=0; u<10; u++)
		{
			while (data[i][u]!=0)
			{
				a.push_back(u);
				data[i][u]--;
			}
		}
	}
	return 0;
}

void get_data(ifstream &inp)
{
	int a,b;
	vector<int> dum;
	inp >> n;
	for (int i=0; i< n; i++)
	{
		data.push_back(dum);
		nums.push_back(dum);
		for(int j=0; j<10; j++)
			data[i].push_back(0);
		inp >> a;
		cout << " n : " << i << "  A " << a << endl;
		while(a!=0)
		{
			b=a%10;
			a=a/10;
			//cout << " b  " << b << endl;
			nums[i].push_back(b);
			data[i][b]++;
			//cout << " data  " << b << " " << data[i][b] << endl;
		}
	}
}
