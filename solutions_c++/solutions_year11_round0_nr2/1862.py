#include<stdio.h>
#include<map>
#include<list>
using namespace std;
int main()
{
	int num_tests = 0;
	map<char,int> base_elements;
	base_elements['Q'] = 1;	
	base_elements['W'] = 2;
	base_elements['E'] = 3;
	base_elements['R'] = 4;
	base_elements['A'] = 5;
	base_elements['S'] = 6;
	base_elements['D'] = 7;
	base_elements['F'] = 8;
	scanf("%d",&num_tests);
	for (int q = 1; q <= num_tests ; q++)
	{
		char combos[9][9] = {0};
		bool destroys[9][9] = {false};
		int num_combinations;
		scanf("%d",&num_combinations);
		for (int i=0 ; i < num_combinations; i++)
		{
			char src1,src2,dst;
			scanf(" %c%c%c",&src1,&src2,&dst);
			combos[base_elements.find(src1)->second][base_elements.find(src2)->second] 
				= dst;
			combos[base_elements.find(src2)->second][base_elements.find(src1)->second] 
				= dst;
		}
		int num_destructions;
		scanf("%d",&num_destructions);
		for (int i=0 ; i < num_destructions; i++)
        {
            char src1,src2,dst;
            scanf(" %c%c%c",&src1,&src2,&dst);
            destroys[base_elements.find(src1)->second][base_elements.find(src2)->second]
                = true;
            destroys[base_elements.find(src2)->second][base_elements.find(src1)->second]
                = true;
        }
		int num_chars;
		scanf("%d",&num_chars);
		list<char> l;
		int count[9] =  {0};
		for (int i=0 ; i < num_chars ; i++)
		{
			char inp;
			scanf(" %c",&inp);
			if (!l.empty())
			{
				
				char combo = 0;
				if (base_elements.find(l.back()) != base_elements.end()) 
			  	{
					combo = combos[base_elements.find(l.back())->second][base_elements.find(inp)->second];
				}
				if (combo > 0)
				{
						count[base_elements.find(l.back())->second]--;
						l.pop_back();
						l.push_back(combo);
						continue;
				}

				bool destroy = false;
				for (int j = 1;  j < 9 ; j++)
				{
					if(count[j] > 0 && (destroys[base_elements.find(inp)->second][j]))
						destroy = true;
				}
				if ( destroy )
				{
				 	l.clear();
					for (int j = 1; j < 9 ; j++)
					{
						count[j]=0;
					}
					continue;
				}

				if ( combo == 0)
				{	
					l.push_back(inp);
					count[base_elements.find(inp)->second]++;
				}
			}
			else
			{
				l.push_back(inp);
				count[base_elements.find(inp)->second]++;
			}
		}
		printf("Case #%d: [",q);
		while (!l.empty())
		{
			printf("%c%s",l.front(),l.size()==1?"":", ");
			l.pop_front();
		}
		printf("]");	
		printf("\n");
	}	
}
