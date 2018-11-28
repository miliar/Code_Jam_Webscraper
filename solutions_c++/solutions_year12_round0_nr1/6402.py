#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main()
{
	char c;
	int num;
	string s;
	ifstream ins;
	ins.open("input.txt");

	ins>>num;
	while(num>=0)
	{
		//cout<<"!!!!!!";
			getline(ins,s);

				for(int i=0;i<s.length();i++)
				{
					//cout<<"111";
					c=s[i];
					if(c==' ')
					{
						cout<<' ';
					}
					if(c=='a')
							{
								cout<<'y';
							}
							if(c=='b')
									{
									cout<<'h';
									}
							if(c=='c')
									{
										cout<<'e';
									}
							if(c=='d')
									{
										cout<<'s';
									}
							if(c=='e')
									{
								cout<<'o';
									}
							if(c=='f')
									{
								cout<<'c';
									}
							if(c=='g')
									{
								cout<<'v';
									}
							if(c=='h')
									{
								cout<<'x';
									}
							if(c=='i')
									{
								cout<<'d';
									}
							if(c=='j')
									{
								cout<<'u';
									}
							if(c=='k')
									{
								cout<<'i';
									}
							if(c=='l')
									{
								cout<<'g';
									}
							if(c=='m')
									{
								cout<<'l';
									}
							if(c=='n')
									{
								cout<<'b';
									}
							if(c=='o')
									{
								cout<<'k';
									}
							if(c=='p')
									{
								cout<<'r';
									}
							if(c=='q')
									{
								cout<<'z';
									}
							if(c=='r')
									{
								cout<<'t';
									}
							if(c=='s')
									{
								cout<<'n';
									}
							if(c=='t')
									{
								cout<<'w';
									}
							if(c=='u')
									{
								cout<<'j';
									}
							if(c=='v')
									{
								cout<<'p';
									}
							if(c=='w')
									{
								cout<<'f';
									}
							if(c=='x')
									{
								cout<<'m';
									}
							if(c=='y')
									{
								cout<<'a';
									}
							if(c=='z')
									{
								cout<<'q';
									}
				}
				cout<<endl;

			num--;
		}
		ins.close();


	/*
	int num;
	ifstream ins;

		ins.open("sample.txt");
		if(ins.fail())
		{
			cerr<<"ERROR: Cannot open "<<filename<<endl;
			exit(-1);
		}

		while(!ins.eof())
		{
			ins>>num;
			ins>>areaWidth;

			for(int i=0;i<areaLength;i++)
			{
				altitudes[i]= new int[areaWidth];
				for(int j=0;j<areaWidth;j++)
				{
					ins>>altitudes[i][j];
				}
			}

		}
		ins.close();
		*/
}

