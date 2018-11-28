#include <iostream>
#include <cstdio>

using namespace std;

int main(void)
{
	int temp, test_cases,blocks,button_press,t=0,time_count, time_count_prev, prev_bot_number, next_bot_number, bot1_position, bot2_position, x=0, y=0,count=0;
	scanf("%d",&test_cases);
	cin.ignore();
	bool check;
	char common[6] = {'C','a','s','e',' ','#'};
	char inp[50500],prev_bot = '\0', next_bot;
	blocks = fread(inp, 1, 50500, stdin);
	for(unsigned int i=0; i<blocks; i++)
	{
		time_count = 0;
		time_count_prev = 0;
		check = true;
		if(inp[i] == 32)
		{
			++count;
			x=0;
			y=0;
			bot1_position=1;
			bot2_position=1;
			button_press = t;	//N is number
			t=0;
			++i;
			while(check)
			{
				next_bot = inp[i];
				i+=2;
				for(;;++i)
				{
					if(inp[i] == 32 )
					{
						next_bot_number= t;
						t=0;
						break;
					}
					else if(inp[i] == 10)
					{
						next_bot_number= t;
						t=0;
						check = false;
						break;
					}
					else
					{	t = t*10 +(inp[i] - '0');	}	
				}
				++i;
				
				if( next_bot == 'O')
				{
					temp = next_bot_number - bot1_position;
	//				cout<<"from O:: temp:::"<<temp<<"x is "<<x<<endl;
					if(temp<0)
					{	temp = temp*-1;	}
					if(x>temp)
					{
						bot1_position = next_bot_number;
						time_count += 1;
						x=0;
						y=1;
					}
					else
					{
		//				cout<<"in here fom O"<<endl;
						time_count = time_count + temp - x +1 ;
						bot1_position = next_bot_number;
						x=0;
						//if(prev_bot == next_bot)
						{	y= y + time_count - time_count_prev;	}
						/*else
						{
							cout<<"we are here from O"<<endl;
							y= temp - x + 1;
						}*/
					}
			//		cout<<"from O here from:: y is::"<<y<<" ::x is:::"<<x<<" :::bot_1_pos"<<bot1_position<<"::bot2_position::"<<bot2_position<<":::::::::"<<time_count<<endl;
				}
				else
				{
					temp = next_bot_number - bot2_position;
//					cout<<"from B:: temp:::"<<temp<<"   x is "<<x<<endl;
					if(temp<0)
					{temp = temp*-1;	}
					if(y>temp)
					{
						bot2_position = next_bot_number;
						time_count += 1;
						y=0;
						x=1;
					}
					else
					{
	//					cout<<"in here fom B"<<endl;
						time_count = time_count + temp - y + 1 ;
						bot2_position = next_bot_number;
						y=0;
						//if(prev_bot == next_bot)
						{	x = x + time_count - time_count_prev;	}
						/*else
						{
							x = temp - y + 1;
						}*/
					}
		//			cout<<"from B here from:: y is::"<<y<<" ::x is:::"<<x<<" :::bot_1_pos"<<bot1_position<<"::bot2_position::"<<bot2_position<<":::::::::"<<time_count<<endl;
				}
				time_count_prev = time_count;
				prev_bot = next_bot;
			}
			fwrite(common,1 ,6, stdout);	
			printf("%d%c %d\n", count,':',time_count);
		}
		else
		{	t = t*10 +(inp[i] - '0');	}
	}
	return 0;
}
