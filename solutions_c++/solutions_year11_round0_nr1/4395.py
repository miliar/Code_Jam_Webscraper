#include <iostream>
#include <fstream>
using namespace std;
#define makepos(x) (x>0?x:-(x))
int main()
{
	int cc=1,tc,no_points,cp=0,b_time=0,o_time=0,b_pos=1,o_pos=1, cur_pos, tot_time=0,res[20];
	char cur_color, temp_color;
ofstream myfile;
myfile.open ("outputl");
	for(cin>>tc;cc<=tc;cc++)
	{
		tot_time=0, b_time=0,o_time=0,b_pos=1,o_pos=1,cp=0;
		for(cin>>no_points;cp<no_points;cp++)
		{
			cin>>cur_color>>cur_pos;
			if(cp==0)
			temp_color=cur_color;
			if(cur_color==temp_color)
			{
				if(cur_color=='B')
				{
					tot_time+=makepos(cur_pos-b_pos)+1;
					b_time+=makepos(cur_pos-b_pos)+1;
					b_pos=cur_pos;
					o_time=0;
				}

				if(cur_color=='O')
				{
					tot_time+=makepos(cur_pos-o_pos)+1;
					o_time+=makepos(cur_pos-o_pos)+1;
					o_pos=cur_pos;
					b_time=0;
				}
			}
			else
			{
				if(cur_color=='B')
				{
					tot_time+=(o_time<makepos(cur_pos-b_pos))?(makepos(cur_pos-b_pos)-o_time)+1:1;
					b_time+=(o_time<makepos(cur_pos-b_pos))?(makepos(cur_pos-b_pos)-o_time)+1:1;
					b_pos=cur_pos;
					o_time=0;
				}

				if(cur_color=='O')
				{
					tot_time+=(b_time<makepos(cur_pos-o_pos))?(makepos(cur_pos-o_pos)-b_time)+1:1;
					o_time+=(b_time<makepos(cur_pos-o_pos))?(makepos(cur_pos-o_pos)-b_time)+1:1;
					o_pos=cur_pos;
					b_time=0;
				}	
			}
			temp_color=cur_color;
		}
myfile<<"Case #"<<cc<<": "<<tot_time<<endl;
	}
	return 0;
}
