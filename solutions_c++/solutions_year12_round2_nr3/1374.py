// the reason to have fast cpu :)

#include <iostream>
#include <vector>
#include <map>
#include <list>

using namespace std;

template <typename  Container>
void readArray(Container& C, int numberOfEntries)
{
	for(int i = 0; i < numberOfEntries; i++)
	{
	    typename Container::value_type value;
		cin >> value;
		C.push_back(value);
	}
}

vector <int> S;
int N;

bool quickabort;

bool possible(long s, vector<int> &index, int start)
{
	bool b = false;

    vector <int> index2;
    vector <int> index3;

    // printf("%d %d\n", s, start);

    for(int i = start; i < N; i++)
    {
        if( s < S[i]) continue;

    	if( ( s == S[i]) || possible( s - S[i], !b?index2:index3, i + 1))
    	{
    		if(b)
    		{
	    	    index3.push_back(i);

	    	    // found second solution
				for(int i = 0; i < index.size(); i++)
					printf("%d ", S[index[i]]);

				for(int i = 0; i < index2.size(); i++)
				{
					printf("%d ", S[index2[i]]);
					if(i != index2.size() - 1) printf(" ");
				}

				printf("\n");

	    	    // found second solution
				for(int i = 0; i < index.size(); i++)
					printf("%d ", S[index[i]]);

				for(int i = 0; i < index3.size(); i++)
				{
					printf("%d ", S[index3[i]]);
					if(i != index3.size() - 1) printf(" ");
				}

				printf("\n");

				quickabort = true;

				return false;
	    	}
			else
			{

				// printf("Sol!\n");

				index2.push_back(i);
				b = true;
			}
    	}

	    if( quickabort) return false;
    }

    if(b)
    {
    	for(int i = 0; i <  index2.size(); i++) index.push_back( index2[i]);
    }

    return b;
}

void processCase()
{
	cin >> N;

	S.clear();

	readArray(S, N);

	long int sum = 0;
	for(int i =0; i < N; i++) sum += S[i];

	for(int i = 1; i < sum; i++)
	{
	
		vector<int> index;

		quickabort = false;

		possible(i, index, 0);

	    if( quickabort) return;
	}

	printf("Impossible\n");
}

int main(int argc, const char * argv[])
{
	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {
		printf("Case #%d:\n", i + 1);
			processCase();
	}
	
    return 0;
}
