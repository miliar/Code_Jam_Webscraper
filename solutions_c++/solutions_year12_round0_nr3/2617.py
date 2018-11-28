// GoogleJam1.cpp : Defines the entry point for the console application.
//
/*
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;
void main()
{
	char temp1[1024];
	char* token;
	fstream input,output;
	input.open("D://1.txt");
	input.getline(temp1,1024);
	output.open("D://2.txt");
	int count=atoi(temp1),Case=1;
	while(count--)
	{
		int q[288],w[288],e=0;
		input.getline(temp1,1024);
		int A=atoi(strtok(temp1," "));		
		int B=atoi(strtok(NULL," "));
		int max=0;
		int ea=0;
		for(int i=A;i<=B;i++)
		{
			int index[1000],k=0;
			string number;
			stringstream ss;
			ss<<i;
			ss>>number;	
			for(int j=0;j<number.length()-1;j++)
			{
				string back(number.begin(),number.begin()+j+1);
				string front(number.begin()+j+1,number.end());
				string NEW=front;
				NEW.append(back);
				int num=atoi(NEW.c_str());
				if(A<=num &&num<=B && num!=i && num>i) 
				{
					int pass=1;
					for(int l=0;l<k;l++)
					{
						if(index[l]==num) pass=0;
					}
					if(pass==1)
					index[k++]=num;
					max++;
				}
			}
		}
		output<<"Case #"<<Case++<<": "<<max<<endl;
	}
	output.close();
}
*/

	// GoogleJam1.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;
void main()
{
	char temp1[1024];
	char* token;
	fstream input,output;
	input.open("D://1.txt");
	input.getline(temp1,1024);
	output.open("D://2.txt");
	int count=atoi(temp1),Case=1;
	while(count--)
	{
		int q[288],w[288],e=0;
		input.getline(temp1,1024);
		int A=atoi(strtok(temp1," "));		
		int B=atoi(strtok(NULL," "));
		int max=0;
		int ea=A+1+(B-A)/2;
		for(int i=A;i<=B;i++)
		{
			int index[1000],k=0;
			char number[10];
			itoa(i,number,10);
			for(int j=0;j<strlen(number)-1;j++)
			{
				char number1[10];
				strncpy(number1,number+j+1,strlen(number)-(j+1));
				strncpy(number1+strlen(number)-(j+1),number,j+1);
				number1[strlen(number)]=0;
				int num=atoi(number1);
				if(A<=num &&num<=B && num!=i && num>i) 
				{
					int pass=1;
					for(int l=0;l<k;l++)
					{
						if(index[l]==num) pass=0;
					}
					if(pass==1)
					{
						index[k++]=num;
						max++;
					}
				}
			}
		}
		output<<"Case #"<<Case++<<": "<<max<<endl;
	}
	output.close();
}

/*
		for(int i=0;i<ea;i++)
		{
			for(int j=i+1;j<ea;j++)
			{
				if(q[i]==w[j] && q[j]==w[i])
				{
					cout<<q[i]<<" "<<w[i]<<" "<<i<<endl;
					cout<<q[j]<<" "<<w[j]<<" "<<j<<endl;
				}

			}
				if(q[i]==w[i])
				{
					cout<<q[i]<<" "<<w[i]<<" "<<i<<endl;
				}

		}
*/
