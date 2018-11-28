#include <fstream>
#include <string>

using namespace std;

struct ttime
{
	int hour;
	int minute;
	int action; //A_in: 0, B_in: 1, A_out: 2, B_out: 3
};

int N; //number of test cases
int T; //interval
int NA, NB;
ttime timetable[500];

void sort()
{
	int i, j;
	int int_temp;
	for (int i=0;i<(NA+NB)*2;i++)
		for (int j=0;j<(NA+NB)*2;j++)
			if ( ( timetable[i].hour<timetable[j].hour ) || ( ( timetable[i].hour==timetable[j].hour) && ( timetable[i].minute<timetable[j].minute ) )
				|| ( ( timetable[i].hour==timetable[j].hour ) && ( timetable[i].minute==timetable[j].minute ) && ( timetable[i].action<timetable[j].action ) ) )
			{
				int_temp = timetable[j].hour;
				timetable[j].hour = timetable[i].hour;
				timetable[i].hour = int_temp;
				int_temp = timetable[j].minute;
				timetable[j].minute = timetable[i].minute;
				timetable[i].minute = int_temp;
				int_temp = timetable[j].action;
				timetable[j].action = timetable[i].action;
				timetable[i].action = int_temp;
			}
}

int main()
{
	int i, j;
	int ANow, BNow, AOut, BOut;
    string temp;
	ifstream input_file("B-small.in");
//	ifstream input_file("B-large.in");
	ofstream output_file("B-small.out");
//  ofstream output_file("B-large.out");
	input_file>>N;
	for (i = 1; i<=N; i++)
	{
		ANow = 0;
		BNow = 0;
		AOut = 0;
		BOut = 0;
		input_file>>T;
	    input_file>>NA;
		input_file>>NB;
		for (j = 0;j<NA;j++)
		{
			input_file>>temp;
			timetable[j*2].hour = ( temp[0] - 48 )*10 + temp[1] - 48;
			timetable[j*2].minute = ( temp[3] - 48 )*10 + temp[4] - 48;
			timetable[j*2].action = 2; //start from A
			input_file>>temp;
			timetable[j*2+1].hour = ( temp[0] - 48 )*10 + temp[1] - 48;
			timetable[j*2+1].minute = ( temp[3] - 48 )*10 + temp[4] - 48 + T;
			if ( timetable[j*2+1].minute>59 )
			{
				timetable[j*2+1].hour++;
				timetable[j*2+1].minute-=59;
			}
			timetable[j*2+1].action = 1; //arrive B
		}
		for (j = NA;j<NA+NB;j++)
		{
			input_file>>temp;
			timetable[j*2].hour = ( temp[0] - 48 )*10 + temp[1] - 48;
			timetable[j*2].minute = ( temp[3] - 48 )*10 + temp[4] - 48;
			timetable[j*2].action = 3; //start from B
			input_file>>temp;
			timetable[j*2+1].hour = ( temp[0] - 48 )*10 + temp[1] - 48;
			timetable[j*2+1].minute = ( temp[3] - 48 )*10 + temp[4] - 48 + T;
			if ( timetable[j*2+1].minute>59 )
			{
				timetable[j*2+1].hour++;
				timetable[j*2+1].minute-=59;
			}			
			timetable[j*2+1].action = 0; //arrive A
		}
		sort();
		for (j=0;j<(NA+NB)*2;j++)
		{
//			output_file<<timetable[j].hour<<":"<<timetable[j].minute<<endl;
			if ( timetable[j].hour<24 )
			{
				switch ( timetable[j].action )
				{
					case 1: //arrive B
					{
						BNow++;
						break;
					}
					case 0: //arrive A
					{
						ANow++;
						break;
					}
					case 3: //leave B
					{
						if ( BNow>0 )
							BNow--;
						else
							BOut++;
						break;
					}
					case 2: //leave A
					{
						if ( ANow>0 )
							ANow--;
						else
							AOut++;
						break;
					}
				}
			}
//			output_file<<"ANow: "<<ANow<<" AOut: "<<AOut<<" BNow: "<<BNow<<" BOut: "<<BOut<<endl;
		}
		output_file<<"Case #"<<i<<": "<<AOut<<" "<<BOut<<endl;
	}
	return 0;
}
