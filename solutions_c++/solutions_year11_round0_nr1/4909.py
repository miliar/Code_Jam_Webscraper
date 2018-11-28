
// bot_trust.cc
// g++ -g -o bottrust bot_trust.cc

#include <string.h>
#include <iostream>
#include <string>
#include <vector>
#include <deque>

using namespace std;

typedef struct Task
{
  char robot;
  int pos;
	Task():robot(' '),pos(0){};
}Task;
typedef vector<Task> VecTask;
typedef vector<VecTask> VecCase;
typedef deque<int> QueTarget;
typedef vector<long> VecResult;

const int  kLineSize = 400; 

int GetInput(const string& input,VecCase& vec_case);
void RunTask(const VecTask& vec_task,long& result);
int Output(const string& output,const VecResult& vec_res);

int main(int argc,char** argv)
{
  if (argc < 3)
  {
    cout<<"syntax error!"<<endl;
    return -1;
  }
  string input = argv[1];
  string output = argv[2];

	VecCase vec_case;
	int n = GetInput(input,vec_case);
	if (n != 0)
	{
		cout<<"get input error!"<<endl;
		return -2;
	}
	long res = 0;

	VecResult vec_res;
	for (int i=0;i<vec_case.size();i++)
	{
		RunTask(vec_case[i],res);	
		vec_res.push_back(res);
	}

	if (0 == Output(output,vec_res))
		cout<<"ouput file ok!"<<endl;
	else
		cout<<"output file error!"<<endl;

  return 0;
}

int GetInput(const string& input,VecCase& vec_case)
{
	FILE* fp;
  if (NULL == (fp = fopen(input.c_str(),"r")))
  {
    cout<<"open input file error!"<<endl;
    return -1;
  }
	int total_cases = 0;
  char buf[kLineSize + 1] = {0};
	if (fgets(buf,kLineSize,fp))
		total_cases = atoi(buf);
  while (!feof(fp))
  {
    if (!fgets(buf,kLineSize,fp)) // fgets will read the '\n' together.
			break;	
		char* end = buf;
		if (end = strstr(end,"\n"))
			*end = '\0';
		//  4 O 2 B 1 B 2 O 4
		VecTask vec_task;
		char* p = buf;
		char* q = p;
		int total_task = 0;
		if (p = strstr(p," "))
		{
			*p++ = '\0';
			total_task = atoi(q);
			q = p;
		}
		while (p = strstr(p," "))
		{
			Task t;
			*p++ = '\0';
			// robot.
			t.robot = q[0];
			q = p;

			p = strstr(p," ");
			if (p != NULL)
				*p++ = '\0';
			// button pos.
			t.pos = atoi(q);
			q = p;
			vec_task.push_back(t);
			if (NULL == p)
				break;
		}
		vec_case.push_back(vec_task);
  }

  fclose(fp);
	return 0;
}

int Output(const string& output,const VecResult& vec_res)
{
	FILE* fp;
  if (NULL == (fp = fopen(output.c_str(),"w")))
  {
    cout<<"open output file error!"<<endl;
    return -1;
  }
	for (int i=0;i<vec_res.size();i++)
	{
		fprintf(fp,"Case #%d: %d\n",i+1,vec_res[i]);	
	}
  fclose(fp);
	return 0;
}

void RunTask(const VecTask& vec_task,long& result)
{
	// get OTarget BTarget
	QueTarget Otar,Btar;
	for (int i=0;i<vec_task.size();i++)
	{
		Task t = vec_task[i];
		if (t.robot == 'O')
			Otar.push_back(t.pos);
		else if (t.robot == 'B')
			Btar.push_back(t.pos);	
		else
			;
	}

	result = 0;
	int o_tar = Otar.front();
	int b_tar = Btar.front();
	int o_cur = 1;
	int b_cur = 1;
	for (int i=0;i<vec_task.size();i++)
	{
		Task t = vec_task[i];	
		if (t.robot == 'O')
		{
			if (o_cur < o_tar)
			{
				while (o_cur < o_tar)
				{
					o_cur++; // o move
					result++;
					// b move
					if (b_cur < b_tar) b_cur++; 
					if (b_cur > b_tar) b_cur--;
				}
			}
			else if (o_cur > o_tar)
			{
				while (o_cur > o_tar)
				{
					o_cur--; // o move
					result++;
					// b move
					if (b_cur < b_tar) b_cur++; 
					if (b_cur > b_tar) b_cur--;
				}
			}
			result++;	// o push
			Otar.pop_front();
			o_tar = Otar.front();
			// b move
			if (b_cur < b_tar) b_cur++; 
			if (b_cur > b_tar) b_cur--; 
		
		}
		else if (t.robot == 'B')
		{
			if (b_cur < b_tar)
			{
				while (b_cur < b_tar)
				{
					b_cur++;
					result++;
					// o move
					if (o_cur < o_tar) o_cur++; 
					if (o_cur > o_tar) o_cur--;
				}

			}
			else if (b_cur > b_tar)
			{
				while (b_cur > b_tar)
				{
					b_cur--;
					result++;
					// o move
					if (o_cur < o_tar) o_cur++; 
					if (o_cur > o_tar) o_cur--;
				}
			}
			result++; // b push			
			Btar.pop_front();
			b_tar = Btar.front();

			// o move
			if (o_cur < o_tar) o_cur++; 
			if (o_cur > o_tar) o_cur--;
		}
		else{};
	}	
}
