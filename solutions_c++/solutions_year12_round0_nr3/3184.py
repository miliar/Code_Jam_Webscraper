#include<iostream>
#include<map>
#include<string>
#include<iostream>
#include<fstream>
#include <iostream>
#include <stdio.h>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int rever1(int n)
{
	char str1[5],temp;
	string str2;
	itoa(n,str1,10);
	//cout<<str1<<endl;
	str2.push_back(str1[1]);
	str2.push_back(str1[0]);
	return atoi(str2.c_str());
}

int rever2(int n)
{
	char str1[5],temp;
	string str2;
	itoa(n,str1,10);
	//cout<<str1<<endl;
	str2.push_back(str1[1]);
	str2.push_back(str1[2]);
	str2.push_back(str1[0]);
	return atoi(str2.c_str());
}

int rever3(int n)
{
	char str1[5],temp;
	string str2;
	itoa(n,str1,10);
	//cout<<str1<<endl;
	str2.push_back(str1[2]);
	str2.push_back(str1[0]);
	str2.push_back(str1[1]);
	return atoi(str2.c_str());
}


int main()
{
	ifstream file1("C-small-attempt0.in");
    ofstream file2("C-small-attempt0.out");
	int T;
    file1>>T;

	for (int k=1;k<=T;k++)
	{
		
		int n1,n2;
		file1>>n1>>n2;
		int count=0;
		int count1=0;
		if(n2<10)	
		file2<<"Case"<<" "<<"#"<<k<<":"<<" "<<count/2<<endl;
		else if (n2>=10 && n2<100)
				{
					for(int n=n1;n<=n2;n++)
					{
						if(rever1(n)>=n1 && rever1(n)<=n2 && n!=rever1(n))
						{count++;}
					}
				file2<<"Case"<<" "<<"#"<<k<<":"<<" "<<count/2<<endl;
				}
		else if(n2>=100&& n2<=1000)
			 {
				 for(int n=n1;n<=n2;n++)
					{
						if(rever2(n)>=n1 && rever2(n)<=n2 && n!=rever2(n))
						{count1++;}	
						if(rever3(n)>=n1 && rever3(n)<=n2 && n!=rever3(n))
						{count1++;}
					}
				file2<<"Case"<<" "<<"#"<<k<<":"<<" "<<count1/2<<endl;
			}
	}
	
	file1.close();
    file2.close();

	return 0;
}