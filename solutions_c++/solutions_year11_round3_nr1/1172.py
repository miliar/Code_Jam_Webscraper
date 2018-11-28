

#include <iostream>
#include <vector>
using namespace std;

bool convert_if_possible(vector < vector<char> > &picture)
{
	for (int i=0; i<picture.size(); i++)
	{
		for (int j=0; j<picture[i].size(); j++)
		{
			if (picture[i][j] == '#')
			{
				if ((i+1<picture.size())&&(j+1<picture[i].size()))
				{
					if((picture[i][j+1] == '#')&&(picture[i+1][j] == '#')
						&&(picture[i+1][j+1] == '#'))
					{
					    picture[i][j] = '/';
						picture[i+1][j+1] = '/';
						picture[i+1][j] = '\\';
						picture[i][j+1] = '\\';
					}
					else
					{
					    return 0;
					}
				}
				else
				{
					return 0;
				}
			}
		}
	}
	return 1;
}

int main(void)
{
    int num_of_cases;
	cin>>num_of_cases;

	int tc_count = 1;
	while(tc_count <= num_of_cases)
	{
		int R, C;
		cin>>R>>C;
		
		vector < vector<char> > picture;

		for (int i=0; i<R; i++)
		{
			vector <char> row;
			for (int j=0; j<C; j++)
			{
			    char temp;
				cin>>temp;
				row.push_back(temp);
			}
			picture.push_back(row);
		}

		cout<<"Case #"<<tc_count<<":\n";
		if(convert_if_possible(picture))
		{
			for (int i=0; i<R; i++)
			{
				for (int j=0; j<C; j++)
				{
					cout<<picture[i][j];
				}
				cout<<"\n";
			}
		}
		else
		{
		    cout<<"Impossible\n";
		}
		tc_count++;
	}
	return 0;
}