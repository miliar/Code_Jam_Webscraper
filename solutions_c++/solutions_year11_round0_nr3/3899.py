#include <iostream>
#include <string>
using namespace std;

#define LIST_SMALL_INP 15

unsigned long int rec_wrong_sum( int it_s, const int it_e, unsigned long int *val)
{
	if(it_s == it_e) return 0;

	return val[it_s]^rec_wrong_sum(it_s+1, it_e, val);
}
unsigned long int rec_correct_sum( int it_s, const int it_e, unsigned long int *val)
{
	if(it_s == it_e) return 0;

	return val[it_s]+rec_correct_sum(it_s+1, it_e, val);
}
int main()
{
	int test_num=0;
	cin >> test_num;
	
	std::string outputStr;

	int it_test;
	for(it_test=0; it_test < test_num; it_test++)
	{
		int candy_num = 0;
		cin >> candy_num;		
		
		unsigned long int candy_values[LIST_SMALL_INP*2]={0};

		//read comb;
		int it_candy;
		for( it_candy=0; it_candy< candy_num; it_candy++)
		{
			cin >> candy_values[it_candy];
			candy_values[it_candy+candy_num]=candy_values[it_candy];
		}

		int it=0;
		unsigned long int max_csum = 0;
		unsigned long int max_csum1 = 0;
		unsigned long int max_csum2 = 0;
		unsigned long int max_wsum = 0;
		if( candy_num > 2 )
		{
			for( it = 0; it < candy_num; it++)
			{
				for(int comb = 1; comb < candy_num; comb++)
				{
					int cdy_for_s = candy_num - ((it+comb)-it);
					unsigned long int wsum1 = rec_wrong_sum( it, it+comb, candy_values);
					unsigned long int wsum2 = rec_wrong_sum( it+comb, candy_num+it, candy_values);
					if( wsum1 == wsum2)
					{
						unsigned long int csum1 = rec_correct_sum(  it, it+comb, candy_values);
						unsigned long int csum2 = rec_correct_sum( it+comb, candy_num+it, candy_values);
						unsigned long int max_curr = csum1 > csum2 ? csum1 : csum2;
						if( max_curr > max_csum )
						{
							max_csum = max_curr;
							max_wsum = wsum1;
							max_csum1 = csum1; max_csum2 = csum2;
						}
					}
				}				
			}
		}
		else if( candy_num == 2 && candy_values[0] == candy_values[1])
		{
			max_csum = candy_values[0];
		}
		
		cout << "Case #" << it_test+1 << ": " << max_csum << "[ " << max_wsum << ", " << max_csum1 << ", " << max_csum2 << endl;
		
		// temp
		char outp[100];
		sprintf( outp, "Case #%d: ", it_test+1 );
		outputStr += outp;

		if( max_csum == 0 )
			outputStr += "NO\n";
		else
		{
			sprintf( outp, "%u\n", max_csum );
			outputStr += outp;
		}
	}
	//std::cout << "Hellow " << std::endl;
	cout << "Output " << endl << endl;
	cout << outputStr;
	return 0;
}
