#include <vector>
#include <iostream>

using namespace std;

class Letter
{
public:
		int used_nums;
		int type_nums;
};

int handle_case()
{
		int max_letters;
		int keys;
		int alphabet_letters;
		int sum = 0;

		cin >> max_letters >> keys >> alphabet_letters;

		vector<Letter> alphabet;	
		for( int i = 0; i < alphabet_letters; i++ )
		{
				Letter tmp;
				int j;
				cin >> tmp.used_nums;
				tmp.type_nums = 0;
				for( j = 0; j < alphabet.size(); j++ )
				{
								if( alphabet[j].used_nums < tmp.used_nums ) break;
				}
				alphabet.insert(alphabet.begin()+j, tmp);
		}

		int types = 1;
		for( int i = 0, tmp = keys; i < alphabet_letters; i++, tmp-- )
		{
							if( tmp == 0 )
							{
									types++;
									tmp = keys;
							}
							//if( types > max_letters ) return -1;
							alphabet[i].type_nums = types;
		}

		for( int i = 0; i < alphabet_letters; i++ )
					sum += alphabet[i].used_nums*alphabet[i].type_nums;

		return sum;
}


int main()
{
	int case_nums;
	cin >> case_nums;

	for( int i = 0; i < case_nums; i++ )
	{
		//int ret = handle_case();
		//if( -1 == ret )
		//		cout <<
		cout << "Case #" << i+1 << ": " << handle_case() << endl;
	}
}
