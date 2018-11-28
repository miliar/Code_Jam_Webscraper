

#include <iostream>
#include <vector>
using namespace std;

class line
{
public:
    int h1;
	int h2;
};

int main()
{
	int no_of_cases;
	cin>>no_of_cases;
    int T = no_of_cases;

	while(T--)
	{
		int N, tn;
	    cin>>N;
		tn = N;
		vector < line > lines;
		long long int count = 0;
		while(tn--)
		{
		    line l;
			cin>>l.h1>>l.h2;
			lines.push_back(l);
		}
		for (int i=0; i<N; i++)
		{
			for (int j=i+1; j<N; j++)
			{
			    if (((lines[i].h1>lines[j].h1)&&(lines[i].h2<lines[j].h2))
					||((lines[i].h1<lines[j].h1)&&(lines[i].h2>lines[j].h2)))
				{
				    count++;
				}
			}
		}
		cout<<"Case #"<<no_of_cases-T<<": "<<count<<"\n";
	}
    return 0;
}