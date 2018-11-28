#include <fstream>
#include <iostream>
#include <list>
#include <stack>
using namespace std;

int a;
int b;

//int c;

bool isFound(list<int> keyList, int a)
{
	list<int>::iterator it;
	
	for(it = keyList.begin(); it != keyList.end(); ++it)
		{
			if(*it == a)
				return true;
		}
	return false;
}

int hash(int input, int digits)
{	
	list<int> partners;
	stack<int> head, tail;
	int temp;

	for(int i = 0; i < digits; i++)
	{
		temp = input;
		for(int j = 0; j < digits; j++)
		{
			if(j < i)
			{
				tail.push(temp % 10);
				temp /= 10;
			}
			else
			{
				head.push(temp % 10);
				temp /= 10;
			}
		}
		temp = 0;
		while(!tail.empty())
		{
			temp += tail.top();
			tail.pop();
			temp *= 10;
		}
		while(!head.empty())
		{
			temp += head.top();
			head.pop();
			temp *= 10;
		}
		temp /= 10;

		if((temp >= a) && (temp <= b))
			if(!isFound(partners, temp))
				partners.push_back(temp);
	}

	partners.sort();

	return partners.front();
}

int findNoPairs(int input, int digits)
{
	stack<int> head, tail;
	list<int> partners;
	int temp;
	int result = 0;

	for(int i = 0; i < digits; i++)
	{
		temp = input;
		for(int j = 0; j < digits; j++)
		{
			if(j < i)
			{
				tail.push(temp % 10);
				temp /= 10;
			}
			else
			{
				head.push(temp % 10);
				temp /= 10;
			}
		}
		temp = 0;
		while(!tail.empty())
		{
			temp += tail.top();
			tail.pop();
			temp *= 10;
		}
		while(!head.empty())
		{
			temp += head.top();
			head.pop();
			temp *= 10;
		}
		temp /= 10;

		if((temp >= a) && (temp <= b))
			if(!isFound(partners, temp))
				partners.push_back(temp);
	}

	temp = partners.size();
	result = (temp * (temp - 1)) / 2;
	return result;
}

int main(){
	ifstream fin("C:\\Users\\ting\\Documents\\Visual Studio 2008\\Projects\\Google2012\\Debug\\file.in");
	ofstream fout("C:\\Users\\ting\\Documents\\Visual Studio 2008\\Projects\\Google2012\\Debug\\file.out");

	int cases;
	int counter = 1;

	fin >> cases;
	
	while(counter <= cases){
		int answer = 0;
		int digits = 0;
		list<int> keyList;

		fin >> a;
		fin >> b;
//		cin >> c;

		int temp = a;
		while(temp > 0)
		{
			temp /= 10;
			digits++;
		}

		//#################### START ######################
		int aCounter = a;
		while(aCounter <= b)
		{
			temp = hash(aCounter, digits);
			if(!isFound(keyList, temp))
			{			
				keyList.push_back(temp);
				answer += findNoPairs(aCounter, digits);
			}
			aCounter++;
		}

		fout << "Case #" << counter << ": " << answer << endl;
		counter++;
	}

	return 0;
}