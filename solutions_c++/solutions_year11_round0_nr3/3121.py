#include <string.h>
#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;
#define MaxCandy 1024
#define SliptChar " "

//int showbit(int tmp)
//{
//	int length = sizeof(tmp)*8;
//	unsigned int mymask = 0x80000000;
//	bool has_val = false;
//	int res = 0;
//	int count = 0;
//	for (int i = length ; i>0 ;i--)
//	{
//		if((tmp & mymask) != 0 || has_val == true)
//		{
//			int tmp_ = (tmp & mymask) ==0? 0:1;
//			res += tmp_  * pow(10.0,i-1);
//			has_val =true;
//		}
//		mymask=mymask>>1;
//	}
//	return res;
//}

int main(int argc,char *argv[])
{
	char case_str[MaxCandy]={0};	
	int total_test_case = 0;
	char* input_file = "..\\request.txt";
	fstream fs (input_file,ios::in);
	fstream fso ("..\\output.txt",ios::out);
	if (!fs)
	{
		cout<<"读取文件错误！"<<endl;
		return 0;
	}
	fs.getline(case_str,MaxCandy);
	total_test_case = atoi(case_str);
	//循环处理每个Test case
	char* p ;
	for(int i = 1 ; i<= total_test_case ;i++)
	{
		int one_case_total_num = 0;
		int total_sum = 0;
		int total_sum_D = 0;
		int tmp_num = 0 ;
		int min_num = 0 ;
		fs.getline(case_str,MaxCandy);
		one_case_total_num = atoi(case_str);
		fs.getline(case_str,MaxCandy);
		p = strtok(case_str,SliptChar);
		while(p != NULL)
		{
			tmp_num = atoi(p);
			if(min_num == 0)
			{
				min_num = tmp_num;
			}
			else
			{
				if(tmp_num< min_num)
				{
					min_num = tmp_num;
				}
			}
			total_sum_D += tmp_num;
			total_sum = total_sum ^ tmp_num ; 
			p = strtok(NULL,SliptChar);
		}
		if(total_sum == 0)
		{
			cout<<"Case #"<<i<<": "<<total_sum_D - min_num<<endl;
			fso<<"Case #"<<i<<": "<<total_sum_D - min_num<<endl;
		}
		else
		{
			cout<<"Case #"<<i<<": "<<"NO"<<endl;
			fso<<"Case #"<<i<<": "<<"NO"<<endl;
		}

	}
	int a;
	cin>>a;
	fs.close();
	fso.close();
	return 0;
}