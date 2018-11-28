#include<iostream>
#include<stdlib.h>
#include<fstream>
#include<string>
#include<map>
#include<algorithm>
#include<list>
#include<math.h>
#include<vector>

using namespace std;


void sortstr(size_t n, std::string & num, bool flag)
{
	cout <<" sortstr:: received str "<<num;		
	std::vector<char> digits;
	int zero_count = 0;
	for(size_t i=n; i<num.length(); i++)
	{
		if((num[i]) == '0' && flag)
		{
			zero_count++;
			continue;
		}
		cout << "Adding to digits" <<num[i];	
		digits.push_back(num[i]);
	}
	cout<<"zero_count is"<<zero_count;		
	sort(digits.begin(),digits.end());

	if(flag)
	{
		size_t i = 0;
		if(digits.size() > 0)
			num[n+i] = digits[i];

		for(i=1; i<=zero_count; i++)
		{
			num[i+n] = '0';
		}
		for(size_t j =1; j<digits.size(); j++,i++)
		{
			num[n+i] = digits[j];
		}
	}
	else
	{
		for(size_t i=0; i<digits.size(); i++)
		{
			num[n+i] = digits[i];
			cout<<"num["<<i<<"] = "<<digits[i]<<"\n";
		}
	}
	
	cout<<" and returning string " << num<<"\n";
	return;
}
		
std::string swapmin(std::string num, int * index1, int * index2)
{
	cout<< "swapmin: receivde string " << num;
	size_t len = num.length();
	bool found = false;
	size_t n1, n2;
	for(size_t i = len-2; i>=0,len>=2; i--)
	{
		char min;
		for(size_t j = i+1; j<len; j++)
		{
			if((num.at(i) == '0') && j==0)
				break;
			cout<<"(i,j)=("<<i<<","<<j<<")"<<"\n";
			
			if((num.at(i) - '0') < (num.at(j) - '0'))
			{
				if(!found)
				{
					min = num.at(j);

					found = true;
					*index1 = i;
					n1 = i;
					n2 = j;
					*index2 = j;
				}
				else
				{
					if((num.at(j)-'0') < (min-'0'))
					{
						min = num.at(j);

						found = true;
						*index1 = i;
						n1 = i;
						n2 = j;
						*index2 = j;
					}
				}
			}
			if(j==0)
				break;
		}
		if(found == true)
			break;

		if(i==0)
			break;

	}
	if(found)
	{
		std::string newnum = num;
		newnum[n1] = num[n2];
		newnum[n2] = num[n1];
		if(n1 < len-1)
			sortstr(n1+1, newnum, false);
	
		cout<< "and returning string " << newnum << "\n";
		return newnum;
	}
	else
	{
		sortstr(0, num, true);
		int index=0;
		std::string temp = num.substr(0,1);
		temp += "0";
		temp += num.substr(1,num.length()-1);
		cout<< "and returning string " << temp << "\n";
		return temp;
	}
}

int main()
{
	ifstream infile("A-small.txt");
	//ifstream infile("A-small.txt");
	ofstream outfile("A-small-output.txt");
	
	if(!infile)
	{
		cout<<"Error opening inout file";
		return 1;
	}
	if(!outfile)
	{
		cout<<"Error opening output file";
		return 1;
	}
	int numTestCases, num;
	infile >> numTestCases;
	for(int i = 1; i<= numTestCases; i++)
	{
		//Input testcase
		infile >> num;
		char buf[1000000]; buf[0]='\0';
		sprintf(buf,"%d",num);
		std::string n = std::string(buf);

		//Process
		int index1, index2;
		std::string res = swapmin(n, &index1, &index2);

		//Output result
		
		outfile << "Case #"<< i <<": "<< res << "\n";
	}

}
