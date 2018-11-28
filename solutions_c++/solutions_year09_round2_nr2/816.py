#include <cstdlib>
#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[])
{
	fstream fin;
	fstream fout;
	fin.open("b.in");
	fout.open("b.out", ios_base::app);
	//
    int t,n;
	fin >> t;
    //fin >> n;


    for(int i=0; i<t; i++)
    {
		string a;
		fin >> a;
		//fout 
		bool is=next_permutation (a.begin(),a.end());
		if(is)
			fout << "Case #" << i+1 << ": " << a << endl;
		else
		{
			int j=0;
			while(a[j]=='0')
			{
				j++;
			}
			string b;
			b+=a[j];
			int k=0;
			j++;
			while(k<j)
			{
				b+='0';
				k++;
			}
			while(j<a.length())
			{
				b+=a[j];
				j++;
			}
			fout << "Case #" << i+1 << ": " << b << endl;
		}
    }
	//
    fin.close();
	fout.close();
    return 0;
}
