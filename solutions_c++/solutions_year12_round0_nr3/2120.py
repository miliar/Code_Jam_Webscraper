#include <fstream>

using namespace std;

int output_value;

int A,B;

int move1(int num)
{
	int temp = num % 10;
	num = num / 10;
	return temp * 1000000 + num;
}

int move2(int num)
{
	int temp = num % 10;
	num = num / 10;
	return temp * 100000 + num;
}

int move3(int num)
{
	int temp = num % 10;
	num = num / 10;
	return temp * 10000 + num;
}

int move4(int num)
{
	int temp = num % 10;
	num = num / 10;
	return temp * 1000 + num;
}

int move5(int num)
{
	int temp = num % 10;
	num = num / 10;
	return temp * 100 + num;
}

int move6(int num)
{
	int temp = num % 10;
	num = num / 10;
	return temp * 10 + num;
}

int move7(int num)
{
	int temp = num % 10;
	num = num / 10;
	return temp + num;
}

void run()
{
	output_value = 0;
	int num, temp_num;
	if(A >= 1000000)
	{
		for(int i=A;i<=B;i++)
		{
			num = i;
			while(i != (temp_num = move1(num)))
			{
				if (temp_num <= B && i < temp_num)
					output_value++;
				num = temp_num;
			}
		}
	}
	else if(A >= 100000)
	{
		for(int i=A;i<=B;i++)
		{
			num = i;
			while(i != (temp_num = move2(num)))
			{
				if (temp_num <= B && i < temp_num)
					output_value++;
				num = temp_num;
			}
		}
	}
	else if(A >= 10000)
	{
		for(int i=A;i<=B;i++)
		{
			num = i;
			while(i != (temp_num = move3(num)))
			{
				if (temp_num <= B && i < temp_num)
					output_value++;
				num = temp_num;
			}
		}
	}
	else if(A >= 1000)
	{
		for(int i=A;i<=B;i++)
		{
			num = i;
			while(i != (temp_num = move4(num)))
			{
				if (temp_num <= B && i < temp_num)
					output_value++;
				num = temp_num;
			}
		}
	}
	else if(A >= 100)
	{
		for(int i=A;i<=B;i++)
		{
			num = i;
			while(i != (temp_num = move5(num)))
			{
				if (temp_num <= B && i < temp_num)
					output_value++;
				num = temp_num;
			}
		}
	}
	else if(A >= 10)
	{
		for(int i=A;i<=B;i++)
		{
			num = i;
			while(i != (temp_num = move6(num)))
			{
				if (temp_num <= B && i < temp_num)
					output_value++;
				num = temp_num;
			}
		}
	}
	else
	{
		for(int i=A;i<=B;i++)
		{
			num = i;
			while(i != (temp_num = move7(num)))
			{
				if (temp_num <= B && i < temp_num)
					output_value++;
				num = temp_num;
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
	ifstream in("C-large.in");
	ofstream out("output_c.txt");
	in >> T;
	for(int i=0;i<T;i++)
	{
		in >> A >> B;
		run();
		output(i, &out);
	}
	in.close();
	out.close();
}