#include<iostream>
#include<fstream>
#include<string>
#include <sstream>
using namespace std;
bool check(int value,int p,int& s)
{
	bool stop;

	for(int i=p;i<=10;i++)
		if((value-i)<=20)
		{
			for(int l=i-1;l<=i;l++)
				for(int j=i-1;j<=i;j++)
					if((l+j+i)== value && l>=0 && j>=0)
						return true;
			if(s)
				for(int l=i-2;l<=i;l++)
					for(int j=i-2;j<=i;j++)
						if((l+j+i)== value && l>=0 && j>=0)
						{
							s--;
							return true;
						}
		}
	return false;
}
int main()
{
	ifstream file("B-large.in",ios::in);
	ofstream fichier("B-large.out", ios::out | ios::trunc);
	string line;
	int t,nbr,n,s,p,value;

	getline(file,line);
	istringstream iss (line,istringstream::in);
	iss>>t;
	for(int c=0;c<t;c++)
	{
		nbr=0;
		getline(file,line);
		istringstream iss (line,istringstream::in);
		iss>>n;
		iss>>s;
		iss>>p;
		for(int i=0;i<n;i++)
		{
			iss>>value;
			if(check(value,p,s))
				nbr++;
		}
		fichier<<"Case #"<<c+1<<": "<<nbr<<endl;
	}
	return 0;
}
