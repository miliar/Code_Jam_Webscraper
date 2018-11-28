// t01.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "iostream.h"
#include "string.h"
#include "math.h"

int main(int argc, char* argv[])
{
	int		num_cases = 0;

	FILE	*fp = fopen("A-large.in.txt","rt");
	FILE	*fp2 =fopen("OutputL.txt","wt");

	if (!fp)
	{
		cout<<"Error opening file A-small-attempt0.in.txt"<<endl;
		return 0;
	}
	fscanf(fp, "%d", &num_cases);

	for(int icase=0;icase<num_cases;icase++)
	{
		int		s, q;
		int		i;
		int		j;

		char	**list_s, **list_q;

		cout<<"Case #"<<icase+1<<": ";
		fprintf(fp2, "Case #%d: ", icase+1);

		fscanf(fp, "%d", &s);
		list_s = (char**) new char*[s];
		if (list_s==NULL)
		{
			cout<<"Not enough memory!"<<endl;
			return 0;
		}

		fgetc(fp);	// ignore the leading '\n '

		for (i=0; i<s; i++)
		{
			list_s[i] = (char*) new char[101];
			if (list_s[i]==NULL)
			{
				cout<<"Not enough memory!"<<endl;
				return 0;
			}
			char	char_read_from_input;
			int		int_read_from_input;
			int_read_from_input = fgetc(fp);
			if (int_read_from_input!=EOF)
			{
				char_read_from_input = (char) int_read_from_input;
			}
			else
			{
				cout<<"EOF!!"<<endl;
				return 0;
			}
			for (j=0; (j<100)&&(char_read_from_input!='\n'); j++)
			{
				list_s[i][j] = char_read_from_input;
				int_read_from_input = fgetc(fp);
				if (int_read_from_input!=EOF)
				{
					char_read_from_input = (char) int_read_from_input;
				}
				else
				{
					cout<<"EOF!!"<<endl;
					return 0;
				}
			}
			list_s[i][j]=0;
		}

		fscanf(fp, "%d", &q);
		list_q = (char**) new char*[q];
		if (list_q==NULL)
		{
			cout<<"Not enough memory!"<<endl;
			return 0;
		}

		fgetc(fp);	// ignore the leading '\n '

		for (i=0; i<q; i++)
		{
			list_q[i] = (char*) new char[101];
			if (list_q[i]==NULL)
			{
				cout<<"Not enough memory!"<<endl;
				return 0;
			}
			char	char_read_from_input;
			int		int_read_from_input;
			int_read_from_input = fgetc(fp);
			if (int_read_from_input!=EOF)
			{
				char_read_from_input = (char) int_read_from_input;
			}
			else
			{
				cout<<"EOF!!"<<endl;
				return 0;
			}
			for (j=0; (j<100)&&(char_read_from_input!='\n'); j++)
			{
				list_q[i][j] = char_read_from_input;
				int_read_from_input = fgetc(fp);
				if (int_read_from_input!=EOF)
				{
					char_read_from_input = (char) int_read_from_input;
				}
				else
				{
					cout<<"EOF!!"<<endl;
					return 0;
				}
			}
			list_q[i][j]=0;
		}

		int	num_switches = -1;

		int	chosen_engine = -1;
		int	first_appears = -1;

		bool	need_to_switch = true;

		for (i=0; i<q; i++)
		{
			if (need_to_switch)
			{
				chosen_engine = 0;
				first_appears = -1;

				for (j=0; j<s; j++)
				{
					bool	got_it = false;
					if (strcmp(list_s[j], list_q[i])==0)
					{
						continue;
					}
					for (int ii=i; (ii<q)&&(got_it==false); ii++)
					{
						if (strcmp(list_s[j], list_q[ii])==0)
						{
							got_it = true;
							if (ii>first_appears)
							{
								first_appears = ii;
								chosen_engine = j;
							}
						}
					}
					if (got_it==false)
					{
						chosen_engine = j;
						break;
					}
				}
//				cout<<i<<":["<<list_q[i]<<"]"<<list_s[chosen_engine]<<endl;
				num_switches++;
				need_to_switch = false;
			}

			if ( (i+1<q)
				&& (strcmp(list_s[chosen_engine], list_q[i+1])==0) )
			{
				need_to_switch = true;
			}

		}

		if (q==0) num_switches++;

		cout<<num_switches<<endl;
		fprintf(fp2, "%d\n", num_switches);


		for (i=0; i<s; i++)
		{
			delete[] list_s[i];
		}
		delete[] list_s;
		for (i=0; i<q; i++)
		{
			delete[] list_q[i];
		}
		delete[] list_q;

	}
	return 0;
}


