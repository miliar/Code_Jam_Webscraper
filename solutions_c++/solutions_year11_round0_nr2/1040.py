#include <iostream>
using std::cin;
using std::cout;

#define cycle(i,n) for ( i = 0; i < n; i++ )

char combinations[8][8];
bool opposed[8][8];

void clean_up()
{
	int i,j;
	for (i=0;i<8;i++)
	{
		for (j=0;j<8;j++)
		{
			combinations[i][j] = '\0';
			opposed[i][j] = false;
		}
	}
}

char ind_to_char(int index)
{
	static const char symbols[8] = {'Q','W','E','R','A','S','D','F'};
	if (index < 0 || index >7 ) std::cerr << "ind_to_char receiver wrong argument\n";
	return symbols[index];
}

int char_to_ind(char c)
{
	switch (c)
	{
	case 'Q': return 0;
	case 'W': return 1;
	case 'E': return 2;
	case 'R': return 3;
	case 'A': return 4;
	case 'S': return 5;
	case 'D': return 6;
	case 'F': return 7;
	default: return 8;
	}
}

class element_list_class
{
private:
	int size;
	char str[101];
public:
	void reset()
	{
		size = 0;
	}
	void invoke(char c)
	{
		bool combine = false;
		bool collapse = false;
		if (size > 0)
			if ( char_to_ind(str[size-1]) < 8 )
				combine = (combinations[char_to_ind(c)][char_to_ind(str[size-1])] != '\0');

		if ( combine )
		{
			str[size-1] = combinations[char_to_ind(c)][char_to_ind(str[size-1])];
		}
		else
		{
			int s;
			cycle(s,size)
				if ( char_to_ind(str[s]) < 8 )
					if ( opposed[char_to_ind(c)][char_to_ind(str[s])])
						collapse = true;
			if ( collapse )
				reset();
			else
			{
				str[size] = c;
				size++;
			}
		}
	}
	void output()
	{
		int s;
		cout << '[';
		cycle(s,size-1)
		{
			if (str[s] < 'A' || str[s] > 'Z') std::cerr << "wrong output character found\n";
			cout << str[s] << ", ";
		}
		if (size > 0)
			cout << str[size-1];
		cout << ']';
	}
} element_list;

int main()
{
	int t,T;
	
	cin >> T;
	
	cycle(t,T)
	{
		int c,C,d,D,n,N;
		char misc_string[4];
		char invoke_order[101];
		
		clean_up();

		cin >> C;
		cycle(c,C)
		{
			cin >> misc_string;
			combinations[ char_to_ind(misc_string[0]) ][ char_to_ind(misc_string[1]) ] = misc_string[2];
			combinations[ char_to_ind(misc_string[1]) ][ char_to_ind(misc_string[0]) ] = misc_string[2];
		}

		cin >> D;
		cycle(d,D)
		{
			cin >> misc_string;
			opposed[ char_to_ind(misc_string[0]) ][ char_to_ind(misc_string[1]) ] = true;
			opposed[ char_to_ind(misc_string[1]) ][ char_to_ind(misc_string[0]) ] = true;
		}

		cin >> N;
		cin >> invoke_order;

		element_list.reset();
		cycle(n,N)
		{
			element_list.invoke(invoke_order[n]);
		}

		cout << "Case #" << t + 1 << ": ";
		element_list.output();
		cout << "\n";
	}
	
	return 0;
}
