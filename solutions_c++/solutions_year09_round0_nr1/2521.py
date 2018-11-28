#include<iostream>
#include<fstream>
#include<set>
#include<vector>

using namespace std;


int main()
{
	ifstream fin

	("D:\\CodingForFun\\google code jam\\2009 1 Qualification\\files\\A2.in");
	ofstream fout
	("D:\\CodingForFun\\google code jam\\2009 1 Qualification\\files\\A2.out");


	vector<string> dict;

	int L, D, N;
	fin>>L>>D>>N;
	for(int i = 0; i < D; i++)
	{
		string str;
		fin>>str;
		dict.push_back(str);
	}

	for(int i = 0; i < N; i++)
	{
		cout<<"=====Case #"<< i+1 <<"====="<<endl;
		string str;
		fin>>str;

//		if(str.length() == L)
//		{
////			if(dict.find(str) != dict.end())
////			fout<<"Case #"<< i+1 <<": "<<1<<endl;
//			for(int k = 0; k < D; k++)
//			{
//				int l;
//				for(l = 0; l < L; l++)
//				{
//					if(str[l] != dict[k][l])break;
//				}
//				if(l == L-1)
//					fout<<"Case #"<< i+1 <<": "<<1<<endl;
//				break;
//			}
//		}
//
//		else
		{
			int count_t = 0;
			vector<string> letter;
			while(str.length()>0)
			{
				if(str[0] == '(')
				{
					int pos = str.find(')');
					letter.push_back(str.substr(1,pos-1));
					str = str.substr(pos+1, str.length()-pos-1);
				}
				else
				{
					letter.push_back(str.substr(0,1));
					str = str.substr(1, str.length()-1);
				}
				cout<<letter[letter.size()-1]<<endl;
				cout<<str<<endl;
			}
			for(int k = 0; k < D; k++)
			{
				for(int l = 0; l < L; l++)
				{
					if(letter[l].find(dict[k][l]) == string::npos)break;
					if(l == L-1)count_t++;
				}
			}
			fout<<"Case #"<< i+1 <<": "<<count_t<<endl;
		}
	}
}
