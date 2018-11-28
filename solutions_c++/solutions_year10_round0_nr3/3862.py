#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <numeric>
#include <fstream>
#include <string>

//those who was first shall become the last
void shift(std::deque<int>& obj, int n);

//sum peoples in "n" first groupes
int sum_first_n(std::deque<int> obj, int n);

//take all the info, return result
int so_how_much(int R, int k, std::deque<int> arr);

int main()
{
	int T,R,k,N; 
	std::deque<int> arr;

	std::ifstream in("D:\\C-small-attempt0.in");
	std::ofstream of("D:\\Output.txt");
	
	if(!in)
	{
		std::cout<<"Error reading input"<<std::endl;
		return 1;
	}

	if(!of)
	{
		std::cout<<"Error with output"<<std::endl;
		return 1;
	}

	in>>T;

	for(int i=0; i<T; i++)
	{
		arr.clear();
		in>>R>>k>>N;		   //read R,k,N
		for(int j=0; j<N; j++) //read info about groups and fill our deque with it
		{
			int n = 0;
			in>>n;
			arr.push_back(n);
		}
		
		of<<"Case #"<<i+1<<": "<<so_how_much(R,k,arr)<<std::endl;
	}

	in.close();
	of.close();

	std::cout<<"Done! Check out Outfile!";
	return 0;
}

void shift(std::deque<int>& obj, int n)
{
	for(int i=0; i<n; i++)
	{
		int n = obj.front();
		obj.pop_front();
		obj.push_back(n);
	}
}

int sum_first_n(std::deque<int> obj, int n)
{
	return std::accumulate(obj.begin(),obj.begin()+n,0);
}

int so_how_much(int R, int k, std::deque<int> arr)
{
	int N = arr.size();

	int temp1 = 0;
	int groups_n = 0;
	int sum_money = 0;

	for(int i=0; i<R; i++)
	{
		//find out how much groups can we take
		temp1=groups_n=0;
		for(int j=0; j<N; j++)
		{
			temp1+=arr[j];
			if(temp1<=k)
				groups_n++;
			else
				break;
		}

		//take them for a ride & place them in a queue
		sum_money += sum_first_n(arr,groups_n);
		shift(arr,groups_n);
	}
	return sum_money;
}