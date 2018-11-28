#include <fstream>
#include <iostream>
using namespace std;

enum game_status_e
{
	status_x_won,
	status_o_won,
	status_draw,
	status_unfinished,
};

static char *ppsz_result[]=
{
	"X won",
	"O won",
	"Draw",
	"Game has not completed",
};

static int umpire_for_won(char *p_status,char target)
{
	bool b_result=false;
	int x_count=0;
	for(int i=0;i<4;i++)
	{
		b_result=true;
		x_count=0;
		for(int j=i*4;j<(i+1)*4;j++)
		{
			if(p_status[j]==target)
				x_count++;
			if(p_status[j]!=target&&p_status[j]!='T')
			{
				b_result=false;
				break;
			}
		}
		if(b_result&&x_count>=3)
		{
			break;
		}
	}
	if(b_result)
		return 1;
	for(int i=0;i<4;i++)
	{
		b_result=true;
		x_count=0;
		for(int j=i;j<i+13;j=j+4)
		{
			if(p_status[j]==target)
				x_count++;
			if(p_status[j]!=target&&p_status[j]!='T')
			{
				b_result=false;
				break;
			}
		}
		if(b_result&&x_count>=3)
		{
			break;
		}
	}
	if(b_result)
		return 1;
	x_count=0;
	b_result=true;
	for(int i=0;i<4;i++)
	{
		if(p_status[5*i]==target)
			x_count++;
		if(p_status[5*i]!=target&&p_status[5*i]!='T')
		{
			b_result=false;
			break;
		}
	}
	if(b_result)
		return 1;
	x_count=0;
	b_result=true;
	for(int i=0;i<4;i++)
	{
		if(p_status[3*i+3]==target)
			x_count++;
		if(p_status[3*i+3]!=target&&p_status[3*i+3]!='T')
		{
			b_result=false;
			break;
		}
	}
	if(b_result)
		return 1;
	else
		return 0;
}

static int umpire(char *p_status)
{
	if(umpire_for_won(p_status,'X'))
		return status_x_won;
	if(umpire_for_won(p_status,'O'))
		return status_o_won;
	int i_count=16;
	for(int i=0;i<16;i++)
	{
		if(p_status[i]=='.')
		{
			i_count--;
			break;
		}
	}
	if(i_count==16)
		return status_draw;
	else
		return status_unfinished;
}

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("result.out");

	int result=0;
	int test_count;
	char test[32];
	fin>>test_count;
	fin.getline(test,32);
	for(int i=0;i<test_count;i++)
	{
		fin.getline(test,32);
		fin.getline(test+4,32);
		fin.getline(test+8,32);
		fin.getline(test+12,32);
		int result=umpire(test);
		fout<<"Case #"<<i+1<<": "<<ppsz_result[result]<<endl;
		fin.getline(test,32);
	}
	fin.close();
	fout.close();
	return 0;
}
