#include <iostream>
#include <fstream>
using namespace std;


// NOTE: all the input output is done in files. no output will be displayed on console.
void main()
{
	ofstream fout;
	ifstream fin;
	fin.open("input.in");
	fout.open("output.txt");
	
	char g_to_e[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int total_inputs;
	int max_size=110;

	//fout<<"Input\n";
	fin>>total_inputs;
	//fout<<total_inputs<<endl;
	
	
	char **google;  
	char **english;
	
	google = new char*[total_inputs];
	english = new char*[total_inputs];
	
	
	for(int i=0; i<total_inputs;i++)
	{
		google[i]=new char[max_size];
		english[i]=new char[max_size];
	}
	
	for(int j=0;j<total_inputs;j++)
	{
		google[j][0]='\0';
		english[j][0]='\0';
	}
	//cin.ignore();
	fin.ignore();
	for(int k=0;k<total_inputs; k++)
	{
		fin.getline(google[k],max_size,'\n');
		//if(google[k][0]=='\0')
		//fin.ignore();
		//fout<<google[k]<<endl;
	}
	//cout<<"\n\n\n\nOutput\n\n";
	
	for(int l=0; l<total_inputs; l++)
	{
		int size= strlen(google[l]);
		int temp,m;
		for( m=0; m<size; m++)
		{
			temp = (int)google[l][m]-97;
			if((int)google[l][m]==' ') // if space. put a space there.
			{
				english[l][m]=' ';
			}
			else
			{
				english[l][m]=g_to_e[temp];
			}
			
		}
		english[l][m]='\0';
	}
	for(int n=0;n<total_inputs; n++)
	{
		//cout<<"CASE#"<<n<<": "<<english[n]<<endl;
		fout<<"Case #"<<n+1<<": "<<english[n]<<endl;
	}
	system("pause");
	fout.close();
}	







