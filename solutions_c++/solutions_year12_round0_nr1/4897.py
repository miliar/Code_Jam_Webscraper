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
    char z [26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    char s[101] ;

    vector<char> M;
	ifstream ipfile;
	ipfile.open("A-small-attempt1.in",ios::in);
	ofstream outfile;
	outfile.open("small.out",ios::out);
	if(ipfile.is_open())
	{
		while(ipfile.good())
		{

					ipfile.getline(s,101);
					int n;
					char * pEnd;
					n= strtol (s,&pEnd,10);
					for(int i=0;i<n;i++)
					{
					    M.erase(M.begin(),M.end());
						ipfile.getline(s,101);
                        for(int j =0;j<strlen(s);j++)
                        {
                            if(((int)s[j]-97)>=0)
                                M.push_back(z[(s[j]-97)]);
                              else
                                M.push_back(' ');
                        }
                        outfile << "Case #"<<i+1<<": ";
                        outfile.write ((const char*)&M[0],M.size());
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
