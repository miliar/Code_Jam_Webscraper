#include <iostream>
#include <fstream>

using namespace std;

char* transform[36];
char* opposed[28];
char* str;
char* str_done;

int transform_count;
int opposed_count;
int str_len;
int done;

void processOpposed(char C)
{
	for(int i=0; i<opposed_count; i++)
	{
		if(strchr(opposed[i], C))
		{
			char T;
			T = (opposed[i][0] != C)? opposed[i][0]: opposed[i][1];

			bool found = false;
			for(int j=0; j<strlen(str_done)-1; j++)
			{
				if(str_done[j] == T)
				{
					found = true;
					break;
				}
			}

			if(found)
			{
				for(int i=0; i<str_len; i++)
					str_done[i] = '\0';
			}
		}
	}
}

void processTransform(char C)
{
	for(int i=0; i<transform_count; i++)
	{
		char T;
		bool found = false;

		if(transform[i][0] == C)
		{
			T = transform[i][1];
			found = true;
		}
		else if(transform[i][1] == C)
		{
			T = transform[i][0];
			found = true;
		}

		if(found)
		{
			if(str_done[strlen(str_done)-2] == T)
			{
				str_done[strlen(str_done)-2] = transform[i][2];
				str_done[strlen(str_done)-1] = '\0';

				if(strlen(str_done) != 0 && strlen(str_done) != 1)
					processTransform(str_done[strlen(str_done)-1]);
			}
		}
	}
}

void printString()
{
	cout << "[";

	for(int i=0; i<strlen(str_done); i++)
	{
		if(i!=0)
			cout << ", ";
		cout << str_done[i];
	}

	cout << "]" << endl;
}

int main()
{
	ifstream in;
	in.open("input.txt");

	ofstream out;
	out.open("output.txt");

	for(int i=0; i<36; i++)
	{
		transform[i] = new char[3];
		for(int j=0; j<3; j++)
			transform[i][j] = '\0';
	}
	for(int i=0; i<28; i++)
	{
		opposed[i] = new char[2];
		for(int j=0; j<2; j++)
			opposed[i][j] = '\0';
	}

	int tc = 0;
	int i_tc = 0;

	in >> tc;
	while(i_tc < tc)
	{
		in >> transform_count;
		for(int i=0; i<transform_count; i++)
			in >> transform[i];

		in >> opposed_count;
		for(int i=0; i<opposed_count; i++)
			in >> opposed[i];

		in >> str_len;
		
		done = 0;

		str = new char[str_len];
		in >> str;

		str_done = new char[str_len+1];
		for(int i=0; i<=str_len; i++)
			str_done[i] = '\0';

		for(int i=0; i<str_len; i++)
		{
			char C = str[done];
			str_done[strlen(str_done)] = C;

			if(strlen(str_done) != 0 && strlen(str_done) != 1)
				processTransform(C);
			processOpposed(str_done[strlen(str_done)-1]);
			
			done++;
		}

		out << "Case #" << i_tc+1 << ": ";
		out << "[";

		for(int i=0; i<strlen(str_done); i++)
		{
			if(i!=0)
				out << ", ";
			out << str_done[i];
		}

		out << "]" << endl;

		/*for(int i=0; i<transform_count; i++)
			cout << transform[i] << " ";
		cout << endl;
		for(int i=0; i<opposed_count; i++)
			cout << opposed[i] << " ";
		cout << endl;
		cout << str << endl << endl;*/

		i_tc++;
	}

	cout << endl;
	system("pause");
	return 0;
}