#include <vector>
#include <string>
using namespace std;

void main()
{

	freopen("large.in", "r", stdin);
	//freopen("small.in", "r", stdin);

	freopen("output.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	for(int i=0; i<n; ++i)
	{

		//printf("%d Search engines\n", n);
		int cantEngine;
		scanf("%d\n", &cantEngine);

		vector <string> names(cantEngine);

		for(int j=0; j<cantEngine; ++j)
		{
			char name[103];
			gets(name);
			//printf("%s\n", name);
			names[j] = name;
		}

		int cantQuery;
		scanf("%d\n", &cantQuery);

		//printf("\nquerys:\n");

		bool visited[103];

		memset(visited, false, sizeof(visited));

		int cant = 0;
		int swaps = 0;
		for(int j=0; j<cantQuery; ++j)
		{
			char name[103];
			gets(name);
			string q = name;

			for(int k=0; k<cantEngine; ++k)
			{
				if(q == names[k])
				{
					if(!visited[k]) 
					{
						if(cant == cantEngine-1)
						{
							memset(visited, false, sizeof(visited));
							++swaps;
							cant=0;
						}

						cant++;
					}
					visited[k] = true;
				}
			}

			
		}

		printf("Case #%d: %d\n", i+1, swaps);
	}

}