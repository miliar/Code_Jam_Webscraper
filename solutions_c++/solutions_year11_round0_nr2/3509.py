#include <iostream>
using namespace std;

#define INPUT_FILE "B.in.txt"
#define OUTPUT_FILE "B.out.txt"

static char combined [36][2];
static char result [36];
static char opposed [28][2];
static int C;
static int D;

static char list [100];
static int  list_size;

static int is_combined(char element, int *index)
{
	for (int c = 0; c < C; c++)
	{
		if ( element == combined[c][0] )
		{
			if ( list[list_size-1] == combined[c][1] )
			{
				*index = c;
				return 1;
			}
		}
		if ( element == combined[c][1] )
		{
			if ( list[list_size-1] == combined[c][0] )
			{
				*index = c;
				return 1;
			}
		}
	}
	return 0;
}

static int is_opposed(char element)
{
	char opposed_element = '-';
	for (int d = 0; d < D; d++)
	{
		if ( element == opposed[d][0] )
		{
			for (int i = 0; i<list_size; i++)
			{			
				if ( opposed[d][1] == list[i] )
				{			
					return 1;
				}
			}
		}
		
		if ( element == opposed[d][1] )
		{
			for (int i = 0; i<list_size; i++)
			{				
				if ( opposed[d][0] == list[i] )
				{
					return 1;
				}
			}
		}
	}
	return 0;
} 

int main()
{
	freopen(INPUT_FILE, "r", stdin);
	freopen(OUTPUT_FILE, "w+", stdout);
	
    int t, T, c, d, n, N;
	char element;
	
    cin >> T;

    for (t = 0; t < T; t++)
    {
        cout << "Case #" << (t+1) << ": ";
		cin >> C;
		for (c = 0; c < C; c++)
		{
			// Elements combined
			cin >> combined[c][0] >> combined[c][1] >> result[c];
		}
		cin >> D;
		for (d = 0; d < D; d++)
		{
			// Elements opposed
			cin >> opposed[d][0] >> opposed[d][1];
		}
		cin >> N;	
		list_size = 0;
		for (n = 0; n < N; n++)
		{
			// Invoke elements
			cin >> element;

			int i;
			if ( list_size == 0 )
			{
				list[list_size++] = element;
			}
			else
			{
				if ( is_combined(element, &i) == 1 )
				{			
					// COMBINED!
					list[list_size-1] = result[i];
				}
				else if ( is_opposed(element) == 1 )
				{			
					// OPPOSED!
					list_size = 0; // Reset list
				}
				else
				{		
					list[list_size++] = element;
				}
			}
		}
		// Result
		cout << "[";
		for (n = 0; n < list_size; n++)
		{ 	
			if ( n > 0 ) cout << ", ";
			cout << list[n];
		}
		cout << "]" << endl;	
    }
	
	return 0;
}