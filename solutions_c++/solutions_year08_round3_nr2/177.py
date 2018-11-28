#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cctype>
#include <string>
#include <vector>
using namespace std;


long long calculate_number_of_ugly(string k, long long* value  )
{
	if((k.length() == 1 ) )
	{
		long long number ;
		number = atoll(k.c_str());
		if(number == 0) { return 1; }
		
		if(number % 2 == 0) { return 1; }
		if(number % 3 == 0) { return 1; }
		if(number % 5 == 0) { return 1; }
		if(number % 7 == 0) { return 1; }
		
		return 0;
	}
	else
	{
			

	}

}

int evaluate_expression(string k, int* bitmap, int length)
{
	int start_index = 0;
	int end_index = 0;
	long long sum = 0;
	int last_noted = 1;  //1 means +

	//printf("Revieved bitmap ");
	for(int i = 0; i < length; i++)
	{
		//printf("%d ",bitmap[i]);
	}
	//printf("\n");
	for(int i = 0; i < length; i++)
	{
		if(bitmap[i] != 0 )
		{
			end_index = i;
			long long value;


			value = atoll(k.substr(start_index,end_index-start_index+1).c_str());
			
			//printf("Evaluated %s answer is %lld, ",k.substr(start_index,end_index-start_index+1).c_str(),value);

			start_index = end_index + 1;
			if(last_noted == 1) { sum += value;}
			else if(last_noted == 0) { sum = sum - value; }
	
			if(bitmap[i] == 1) { last_noted = 1; }
			else { last_noted = 0;}
		}
	}

			end_index = length;
			long long value;
			value = atoll(k.substr(start_index,end_index-start_index+1).c_str());
			
			//printf("Evaluated %s answer is %lld\n ",k.substr(start_index,end_index-start_index+1).c_str(),value);
		//	start_index = end_index + 1;
			if(last_noted == 1) { sum += value;}
			else if(last_noted == 0) { sum = sum - value; }
	//		if(bitmap[i] == 1) { last_noted = 1; }
	//		else { last_noted = 0;}

		if(sum < 0 ) { sum = 0 -sum; }
		if(sum == 0) { return 1; }
		
		if(sum % 2 == 0) { return 1; }
		if(sum % 3 == 0) { return 1; }
		if(sum % 5 == 0) { return 1; }
		if(sum % 7 == 0) { return 1; }

		return 0;
	
}

int bitmap_increment(int* bitmap, int length)
{
	int i;
	int j;

	for(i=0;i < length; i++)
	{
		if(bitmap[i] == 0 ) { bitmap[i] = 1; return 1;}
		else if(bitmap[i] == 1) { bitmap[i] = 2; return 1;}

		bitmap[i] = 0;

	}
  return 0;
}


int main()
{
	int num_cases;
	int i;

	cin >> num_cases;

	for(i=0;i< num_cases;i++)
	{
		string s;
		cin >> s;
		int length = s.length() - 1;
		int* bitmap;
		long long num_uglies = 0;

		int j;

		bitmap = new int[length];

		for(j =0 ; j < length; j++)
		{
			bitmap[j] = 0;
		}

		do{
		
		num_uglies += evaluate_expression(s,bitmap,length);

		}while(bitmap_increment(bitmap,length) == 1);

		cout << "Case #"<<i+1<<": "<<num_uglies<<endl;

	}
}
