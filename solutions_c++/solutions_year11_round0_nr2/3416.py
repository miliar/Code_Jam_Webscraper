// magicka.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <list>
using namespace std;

typedef struct {
	char a;
	char b;
} opposing_pair;

typedef struct {
	char a;
	char b;
	char r;
} combining_pair;

int main(int argc, char* argv[])
{
	int num_tests = -1;
	list<opposing_pair> op;
	list<opposing_pair>::iterator op_it;
	list<combining_pair> cp;
	list<combining_pair>::iterator cp_it;
	list<char> elements;
	list<char>::iterator el_it;

	int num_combining_pairs;
	int num_opposing_pairs;
	int num_elements;

	opposing_pair new_op;
	combining_pair new_cp;
	char temp_in[200];
	char new_element;

	printf("Running\n");

	FILE * fin = fopen(argv[1], "r");
	if (!fin)
	{
		printf("Couldn't open input file\n");
		return 1;
	}
	FILE * fout = fopen(argv[2], "w");
	if (!fout)
	{
		printf("Couldn't open output file\n");
		return 2;
	}

	fscanf(fin,"%d",&num_tests);
	printf("Number of tests = %d\n", num_tests);

	for (int i = 0; i < num_tests; i++)
	{
		cp.clear();
		op.clear();
		elements.clear();

		fscanf(fin, "%d", &num_combining_pairs);
		for (int j = 0; j < num_combining_pairs; j++)
		{
			fscanf(fin, "%s", temp_in);
			if (strlen(temp_in) != 3)
				return 42;
			new_cp.a = temp_in[0];
			new_cp.b = temp_in[1];
			new_cp.r = temp_in[2];
			cp.push_back(new_cp);
			new_cp.b = temp_in[0];
			new_cp.a = temp_in[1];
			new_cp.r = temp_in[2];
			cp.push_back(new_cp);
		}

		fscanf(fin, "%d", &num_opposing_pairs);
		for (int j = 0; j < num_opposing_pairs; j++)
		{
			fscanf(fin, "%s", temp_in);
			if (strlen(temp_in) != 2)
				return 42;
			new_op.a = temp_in[0];
			new_op.b = temp_in[1];
			op.push_back(new_op);
			new_op.b = temp_in[0];
			new_op.a = temp_in[1];
			op.push_back(new_op);
		}

		fscanf(fin, "%d", &num_elements);
		fscanf(fin, "%s", temp_in);
		if (strlen(temp_in) != num_elements)
			return 42;
		for (int j = 0; j < num_elements; j++)
		{
			new_element = temp_in[j];
			bool combine = false;
			bool oppose = false;

			// the easiest case - if the elements list is empty, just add the new element
			if (elements.empty())
				elements.push_back(new_element);
			else
			{
				// first check to see if we can combine this new element with anything else
				for (cp_it = cp.begin(); cp_it != cp.end(); cp_it++)
				{
					if ((*cp_it).a == new_element)
					{
						if ((*cp_it).b == elements.back())
						{
							elements.pop_back();
							elements.push_back((*cp_it).r);
							combine = true;
							break;
						}
					}
				}

				if (!combine)
				{
					// next check to see if we oppose anything already in the list
					for (op_it = op.begin(); op_it != op.end(); op_it++)
					{
						if ((*op_it).a == new_element)
						{
							for (el_it = elements.begin(); el_it != elements.end(); el_it++)
							{
								if ((*el_it) == (*op_it).b)
								{
									oppose = true;
									break;
								}
							}
							if (oppose)
								break;
						}
					}
					if (oppose == true)
						elements.clear();
					else // otherwise just tack the new thing onto the end
						elements.push_back(new_element);
				}
			}
		}
		fprintf(fout, "Case #%d: ", i+1);
		if (elements.empty())
			fprintf(fout, "[]\n");
		else
		{
			for (el_it = elements.begin(); el_it != elements.end(); el_it++)
			{
				if (el_it == elements.begin())
					fprintf(fout, "[%c", (*el_it));
				else
					fprintf(fout, ", %c", (*el_it));
			}
			fprintf(fout, "]\n");
		}
	}

}

