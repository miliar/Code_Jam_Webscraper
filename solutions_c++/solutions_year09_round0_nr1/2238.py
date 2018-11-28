#include<iostream>
#include<map>
#include<string>
#include<fstream>
using namespace std;

map<string,int> mmp;
int L,D,N;

string str;
char words[15][26];
char length[15];
string mode[5500];

int search()
{
	bool flag=false;
	int count=0;
	for(int i=0;i<D;i++)
	{
		for(int j=0;j<L;j++)
		{
			flag=false;
			for(int k=0;k<length[j];k++)
			{
				if(words[j][k] == mode[i][j])
					flag = true;
			}
			if(flag==false)  break;
		}
		if(flag) count++;

	}

	return count;

}

int main()
{
	ifstream fcin("A-small.in");
	ofstream fcout("A-small");

	int i, j, k, cases;
	cases = 1;


	fcin>>L>>D>>N;
	string word;

	mmp.clear();
	for(i = 0 ;i<D; i++)
	{
		fcin>>word;
		mmp[word]=1;
		mode[i]=word;
	}

	string tmp = "";
	getline(fcin,str);
	for(cases = 1; cases<= N; cases++)
	{
		getline(fcin,str);

		for(i = 0,j=0;i<L; )
		{
			if(str[j]=='(')
			{
				j++;  k=0;
				while(str[j]!=')')
				{
					words[i][k]=str[j];
					j++;  k++;
				}
				length[i]=k;  j++;  i++;
			}
			else
			{
				words[i][0]=str[j];
				length[i]=1;  j++;  i++;
			}
		}


		fcout<<"Case #"<<cases<<": "<<search()<<endl;

	}
	return 0;
}