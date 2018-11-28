#include <iostream>
#include <fstream>
#include <vector>
#include <bitset>
using namespace std;

int main()
{
	
	ifstream in("C-large.in");
	ofstream out("C-large.out");

	vector<long> candy;
	int case_cnt;
	in>>case_cnt;
	if(case_cnt < 1 || case_cnt > 100)
	{
		cout<<"wrong case count"<<endl;
		return 1;
	}

	int candy_cnt;
	long sum1=0,sum2=0;
	long sum=0;
	int case_no=1;
	while(case_cnt --)
	{
		in>> candy_cnt;
		if(candy_cnt <2 || candy_cnt > 1000)
		{
			cout<<"wront candy count"<<endl;
			return 1;
		}
		int temp;
		candy.clear();
		while(candy_cnt --)
		{
			in>>temp;
			candy.push_back(temp);	
		}
		long add1,add2;
		sum1 = 0;
		sum=0;
		bool change = false;
		add1 = candy[0];
		sum = candy[0];
		int min = candy[0];
		for(size_t i=1;i< candy.size();i++)
		{
			sum += candy[i];
			add1 ^= candy[i];
			if(candy[i] < min)
				min = candy[i];

		}
		if(add1 ==0)
			change = true;
		
		//for(size_t i=0;i< candy.size()-1;i++)
		//{
		//	sum1 += candy[i];
		//	if(i)
		//		add1 =add1 ^ candy[i];
		//	else
		//		add1 = candy[0];
		//	sum2 = 0;
		//	for(size_t j=i+1;j< candy.size();j++)
		//	{
		//		sum2 += candy[j];
		//		if(j== i+1)
		//			add2 = candy[i+1];
		//		else
		//			add2 =add2 ^ candy[j];
		//	}
		//	if(add1 == add2)
		//		if(sum1 <= sum2 && sum2 > sum)
		//			sum = sum2;
		//		else if(sum1 > sum2 && sum1 > sum )
		//			sum = sum1;


		//}
		out<<"Case "<<"#"<<case_no<<": ";
		if(change)
			out<<sum - min<<endl;
		else
			out<<"NO"<<endl;
		case_no ++;
		

	}


	return 0;
	
}