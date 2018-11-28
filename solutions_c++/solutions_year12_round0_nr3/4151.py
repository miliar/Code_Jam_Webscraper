#include <fstream>
#include <iostream>
using namespace std;

int getlength(int a) //OK
{
	int temp = a;
	int length = 1;

	while(temp>=10)
	{
		temp/=10;
		length++;
	}

	return length;
}

int pow10(int a)
{
	int e=1;

	for(int i = 0; i < a; i++)
	{
		e*=10;
	}

	return e;
}

bool recyclable(int a, int b)
{
	if(getlength(a)!=getlength(b)) return false;

	int length=getlength(a);
	int loop=0;
	int temp=a;

//0일 때는 어떻게 하지??
	do{
		if(temp==b) return true;

		int b = temp/pow10(length-1);
		temp = temp%(pow10(length-1))*10+b;
		loop++;
	}
	while(loop<length);

	return false;
}

int process(int a, int b)
{
	int num_recyclable=0;
	cout<<a<<' '<<b<<endl;
	for(int i = a; i <= b; i++)
	{
		cout<<"i = "<<i<<endl;
		for(int j = i+1; j <=b; j++)
		{
			cout<<"i = "<<i<<" j= "<<j<<endl;
			if(recyclable(i, j))
			{
				cout<<i<<' '<<j<<boolalpha<<recyclable(i,j)<<endl;
				num_recyclable++;
			}
		}
	}
	return num_recyclable;
}

int main()
{
	ifstream input("input.in");
	ofstream output("output.out");

	int input_number=0;
	input>>input_number;

	for(int i = 1; i <= input_number; i++)
	{
		if(input.good())
		{
			int a, b;
			input>>a>>b;

			output<<"Case #"<<i<<": ";
			output<<process(a, b)<<endl;
		}
	}
	input.close();
	output.close();
	return 0;
}
