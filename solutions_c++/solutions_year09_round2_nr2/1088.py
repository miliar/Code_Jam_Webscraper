/* Google Code Jam 2009
   Round 1B

   Problem: B

   author: David Volgyes

 */

#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;



std::vector<char> nextNumber(string number)
{
	std::vector<char> digits;
	std::vector<char> numberVector;
	string result;
	for(int i=0;i<strlen(number.c_str());i++) numberVector.push_back(number[i]);

	for(int j=1;j<10;j++)
		for (int i=0;i<strlen(number.c_str());i++)
		{
			if (number[i]==(unsigned char)(j+(int)'0')) digits.push_back(number[i]);
		}

	for (int i=strlen(number.c_str())-1;i>0;i--)
	{
		if (number[i]<=number[i-1]) continue;
		{char temp=numberVector[i-1];numberVector[i-1]=numberVector[i];numberVector[i]=temp;}
		for(int k=i;k<strlen(number.c_str());k++)
		{
			if ((numberVector[i-1]>number[k]) && number[k]>number[i-1])
			{
				char temp;
				temp=numberVector[i-1];numberVector[i-1]=numberVector[k];numberVector[k]=temp;
			}

		}

		for(int k=i;k<strlen(number.c_str());k++)
			for(int l=k+1;l<strlen(number.c_str());l++)
				if ((numberVector[k]>numberVector[l]) && (k<l))
				{
					char temp;
					temp=numberVector[k];numberVector[k]=numberVector[l];numberVector[l]=temp;
				}
		return numberVector;
	}
	numberVector.push_back('0');
	for (int i=0;i<numberVector.size()-1;i++)
	{
		if (number[i]==digits[0]) {
			//pos=i;
			{char temp=numberVector[0];numberVector[0]=numberVector[i];numberVector[i]=temp;}
		}
	}

	for(int k=1;k<numberVector.size();k++)
		for(int l=k+1;l<numberVector.size();l++)
			if ((numberVector[k]>numberVector[l]) && (k<l))
			{
				char temp;
				temp=numberVector[k];numberVector[k]=numberVector[l];numberVector[l]=temp;
			}

	return numberVector;
}

int main() {
	int numberOfTestCases;
	int i=0;
	string text,number;
	getline(std::cin,text);
	numberOfTestCases=atoi(text.c_str());
	std::vector<char> result;
	// Main loop
	do{
		getline(std::cin,number);
		i=i+1;
		result=nextNumber(number);
		printf("Case #%i: ",i);
		for(int i=0;i<result.size();i++) printf("%c",result[i]);
		printf("\n");
	}
	while(i<numberOfTestCases);
	return 0;
}
