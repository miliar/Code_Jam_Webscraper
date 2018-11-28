#include "stdafx.h"
#include "iostream"
#include <string>
#include <fstream>
#include <cmath>
#include <vector>


using namespace std;


double process_A(int A, int B, double *prob)
{
	double *pr_solved = new double[A];

	pr_solved[0] = prob[0];
	for(int i = 1; i < A; i++)
	{
		pr_solved[i] = pr_solved[i - 1] * prob[i];
	}

	double pr_all_correct = pr_solved[A-1];
	

	double pr_one_wrong = 1 - pr_all_correct;
	double keep_trying = (B - A + 1) * pr_all_correct + (B - A + 1 + B + 1) * pr_one_wrong;

	double option1 = keep_trying;
	double pr_not_solved;



	double option2 = 32767;
	for(int i = 1; i <= A; i++ )
	{
		double erase_i_char = pr_solved[A-1-i] * (B - A + 2* i + 1) + (1 - pr_solved[A-1-i]) * (B - A + 2*i + 1 + B + 1);
		if(erase_i_char < option2)option2 = erase_i_char;
	}

	double option3 = 2 + B;

	
	if(option1 <= option2)
	{
		if(option1 <= option3)
			return option1;
		else
			return option3;
	}
	else
	{
		if(option2 <= option3)
			return option2;
		else
			return option3;
	}

	return 0;
}


void probA_password()
{
	ofstream out;
	out.open("E://smallA.out");
	int A, B;
	double *prob = NULL;
	int T;
	cin >> T;
	for(int i = 0; i < T; i++)
	{
		cin >> A >> B;
		prob = NULL;
		prob = new double[A];
		
		for(int j = 0 ; j < A; j++)
		{
			cin >> prob[j];
		}

		double value = process_A(A, B, prob);

		cout.precision(6);
		  cout.setf(ios::fixed,ios::floatfield); 
		cout <<"Case #" << i + 1 << ": " << value << endl;
		//out <<"Case #" << i + 1 << ": " << count << endl;
	}


}

int main()
{

	probA_password();
	return 0;
}