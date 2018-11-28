#include<iostream>
#include <string>
#include<fstream>
#include<ostream>
using namespace std;
#define InputOutputToFile

int main(void)
{
#ifdef InputOutputToFile
	
	//cin redirection
	std::ifstream fin("cin.txt");
	std::streambuf *inbuf = std::cin.rdbuf(fin.rdbuf());

	//cout redirection
	std::streambuf* cout_sbuf = std::cout.rdbuf(); // save original sbuf 
	std::ofstream   fout("cout.txt"); 
	std::cout.rdbuf(fout.rdbuf()); // redirect 'cout' to a 'fout' 
	//std::cout.rdbuf(cout_sbuf); // restore the original stream buffer 
#endif
	int run = 0;
	cin>>run;
	fflush(stdin);
	string input;
	getline(cin,input);
	int cs = 1;
	bool flag = false;

	while(run--)
	{
		//string input="ejp mysljylc kd kxveddknmc re jsicpdrysi";
		if(flag)
			cout<<endl;
		flag = true;
		//cin>>input;
		input.clear();
		getline(cin,input);
		char ch;
		int j=0;
		
		
		char a[26]={'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};
		for(int i=0; i < (int)input.length() ; i++)
		{	
			if(input[i]==' ')
				continue;
			else
			{
				ch=input[i];			
				for(j=0;j<26;j++)
				{
					if(ch == a[j])
						break;
				}			
				input[i]=(char)j+97;
			}
		}
		cout<<"Case #"<<cs<<": "<<input;
		cs++;
	}
	return 0;
}