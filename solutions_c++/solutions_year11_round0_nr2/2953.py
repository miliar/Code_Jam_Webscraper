#include <string.h>
#include <iostream>
#include <fstream>

using namespace std;

#define BaseEleNum 8
#define MaxLineChar  1024
#define SliptChar " "
#define MaxInvChar 100

int convert(char tmp_char)
{
	switch (tmp_char)
	{
		case 'Q':
			return 0;
		case 'W':
			return 1;
		case 'E':
			return 2;
		case 'R':
			return 3;
		case 'A':
			return 4;
		case 'S' :
			return 5;
		case 'D' :
			return 6;
		case 'F' :
			return 7;
	}
	return -1;
}

int main(int argc,char *argv[])
{
	char* input_file = "..\\request.txt";
	int line_num = 0;		//行数量
	int total_test_case = 0;
	int cur_test_case = 0;
	char case_str[MaxLineChar]={0};	
	fstream fs (input_file,ios::in);
	fstream fso ("..\\output.txt",ios::out);
	if (!fs)
	{
		cout<<"读取文件错误！"<<endl;
		return 0;
	}
	while(fs.getline(case_str,MaxLineChar))
	{
		
		int com_count = 0;		//相合条件数量
		int van_count = 0;		//相消条件数量
		int tmp_1 = 0;			//临时变量
		int tmp_2 = 0;			//临时变量
		int tmp_ = 0;
		char tmp_3 = 0;
		int one_result_end =0;	//运行结果的末尾
		char combine_arr[BaseEleNum][BaseEleNum] = {0};
		int combine_num[BaseEleNum] = {0};
		bool vanish_arr[BaseEleNum][BaseEleNum] = {false};
		int vanish_num[BaseEleNum] = {0};
		char one_result_arr[MaxInvChar] ={0};
		int one_req_length = 0; //一个测试用例的req字符串长度
		char* p;


		if(line_num == 0)
		{
			total_test_case = atoi(case_str);
			line_num++;
			continue;
		}
		cur_test_case ++;
		p = strtok(case_str , SliptChar);
		//首先转化混合条件的矩阵
		com_count = atoi(p);
		for (int i = 0 ; i < com_count ; i ++)
		{
			p = strtok(NULL,SliptChar);
			tmp_1 = convert(p[0]);
			tmp_2 = convert(p[1]);
			combine_arr[tmp_1][tmp_2] = p[2];
			combine_arr[tmp_2][tmp_1] = p[2];
			combine_num[tmp_1] ++; 
			combine_num[tmp_2] ++; 

		}
		p = strtok(NULL , SliptChar);
		//然后转化相消条件矩阵
		van_count = atoi(p);
		for (int i = 0 ; i < van_count ; i ++)
		{
			p = strtok(NULL,SliptChar);
			tmp_1 = convert(p[0]);
			tmp_2 = convert(p[1]);
			vanish_arr[tmp_1][tmp_2] = true;
			vanish_arr[tmp_2][tmp_1] = true;
			vanish_num[tmp_1] ++;
			vanish_num[tmp_2] ++;
		}
		//获取需要处理的字符串
		p = strtok(NULL , SliptChar);
		one_req_length = atoi(p);
		p = strtok(NULL , SliptChar);
		//逐个处理
		for(int j=0 ; j<one_req_length ; j++)
		{
			//首先处理混合
			tmp_ =convert(p[j]);
			if( combine_num[tmp_] >0 && one_result_end > 0 )
			{
				tmp_3 = convert(one_result_arr[one_result_end-1]);
				if(tmp_3 != -1 && combine_arr[tmp_][tmp_3] != 0)
				{
					one_result_arr[one_result_end] = 0;
					one_result_arr[one_result_end -1] = combine_arr[tmp_][tmp_3];
				}
				else
				{
					one_result_arr[one_result_end] = p[j];
					one_result_end ++;
				}
			}
			else
			{
				one_result_arr[one_result_end] = p[j];
				one_result_end ++;
			}
			//然后处理相消
			tmp_ = convert(one_result_arr[one_result_end -1]);
			if ( vanish_num[tmp_] > 0 && one_result_end > 1)
			{
				for(int m = 0 ; m<one_result_end ; m++)
				{
					tmp_3 = convert(one_result_arr[m]);
					if(tmp_3 !=-1 && vanish_arr[tmp_][tmp_3] ==true )
					{
						one_result_end = 0;
						break;
					}
				}
			}
		}
		fso<<"Case #"<<cur_test_case<<": [";
		cout<<"Case #"<<cur_test_case<<": [";
		for(int n = 0 ; n < one_result_end ; n++)
		{
			fso<<one_result_arr[n];
			cout<<one_result_arr[n];
			if(n != (one_result_end -1))
			{
				fso<<", ";
				cout<<", ";
			}
		}
		fso<<"]"<<endl;
		cout<<"]"<<endl;

	}
	int a;
	cin>>a;
	return 0;
}