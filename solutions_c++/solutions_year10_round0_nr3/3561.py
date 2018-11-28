#include<iostream>
#include<fstream>
#include<deque>
#include<cstdio>
using namespace std;

int main()
{
	FILE *in;
	FILE *out;
	in = fopen("input.txt", "r");
	out = fopen("output.txt", "w");

	int num = 0;

	fscanf_s(in, "%d", &num);
	for (int i = 0; i <  num; i++)
	{
		int result = 0;
		int times = 0, sit = 0, group = 0;
		
		fscanf_s(in, "%d %d %d", &times, &sit, &group);

		deque<int> people;
		
		for (int j = 0; j < group; j++)
		{
			int tmp;
			fscanf_s(in, "%d", &tmp);
			people.push_back(tmp);
		}

		int up = 0;
		int dollar = 0;
		int count_group = 0;
		for (int t = 0; t < times;)
		{
			if (up + people[0] > sit || count_group == group)
			{
				count_group = 0;
				dollar += up;
				up = 0;		
				t++;
			}
			count_group++;
			up += people[0];
			people.push_back(people[0]);
			people.pop_front();
		}

		fprintf(out, "Case #%d: %d\n", i + 1, dollar);
	}

	fclose(in);
	fclose(out);
	system("pause");
	return 0;
}