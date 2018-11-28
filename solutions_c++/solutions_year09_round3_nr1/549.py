#include <iostream>
#include <fstream>
#include <string>
#include <vector>


using namespace std;

int main()
{
    ifstream fin("c:\\input.txt");
    ofstream fout("c:\\output.txt");
	int cases;
	fin>>cases;
	int numn = 1;
	while(cases--)
	{
		int used[36];
		for(int i = 0; i < 36; i++)
		{
			used[i] = 0;
		}
		string mystr;
		fin>>mystr;
		for(int i = 0; i < (int)mystr.size(); i++)
		{
			if(mystr[i]>= '0' && mystr[i] <= '9')
			{
				used[mystr[i]-'0'] = 1;
			}
			else
			{
				used[mystr[i]-'a'+10] = 1;
			}
		}
		vector <int> number;
		number.resize((int)mystr.size());
		for(int i = 0 ; i < (int)number.size(); i++)
		{
			number[i] = -1;
		}
		int numchar = 0;
		for(int i = 0; i < 36; i++)
		{
			if(used[i] == 1)
				numchar++;
		}
		
		vector <int>charused;
		charused.resize(numchar);

		int nownum = 2;
		number[0] = 1;
		for(int i = 1; i < (int)mystr.size(); i++)
		{
			if(mystr[0] == mystr[i])
			{
				number[i] = 1;
			}
		}
		if(numchar != 1)
		{
		int i = 0;
		
		while(number[i] != -1 && (int)mystr.size() > i)
		{
			i++;
		}
		for(int j = i; j < (int)mystr.size(); j++)
		{
			if(mystr[i] == mystr[j])
			{
				number[j] = 0;
			}
		}
		while(numchar > nownum)
		{
			while(number[i] != -1 && (int)mystr.size() > i)
			{
				i++;
			}
			for(int j = i; j < (int)mystr.size(); j++)
			{
				if(mystr[i] == mystr[j])
				{
					number[j] = nownum;
				}
			}
			nownum++;
		}}
		else
			numchar = 2;
		unsigned long long int ans = 0;
		unsigned long long int nowm = 1;
		for(int i = (int)number.size()-1; i >=0; i--)
		{
			ans += number[i] * nowm;
			nowm *=numchar;
		}
		fout<<"Case #"<<numn++<<": "<<ans<<endl;






	}
	fin.close();
    fout.close();
    return 0;
}