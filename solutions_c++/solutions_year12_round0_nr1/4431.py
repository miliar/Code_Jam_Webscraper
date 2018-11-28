#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>

using namespace std;

main()
	{
	ifstream fin1;
	ofstream fout("output.in");
	int x;
	fin1.open("A-small-attempt1.in");
	fin1>>x;
	string str;
	getline(fin1,str);
	for (int i=1;i<=x;++i)
		{
		getline(fin1,str);
		int j=0;
		while(str[j])
			{
			switch (str[j])
				{
				case 'a' : str[j]='y';
					break;
				case 'b' : str[j]='h';
					break;
				case 'c' : str[j]='e';
					break;
				case 'd' : str[j]='s';
					break;
				case 'e' : str[j]='o';
					break;
				case 'f' : str[j]='c';
					break;
				case 'g' : str[j]='v';
					break;
				case 'h' : str[j]='x';
					break;
				case 'i' : str[j]='d';
					break;
				case 'j' : str[j]='u';
					break;
				case 'k' : str[j]='i';
					break;
				case 'l' : str[j]='g';
					break;
				case 'm' : str[j]='l';
					break;
				case 'n' : str[j]='b';
					break;
				case 'o' : str[j]='k';
					break;
				case 'p' : str[j]='r';
					break;
				case 'q' : str[j]='z';
					break;
				case 'r' : str[j]='t';
					break;
				case 's' : str[j]='n';
					break;
				case 't' : str[j]='w';
					break;
				case 'u' : str[j]='j';
					break;
				case 'v' : str[j]='p';
					break;
				case 'w' : str[j]='f';
					break;
				case 'x' : str[j]='m';
					break;
				case 'y' : str[j]='a';
					break;
				case 'z' : str[j]='q';
				}
			j++;
			}
		fout<<"Case #"<<i<<": "<<str<<"\n";
		}
	fin1.close();
	fout.close();
	return 0;
	}
