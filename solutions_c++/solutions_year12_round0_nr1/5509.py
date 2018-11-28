#include<iostream>
#include<fstream>

using namespace std;

int main()
{
	int translation[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int num_t;
	//cin>>num_t;
	//cin.ignore();
	ifstream myfile;
	myfile.open ("A-small-attempt1.in", ios::in);
	myfile>>num_t;
	myfile.ignore();
	char test[num_t][101];
	for(int t = 0; t<num_t; t++)
	{
		myfile.getline(test[t], 101);
	}
	myfile.close();
	ofstream myfileout;
	myfileout.open ("A-small-attempt1.out", ios::out);
	for(int t = 0; t<num_t; t++)
	{
		myfileout<<"Case #"<<t+1<<": ";
		for(int i=0; test[t][i]!='\0'; i++)
		{
			if(test[t][i]==' ') myfileout<<' ';
			else myfileout<<(char)translation[(int)test[t][i] - 97];
		}
		myfileout<<"\n";
	}
	return 0;
}
	