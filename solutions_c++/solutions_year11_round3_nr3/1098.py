

#include <iostream>
#include <vector>
using namespace std;


int main(void)
{
    int num_of_cases;
	cin>>num_of_cases;

	int tc_count = 1;
	while(tc_count <= num_of_cases)
	{
        unsigned int N, L, H;
		cin>>N>>L>>H;

		vector <unsigned int> p_frequencies;

		for (int i=0; i<N; i++)
		{
			unsigned int temp;
			cin>>temp;
			p_frequencies.push_back(temp);
		}

        int eureka = 0;

		for (unsigned int a = L; a<=H; a++)
		{
			bool flag = 1;
			    
			for (unsigned int i=0; i<N; i++)
			{
				if ((p_frequencies[i]%a == 0)||(a%p_frequencies[i] == 0))
				{
				    continue;
				}
				else
				{
					flag = 0;
					break;
				}
			}

			if (flag)
			{
				cout<<"Case #"<<tc_count<<": "<<a<<"\n";
				eureka = 1;
				break;
			}
		}

		if (!eureka)
		{
		    cout<<"Case #"<<tc_count<<": NO\n";
		}

	    tc_count++;
	}
	return 0;
}