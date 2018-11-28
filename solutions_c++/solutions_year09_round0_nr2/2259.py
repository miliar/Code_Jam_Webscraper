#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>

using namespace std;


class Land
{
public:
	int value;
	int type;
	Land* next;

	Land::Land() : value(10001), type(-1), next(NULL)
	{

	}
};

int main()
{
	int test = 0;
	int x = 0;
	int y = 0;

	ifstream ifs( "test.txt" );
	ofstream ofs( "output.txt" );

	ifs >> test;

	for(int k = 0; k < test; ++k)
	{
		Land** data;
		ofs << "Case #" << k + 1 << ": " << endl;

		ifs >> y >> x;

		data = new Land*[x + 2];
		for(int i = 0; i < x + 2; ++i)
		{
			data[i] = new Land[y + 2];
		}

		for(int i = 1; i < y + 1; ++i)
		{
			for(int j = 1; j < x + 1; ++j)
			{
				ifs >> data[j][i].value;
			}
		}

		for(int i = 1; i < y + 1; ++i)
		{
			for(int j = 1; j < x + 1; ++j)
			{
				int mini = data[j][i].value;
				mini = min(data[j][i - 1].value, mini);
				mini = min(data[j - 1][i].value, mini);
				mini = min(data[j + 1][i].value, mini);
				mini = min(data[j][i + 1].value, mini);

				if(data[j][i].value == mini)
				{

				}
				else if(data[j][i - 1].value == mini)
				{
					data[j][i].next = &data[j][i - 1];
				}
				else if(data[j - 1][i].value == mini)
				{
					data[j][i].next = &data[j - 1][i];
				}
				else if(data[j + 1][i].value == mini)
				{
					data[j][i].next = &data[j + 1][i];
				}
				else if(data[j][i + 1].value == mini)
				{
					data[j][i].next = &data[j][i + 1];
				}
			}
		}

		int type = 0;
		for(int i = 1; i < y + 1; ++i)
		{
			for(int j = 1; j < x + 1; ++j)
			{
				Land* current = data[j][i].next;
				Land* prev = NULL;
				while(current != NULL)
				{
					prev = current;
					current = current->next;
				}
				if(prev == NULL)
				{
					prev = &data[j][i];
				}
				if(prev->type == -1)
				{
					prev->type = type;
					data[j][i].type = type;
					type++; 
				}
				else
				{
					data[j][i].type = prev->type;
				}
			}
		}

		for(int i = 1; i < y + 1; ++i)
		{
			for(int j = 1; j < x + 1; ++j)
			{
				ofs << static_cast<char>('a' + data[j][i].type) << " ";
			}
			ofs << endl;
		}

		for(int i = 0; i < x + 2; ++i)
		{
			delete[] data[i];
		}

		delete[] data;

	}

	return 0;
}