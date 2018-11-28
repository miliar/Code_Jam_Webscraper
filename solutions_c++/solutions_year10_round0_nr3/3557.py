#include <iostream>
#include <string>
#include <fstream>
using namespace std;

void main()
{
string line;
long t = 0, r = 0, k = 0, n = 0, g[1001]={0}, i, j, p, q, counter=0;
long long earnings;

ifstream fin("c-small.in");									//open specified file for reading

if (!fin) {}											//{cout << "Cannot open file: b.in\n"; }	//report error if file not exist
	else {	
			
			ofstream fout("c-small.out");							//clear contents of output file before writing
			fout.close();

			char data[8000];

			fin.getline(data,3);
			for(i=0;i<3;i++)
			{
				if (data[i]!=0)
				{
					t = t*10+((int)data[i]-48);
				}
				else
				{
					break;
				}
			}

			for(counter=1;counter<t+1;counter++)
			{
				fin.getline(data,(char)" ");

					for(i=0;i<9;i++)
					{
						if (data[i]==0 || data[i]==32)
						{
							break;
						}
						else
						{
							r = r*10+((int)data[i]-48);
						}
					}


					j=i;
					for(i=i+1;j<11;i++)
					{
						if (data[i]==0 || data[i]==32)
						{
							break;
						}
						else
						{
							k = k*10+((int)data[i]-48);
						}
					}

					j=i;
					for(i=i+1;i<j+6;i++)
					{
						if (data[i]==0 || data[i]==32)
						{
							break;
						}
						else
						{
							n = n*10+((int)data[i]-48);
						}
					}
					
					fin.getline(data,(char)" ");
					p=0;
					j=0;

					for(i=0;i<n*8;i++)
					{
						if (data[i]==0)
						{
							break;
						}
						else
						{
							if (data[i]!=32)
							{
								g[j] = g[j]*10+((int)data[i]-48);
							}
							else
							{
								j++;
							}
						}
					}

					earnings=0;
					p=0;
					for(i=0;i<r;i++)
					{
						j=0;
						q=p;
						while(g[p] + j <= k)
						{
							j = j + g[p];
							p++;
							if (p==n)
							{
								p=0;
								if(p==q)
								{
									break;
								}
							}
						}
						earnings = earnings + j;
					}

					ofstream fout("c-small.out",ios_base::app);
					cout << "Case #" << counter << ": " << earnings << endl;
					fout << "Case #" << counter << ": " << earnings << endl;
					fout.close();

					for(i=0;i<8000;i++)
					{
						data[i]=0;
					}

					for(i=0;i<1001;i++)
					{
						g[i]=0;
					}
					r=0;
					k=0;
					n=0;
			}
	}
fin.close();
}
