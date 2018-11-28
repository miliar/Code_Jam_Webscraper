#include "fstream"
#include "iostream"
#include "cstdlib"
using namespace std;
struct bot_halls{
	int position;
} o_hall, b_hall;

int TTo,TTb;

int T = 0;
int N = 0;

	char ch1;
	int v1, i, j;
	
void move(char, int);

int main()
{

	const int MAX = 5;
	char rows_str[MAX];
	

	
	ifstream infile("A-large.in");
	
	ofstream outfile("A-large.out");
	
	infile.getline(rows_str,MAX);
	
	T = atoi(rows_str);
	
	i = 1;
	while(i <= T)
	{
		infile>>N;
		j=1;
		TTo = 0;
		TTb = 0;
		o_hall.position = 1;
		b_hall.position = 1;

		while(j<=N)
		{
			infile>>ch1;
			infile>>v1;
			move(ch1,v1);
			
			j++;
		}
		if(TTo<TTb)
		{
			TTo = TTb;
		}
		outfile<<"Case #"<<i<<": "<<TTo<<endl;
		i++;
	}

	cout<<endl<<endl;
	
	return 0;
}

void move(char h,int p)
{
	if(h=='O')
	{
		if(p != o_hall.position)
		{
			TTo += abs(p - o_hall.position);
			o_hall.position = p;
		}
		if(TTo<TTb)
		{
			TTo = TTb;
		}
		TTo++;
	}
	if(h=='B')
	{
		if(p != b_hall.position)
		{
			TTb += abs(p - b_hall.position);
			b_hall.position = p;
		}
		if(TTb<TTo)
		{
			TTb = TTo;
		}
		TTb++;
	}
}

	
