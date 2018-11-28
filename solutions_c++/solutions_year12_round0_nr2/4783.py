#include <iostream>
#include <fstream>
#include <string>
#include<string.h>
#include <stdio.h>
#include <stdlib.h>
#include<vector>
using namespace std;

int main()
{
    char s[600] ;
    int a,b,c;
    int t ;
    int m;
    int N ;
    int S;
    int P;
    int Scount;
    int max;
    vector<char> M;
	ifstream ipfile;
	ipfile.open("B-large.in",ios::in);
	ofstream outfile;
	outfile.open("O.out",ios::out);
	if(ipfile.is_open())
	{
		while(ipfile.good())
		{

					ipfile.getline(s,600);
					int n;
					char * pEnd;
					n= strtol (s,&pEnd,10);
					for(int i=0;i<n;i++)
					{
					    max=0;
					    Scount=0;
						ipfile.getline(s,600);
						char * pch;
						pch = strtok (s," ,.-");
						N= strtol (pch,&pEnd,10);
						pch = strtok (NULL," ,.-");
						S= strtol (pch,&pEnd,10);
						pch = strtok (NULL," ,.-");
						P= strtol (pch,&pEnd,10);
                        for(int j =0;j<N;j++)
                        {
                            pch = strtok (NULL," ,.-");
                            t= strtol (pch,&pEnd,10);
                            if(t==0)
                            {
                                if(P==0)
                                    {
                                        max++;
                                        continue;
                                    }
                                continue;

                            }
                            a=b=c=(t/3);
                            m=t%3;
                            switch(m)
                            {
                                case 0:
                                    if((a>=P))
                                    {
                                        max++;
                                        break;
                                    }
                                    a++;
                                    if(a>10)
                                        {break;}
                                    b--;
                                    if((a>=P))
                                    {
                                        max++;
                                        Scount++;
                                    }
                                    break;
                                case 1:
                                    a++;
                                    if((a>=P))
                                    {
                                        max++;
                                        break;
                                    }
                                    break;
                                case 2:
                                    a++;
                                    b++;
                                    if((a>=P))
                                    {
                                        max++;
                                        break;
                                    }
                                    a++;
                                    if(a>10)
                                        {break;}
                                    b--;
                                    if((a>=P))
                                    {
                                        max++;
                                        Scount++;
                                    }
                                    break;
                            }

                        }
                        if((Scount>S)&&(max!=0))
                            max=max-Scount+S;
                        outfile << "Case #"<<i+1<<": ";
                        outfile <<max;
                        outfile << "\n";
                        //for(int j =0;j<M.size();j++)
                          //  {cout<<M[j];}
                        //cout<<endl;
                        //cout<<M.size()<<endl;
                    }
		}
		ipfile.close();
        outfile.close();
	}
    return 0;
}
