
#include <fstream>
#include <iostream>
#include <string>
using namespace std;

void cleanData(int data[500][3])
{
	for(int i=0;i<500;i++)
	{
		data[i][0] = 0;
		data[i][1] = 0;
		data[i][2] = 0;
	}
}
void tipareste(int s, int i, fstream &fout)
{
	int uc;
	uc = s % 10;
	if(i > 0) 
	{
		tipareste(s/10,i-1, fout);
	}
	fout << uc;
}
int main () {

	fstream fin, fout;
	int N;
	int data[500][3];
	string message;
	string welcome("welcome to code jam");
	string codificare("abcdefghijklmnopqrs");
	string small("welcom tdja");
	
	fin.open ("input.in", fstream::in );
	fout.open ("output.out", fstream::out);

	//rezolvare
	
	fin >> N; 
	getline (fin, message);
	
	for(int i=0;i<N;i++)
	{
		getline (fin, message);
		//remove unwanted letters from message
		int found;
		found=message.find_first_not_of(small);
		while (found != string::npos)
		{
			message.erase(found, 1);
			found = message.find_first_not_of(small, found);
		}
		//here I will have the clean text
		cleanData(data);
		int k;
		for(int j=0;j<message.size();j++)
		{
			switch(message[j])
			{
				//welcom tdja
				//"welcome to code jam"
				case 'w':
					data[j][0] = 1;
					data[j][1] = 0;
					data[j][2] = 0;
					break;					
				case 'e':
					for(k=0;k<j;k++)
					{
						if(message[k] == 'w')
							data[j][0] = (data[j][0] + data[k][0])%10000;
						if(message[k] == 'm')
							data[j][1] = (data[j][1] + data[k][0])%10000;
						if(message[k] == 'd')
							data[j][2] = (data[j][2] + data[k][0])%10000;
					}
					break;
				case 'l':
					for(k=0;k<j;k++)
					{
						if(message[k] == 'e')
							data[j][0] = (data[j][0] + data[k][0])%10000;
					}
					break;
				case 'c':
					for(k=0;k<j;k++)
					{
						if(message[k] == 'l')
							data[j][0] = (data[j][0] + data[k][0])%10000;
						if(message[k] == ' ')
							data[j][1] = (data[j][1] + data[k][1])%10000;
					}
					break;//"welcome to code jam"
				case 'o':
					for(k=0;k<j;k++)
					{
						if(message[k] == 'c')
							data[j][0] = (data[j][0] + data[k][0])%10000;
						if(message[k] == 't')
							data[j][1] = (data[j][1] + data[k][0])%10000;
						if(message[k] == 'c')
							data[j][2] = (data[j][2] + data[k][1])%10000;
					}
					break;
				case 'm':
					for(k=0;k<j;k++)
					{
						if(message[k] == 'o')
							data[j][0] = (data[j][0] + data[k][0])%10000;
						if(message[k] == 'a')
							data[j][1] = (data[j][1] + data[k][0])%10000;
					}
					break;//"welcome to code jam"
				case ' ':
					for(k=0;k<j;k++)
					{
						if(message[k] == 'e')
							data[j][0] = (data[j][0] + data[k][1])%10000;
						if(message[k] == 'o')
							data[j][1] = (data[j][1] + data[k][1])%10000;
						if(message[k] == 'e')
							data[j][2] = (data[j][2] + data[k][2])%10000;
					}
					break;//"welcome to code jam"
				case 't':
					for(k=0;k<j;k++)
					{
						if(message[k] == ' ')
							data[j][0] = (data[j][0] + data[k][0])%10000;
					}
					break;
				case 'd':
					for(k=0;k<j;k++)
					{
						if(message[k] == 'o')
							data[j][0] = (data[j][0] + data[k][2])%10000;
					}
					break;
				case 'j':
					for(k=0;k<j;k++)
					{
						if(message[k] == ' ')
							data[j][0] = (data[j][0] + data[k][2])%10000;
					}
					break;
				case 'a':
					for(k=0;k<j;k++)
					{
						if(message[k] == 'j')
							data[j][0] = (data[j][0] + data[k][0])%10000;
					}
					break;
			}
		}
		unsigned int sum = 0;
		for(int j=0;j<message.size();j++)
			if(message[j] == 'm')
				sum = (sum + data[j][1])%10000;
		fout << "Case #" << i+1 << ": ";
		tipareste(sum, 3, fout);
		
		fout << endl;
	}
	
	//end rezolvare
		
	fin.close();
	fout.close();
	cout << "Gata!!!";
	return 0;
}
