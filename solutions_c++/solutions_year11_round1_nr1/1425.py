
#include <iostream>
#include <vector>
using namespace std;


#define NOT_POSSIBLE 1
#define POSSIBLE 2
#define GOT_IT 3

int check_basic(int Pd, int Pg)
{
	if ((Pg == 100)&&(Pd == 100))
	{
	    return GOT_IT;
	}

	else if ((Pd == 0)&&(Pg == 0))
	{
	    return GOT_IT;
	}

	else if ((Pg == 100)&&(Pd != 100))
	{
	    return NOT_POSSIBLE;
	}

	else if ((Pg == 0)&&(Pd != 0))
	{
	    return NOT_POSSIBLE;
	}

	return POSSIBLE;
}

bool possible(int i, int Pd, int Pg)
{
    int won = Pd*i;
	if (won%100 == 0)
	{
	    return 1;
	}
	return 0;
}

int main(void)
{
    int num_of_cases;
	cin>>num_of_cases;

	int tc_count = 1;
	while(tc_count <= num_of_cases)
	{
		int N, Pd, Pg;
        cin>>N>>Pd>>Pg;
        int flag = 0;
		 
        int basic_res = check_basic(Pd, Pg);

		if (basic_res == GOT_IT)
		{
			flag = 1;
		}
		else if(basic_res == NOT_POSSIBLE)
		{
		    /*  */
		}
		else if (basic_res == POSSIBLE)
		{
			for (int i=1; i<=N; i++)
			{

				if (possible(i, Pd, Pg))
				{
					flag = 1;
					break;
				}

			}
		}

		if (flag)
		{
			cout<<"Case #"<<tc_count<<": Possible\n";
		}
		else
		{
			cout<<"Case #"<<tc_count<<": Broken\n";
		}
		tc_count++;
	}
    return 0;
}