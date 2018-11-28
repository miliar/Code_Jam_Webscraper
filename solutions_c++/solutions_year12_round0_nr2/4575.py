#include<iostream>
#include<conio.h>
#include<string>
#include<xstring>
#include<fstream>
#include<sstream>
using namespace std;
void main()
{
	int n,c,i,item[100000];
	string string1;
	ifstream input("A.in");
	ofstream output("b.out");
	if(output == NULL)
	{
		cout<<"can not opent file"<<endl;
	}

	
	input >> n;
		
	getline(input,string1);
	int n1,s,p;
	for (int j = 0; j < n; j++)
	{
		cout<<endl;
		input >> n1;
     	input >> s;
		input >> p;
       // getline(input,string1);
		int count=0,temp=0;
		cout << "case #"<<j+1<<": ";
		output << "Case #"<<j+1<<": ";
		
		getline(input,string1);
		//cout<<string1;
		std::istringstream wordstream(string1);
		int word;
		int x=0;
		while(wordstream >> word)
		{
			item[x] = word;
			x++;
		}
	
		for(int k = 0; k < x; k++)
		{
				if ( item[k] >= p*3){
				count = count + 1;
			}
			else if (item[k] == 0)
			{
			}

			else if ( item[k] < p*3 && s == 0 ){
				if (  item[k] == (p-1)+(p)+(p-1) || item[k] == (p)+(p)+(p-1) || item[k] == (p)+(p)+(p+1) || item[k] == (p)+(p+1)+(p+1) ){
					count = count +1;
				}
			}
			else if ( item[k] < p*3 && s != 0 && temp != s){
				if ( item[k] == (p-1)+(p)+(p+1) || item[k] == (p-1)+(p)+(p-1) || item[k] == (p)+(p)+(p-1) || item[k] == (p)+(p)+(p+1) || item[k] == (p)+(p+1)+(p+1) ){
					count = count +1;
				}
				else if (item[k] == (p-1)+(p)+(p-2) || item[k] == (p+1)+(p)+(p+2) || item[k] == (p+2)+(p)+(p+2) || item[k] == (p-2)+(p)+(p-2) || item[k] == (p)+(p)+(p-2)){
				   temp = temp+1;
				   count = count +1;
				}
			}
		
		}

		output<<count;
		cout<<count;
	output<<endl;		
	}
	cout<<endl;
	cout<<endl;
	input.close();
	output.close();
	getch();

}

