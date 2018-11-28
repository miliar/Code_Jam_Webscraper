#include <iostream>
#include <fstream>
#include <string>
#include <math.h>

using namespace std;

class RoboTask
{
	private:
		int order[110];
		int butt[110];
		int index,top;
		
	public:
		RoboTask()
		{
			clear();
		}

		int getorder(void)
		{
			if ( index < top )
			{
				return order[index];
			}
			else
			{
				//cout << "queue is empty" << endl;
				return 120;
			}
		}
		
		int getbutt(void)
		{
			if ( index < top )
			{
				return butt[index];
			}
			else
			{
				cout << "queue is empty" << endl;
				return 0;
			}
		}

		int add(int ord , int but )
		{
			if ( top <= 110 )
			{
				order[top] = ord;
				butt[top] = but;
				++top;
				return 1;
			}
			else
			{
				cout << "queue is full" << endl;
				return 0;
			}

		}

		int next(void)
		{
			if ( index <= top )
			{
				current = butt[index];
				++index;
				return 1;
			}
			else
			{
				cout << "queue is empty" << endl;
				return 0;
			}
		}

		bool isempty()
		{
			if ( index == top )
				return true;
			else
				return false;
		}

		void walkcalc(void)
		{
			if ( !isempty() )
			{
				walk = abs(getbutt() - current ) +1 ;
			}
			else
			{
				walk = 0;
			}
		}

		int current;
		int walk;

		void clear(void)
		{
			int i;
			for ( i=0 ; i<110 ; ++i)
			{
				order[i]=0;
				butt[i]=0;
			}
			index = 0;
			top = 0;
			current = 1;
		}

};

int main()
{
	RoboTask Blue,Orange,*Before,*After;
	ifstream inp;
	ofstream oup;
	int tc,num,i,j,butt;
	char robot;

	oup.open("D:\\A-large.out");

	inp.open("D:\\A-large.in");
	inp >> tc;

	for ( i=0 ; i<tc ; ++i )
	{
		Blue.clear();
		Orange.clear();

		inp >> num ;
		for ( j=0 ; j<num ; ++j )
		{
			inp >> robot >> butt ;
			if ( robot == 'B' )
			{
				Blue.add(j,butt);
			}
			else if ( robot == 'O' )
			{
				Orange.add(j,butt);
			}
		}

		j=0;

		Orange.walkcalc();
		Blue.walkcalc();

		while( !Orange.isempty() || !Blue.isempty()  )
		{
			
			if ( Orange.getorder() < Blue.getorder() )
			{
				Before = &Orange;
				After = &Blue;
			}
			else
			{
				Before = &Blue;
				After = &Orange;
			}

			if ( (*After).walk > 1 )
			{
				if ( (*Before).walk  >= (*After).walk )
				{
					(*After).walk = 1;
				}
				else
				{
					(*After).walk -= (*Before).walk;
				}
			}
			
			j+= (*Before).walk  ;
			
			(*Before).next();

			if ( !(*Before).isempty()  )
			{
				(*Before).walkcalc();
			}
			else
			{
				(*Before).walk = 0 ;
			}

		}

		oup << "Case #" << i+1 << ": " << j;

		if ( i < tc-1 )
			oup << "\n";

	}

	inp.close();
	oup.close ();
	return 0;
}