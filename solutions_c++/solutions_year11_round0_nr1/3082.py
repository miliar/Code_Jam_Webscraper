#include <string.h>
#include <iostream>
#include <fstream>

using namespace std;

#define MaxBtnNum  100
#define StartBtnNum 1
#define MaxLineChar  1000
#define MaxMission 1000
#define SliptChar " "

int main(int argc,char *argv[])
{
	char* input_file = "..\\request.txt";
	char case_str[MaxLineChar]={0};
	int line_num = 0;
	int test_count = 0;
	int total_test_case = 0;
	fstream fs (input_file,ios::in);
	fstream fso ("..\\output.txt",ios::out);
	if (!fs)
	{
		cout<<"读取文件错误！"<<endl;
	}
	else
	{
		while(fs.getline(case_str,MaxLineChar))
		{
			if(line_num == 0)
			{
				total_test_case = atoi(case_str);
				line_num++;
				continue;
			}
			test_count++;
			char* p = NULL ;
			int total_step = 0;
			int admit_O = 0;
			int admit_B = 0;
			int cur_pos_O = 1;
			int cur_pos_B = 1;
			int tmp_need_step = 0;
			char pre_step = ' ';
			int total_max = 0;
			int cur_step = 0;
			p = strtok(case_str , " ");
			
			while ( p != NULL)
			{
				p = strtok(NULL , " ");
				if(p ==NULL)
				{
					break;
				}
				if((*p) == 'O')
				{
					p = strtok(NULL , " ");
					tmp_need_step = abs(atoi(p) - cur_pos_O) ;//求出需要多少步到达
					cur_pos_O = atoi(p) ;
					if(pre_step != ' ')
					{
						if(pre_step=='O')
						{
							total_step += tmp_need_step +1;
							admit_O += tmp_need_step +1;
						}
						else
						{
							int tmp_addtion = 0;
							if(tmp_need_step > admit_B)
							{
								tmp_addtion = tmp_need_step -admit_B;
							}
							else
							{
								tmp_addtion = 0;
							}
							total_step += tmp_addtion +1;
							admit_O = tmp_addtion +1;
						}
						admit_B = 0;
					}
					else
					{
						admit_O = tmp_need_step +1;
						total_step = tmp_need_step +1;
					}
					pre_step ='O';
				}
				else
					//这是B
				{
					p = strtok(NULL , " ");
					tmp_need_step = abs(atoi(p) - cur_pos_B);
					cur_pos_B = atoi(p) ;
					if(pre_step != ' ')
					{
						if(pre_step=='B') // 这是同一个运行的时候，直接相加
						{
							total_step += tmp_need_step +1;
							admit_B += tmp_need_step +1;
							admit_O = 0;
						}
						else
						{
							//不是的话，需要和以前积累的
							int tmp_addtion = 0;
							if(tmp_need_step > admit_O)
							{
								tmp_addtion = tmp_need_step -admit_O;
							}
							else
							{
								tmp_addtion = 0;
							}
							admit_O = 0;
							total_step += tmp_addtion +1;
							admit_B = tmp_addtion +1;
						}
					}
					else
					{
						admit_B = tmp_need_step +1;
						total_step = tmp_need_step +1;
					}
					pre_step ='B';
				}
				cur_step ++;
			}
			fso<< "Case #"<<test_count<<": "<<total_step<<endl;
			cout<< "Case #"<<test_count<<": "<<total_step<<endl;
		}
	}
	int a;
	cin>>a;
	fs.close();
	fso.close();
	return 0;
}