#include <iostream>
#include <string>
#include <fstream>
#include <math.h>
using namespace std;

void main()
{
string line;
long t = 0, n = 0, k = 0, i, counter;

ifstream fin("a.in");									//open specified file for reading

if (!fin) {}											//{cout << "Cannot open file: b.in\n"; }	//report error if file not exist
	else {	
			
			ofstream fout("a.out");							//clear contents of output file before writing
			fout.close();

			char cases[6], snippers[3], finger[10];

			fin.getline(cases,6);
			for(i=0;i<6;i++)
			{
				if (cases[i]!=0)
				{
					t = t*10+((int)cases[i]-48);
				}
				else
				{
					break;
				}
			}

			for(counter=1;counter<t+1;counter++)
			{
				fin.get(snippers,3,(char)" ");
				for(i=0;i<3;i++)
				{
					if (snippers[i]==0 || snippers[i]==32)
					{
						break;
					}
					else
					{
						n = n*10+((int)snippers[i]-48);
					}
				
				}

				fin.getline(finger,10);
				if (finger[0]==0 || finger[0]==32)
				{
					i=1;
				}
				else
				{
					i=0;
				}
				for(i;i<10;i++)
				{
					if (finger[i]==0 || finger[i]==32)
					{
						break;
					}
					else
					{
						k = k*10+((int)finger[i]-48);
					}
				}


				i=long(pow((double)2,(int)n));

				ofstream fout("a.out",ios_base::app);
				cout << "Case #" << counter << ": ";
				fout << "Case #" << counter << ": ";

				if (((k+1)-(int)((k+1)/i)*i) == 0)
				{	cout << "ON\n";
					fout << "ON\n";
				}
				else
				{	cout << "OFF\n";
					fout << "OFF\n";
				}
				fout.close();

				n=0;
				k=0;
			}
	}
fin.close();
}
