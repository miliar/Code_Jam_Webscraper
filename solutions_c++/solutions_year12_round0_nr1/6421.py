#include <iostream>
#include <fstream>
using namespace std;
void process(int map[],char input[])
{
	int i=0;
	for( i=0;input[i]!='\0';i++)
	{
		if(input[i]==' ')
			;
		else
		input[i]=map[input[i]];
	}
}
int main()
{
	int i;
	char input[102];
	int n=0;
	ifstream ifile("map.txt");
	int map[200];
	for( i=97;i<97+26;i++)
	{
		ifile>>map[i];
	}
	cin>>n;
		cin.ignore();
	for(i=0;i<n;i++)
	{
		cin.getline(input,102);
		process(map,input);
		cout<<"Case #"<<i+1<<": "<<input<<endl;
	}
}
