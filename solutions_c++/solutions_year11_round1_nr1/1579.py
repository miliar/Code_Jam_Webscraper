#include <fstream>
#include <iostream>

using namespace std;

int GCD(int num1, int num2)
{
	int temp, a, b;
	if(num1>num2) /*�ҳ��������еĽϴ�ֵ*/
	{
		temp=num1; num1=num2; num2=temp; /*������������*/
	}
	a=num1; b=num2;
	while(b!=0) /*����շת����������Լ��*/
	{
		temp=a%b;
		a=b;
		b=temp;
	}

	return a;
}


int main()
{
	ifstream input ("A-small.in");
	ofstream output ("A-small.out");
	
	int T, t;

	input >> T;

	for(t = 0; t < T; ++t)
	{
		int N, PD, PG;

		input >> N;
		input >> PD;
		input >> PG;
		
		int temp = GCD(PD, 100);
		int temp1 = 100 / temp;
		//cout << temp << endl;
		
		if(temp1 > N)
		{
			output << "Case #" << t+1 << ": " << "Broken" <<endl;	
		}
		else
		{
			if(PG == 100 && PD != 100)
				output << "Case #" << t+1 << ": " << "Broken" <<endl;
			else if(PG == 0 && PD != 0)
				output << "Case #" << t+1 << ": " << "Broken" <<endl;
			else
				output << "Case #" << t+1 << ": " << "Possible" << endl;
		}		
	}

	//system("pause");
	return 0;
}