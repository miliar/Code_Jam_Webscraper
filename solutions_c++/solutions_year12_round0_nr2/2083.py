#include <fstream>

using namespace std;

int output_value;
int N;
int S;
int p;
int scores[100];

void run()
{
	output_value = 0;
	if(p==1)
	{
		for(int i=0;i<N;i++)
		{
			if(scores[i] > 0)
				output_value++;
		}

	}
	else
	{
		for(int i=0;i<N;i++)
		{
			if(scores[i] > (p-1)*3)
				output_value++;
			else if(S > 0 && scores[i] >= p*3-4)
			{
				S--;
				output_value++;
			}
		}
	}
}

void output(int num, ofstream* out)
{
	*out << "Case #" << num+1 << ": " << output_value << '\n';
}

int main()
{
	int T;
	ifstream in("B-large.in");
	ofstream out("output.txt");
	in >> T;
	for(int i=0;i<T;i++)
	{
		in >> N >> S >> p;
		for(int j=0;j<N;j++)
			in >> scores[j];
		run();
		output(i, &out);
	}
	in.close();
	out.close();
}