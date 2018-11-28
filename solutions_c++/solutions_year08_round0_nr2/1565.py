// train.cpp : Defines the entry point for the console application.
//

#include<fstream>
using namespace std;

struct time{
	int hour;
	int min;
};
int t_match(time t1,time t2)
{
	return t1.hour*60+t1.min-t2.hour*60-t2.min;
}
time t_add(time t1,time t2)
{
	int i_temp=t1.hour*60+t1.min+t2.hour*60+t2.min;
	time t_temp;
	t_temp.min=i_temp%60;
	t_temp.hour=i_temp/60;
	return t_temp;
}
int main()
{
	time departure[200];
	time   arrivel[200];
	int   location[200];
	int number_of_cases;
	time turnaround_time;
	int trips_station_a;
	int trips_station_b;
	int total_trips;
	ifstream  in_stream;
	ofstream out_stream;
	in_stream.open  ("B-small.in");
	out_stream.open("B-small.out");
	int i,j,k;
	char c_temp;
	time t_temp;
	time t_min;
	int i_temp;
	int i_min;
	int trains[2];
	int index;
	bool flag;

	
	in_stream>>number_of_cases;
	for(i=0;i<number_of_cases;++i)
	{
		trains[0]=0;
		trains[1]=0;
		turnaround_time.hour=0;
		in_stream>>turnaround_time.min;
		in_stream>>trips_station_a;
		in_stream>>trips_station_b;
		total_trips=trips_station_a+trips_station_b;
		for(j=0;j<trips_station_a;++j)
		{
			in_stream>>departure[j].hour>>c_temp>>departure[j].min;
			in_stream>>arrivel[j].hour>>c_temp>>arrivel[j].min;
			location[j]=1;
		}
		for(j=trips_station_a;j<total_trips;++j)
		{
			in_stream>>departure[j].hour>>c_temp>>departure[j].min;
			in_stream>>arrivel[j].hour>>c_temp>>arrivel[j].min;
			location[j]=2;
		}
		
		for(j=0;j<total_trips;++j)
		{
			t_min=departure[j];
			i_min=j;
			flag=false;
			for(k=j+1;k<total_trips;++k)
			{
				if(t_match(t_min,departure[k])>0)
				{
					i_min=k;
					t_min=departure[k];
					flag=true;
				}
			}
			if(flag)
			{
				t_temp=departure[j];
				departure[j]=departure[i_min];
				departure[i_min]=t_temp;
				t_temp=arrivel[j];
				arrivel[j]=arrivel[i_min];
				arrivel[i_min]=t_temp;
				i_temp=location[j];
				location[j]=location[i_min];
				location[i_min]=i_temp;
			}
		}

		for(j=0;j<total_trips;++j)
		{
			if(location[j])
			{
				trains[location[j]-1]++;
				t_min=t_add(arrivel[j],turnaround_time);
				i_min=location[j]%2+1;
				location[j]=0;
				for(k=j+1;k<total_trips;++k)
				{
					if(i_min==location[k] && t_match(t_min,departure[k])<=0)
					{
						t_min=t_add(arrivel[k],turnaround_time);
						i_min=location[k]%2+1;
						location[k]=0;
					}				
				}
			}
		}
		out_stream<<"Case #"<<i+1<<": "<<trains[0]<<" "<<trains[1]<<endl;

		/*for(j=0;j<total_trips;++j)
		{
			out_stream<<departure[j].hour<<":"<<departure[j].min<<" ";
			out_stream<<arrivel[j].hour<<":"<<arrivel[j].min<<" ";
			out_stream<<location[j]<<endl;
		}*/


				
		

	}

	return 0;
}

