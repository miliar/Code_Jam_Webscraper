#include <iostream>
#include <vector>
#include <string>
#include <set>
using namespace std;

struct node
{
	char a, b, c;
};

int main()
{
	FILE* in = fopen("in", "r");
	FILE* out = fopen("out.txt","w+");

	int n, m;
	char ll;

	fscanf(in, "%d", &n);
	for (int cas = 1; cas <= n; cas++)
	{
		vector<node> change;
		vector<node> opp;

		fscanf(in, "%d", &m);
		
		for (int i = 0; i < m; i++)
		{
			node tem;
			//getchar();
			fscanf(in, "%c", &ll);
			fscanf(in, "%c%c%c", &tem.a, &tem.b, &tem.c);
			change.push_back(tem);
		}

		fscanf(in, "%d", &m);
		for (int i = 0; i < m; i++)
		{
			node tem;
			//getchar();
			fscanf(in, "%c", &ll);
			fscanf(in, "%c%c", &tem.a, &tem.b);
			opp.push_back(tem);
		}
		
		fscanf(in, "%d", &m);
		//fgetchar(in);
		fscanf(in, "%c", &ll);
		vector<char> ans;
		set<char> col;
		for (int i = 0; i < m; i++)
		{
			char ch;
			fscanf(in, "%c", &ch);
			if (ans.size() == 0)
				ans.push_back(ch);
			else
			{
				char last = ans[ans.size() - 1];
				bool flag = true;
				for (int j = 0; j < change.size();  j++)
				{
					if ((ch == change[j].a && last == change[j].b) || (ch == change[j].b && last == change[j].a))
					{
						ans[ans.size() - 1] = change[j].c;
						flag = false;
						break;
					}
				}

				if (flag)
				{
					for (int j = 0; j < opp.size() && flag; j++)
					{
						if (ch == opp[j].a || ch == opp[j].b)
						{
							char ju = ((ch == opp[j].a) ? opp[j].b : opp[j].a);
							for (int k = 0; k < ans.size() && flag; k++)
							{
								if (ans[k] == ju)
								{
									ans.clear();
									flag = false;
								}
							}
						}
					}
				}
				if (flag)
				{
					ans.push_back(ch);
				}
				
			}

			
		}
		printf("Case #%d: [", cas);
		fprintf(out, "Case #%d: [", cas);
			for (int i = 0; i < ans.size(); i++)
			{
				if (i != 0)
				{
					fprintf(out, ", ");
					printf(", ");
				}
				fprintf(out, "%c", ans[i]);
				printf("%c", ans[i]);
			}
			fprintf(out, "]\n");
			printf("]\n");
 	}
	fclose(out);
	fclose(in);

	system("pause");

	return 0;
}