#include<iostream>
#include<map>
#include<string>
#include<iostream>
#include<fstream>
#include <iostream>
#include <stdio.h>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <vector>

using namespace std;


int main()
{
    ifstream file1("B-large.in");
    ofstream file2("B-large.out");
    int T;
    file1>>T;
	vector<int> V;

    for (int k=1;k<=T;k++)
    {
       
        int n,s,p;
        file1>>n>>s>>p;
		V.clear();
		for(int i=0;i<n;i++)
		{
			
			int n1;
			file1>>n1;
			V.push_back(n1);
		}
		int count=0;
		for(int i=0;i<n;i++)
		{
			if(V.at(i)>=2)
				{
					if(V.at(i)>=3*p-2)
					{
					count++;
					}
					else if (V.at(i)+2>=3*p-2 && s>0)
					{
					s--;
					count++;
					}
				}
			else
				if(V.at(i)>=p)
				{count++;}
		}
			file2<<"Case"<<" "<<"#"<<k<<":"<<" "<<count<<endl;
	}  



    file1.close();
    file2.close();

    return 0;
}