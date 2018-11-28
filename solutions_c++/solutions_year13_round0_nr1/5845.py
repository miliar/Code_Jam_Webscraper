#include<iostream>
#include<cmath>
#include <cstdlib>
#include<fstream>
#include <cstring>
#include<string>
#include<algorithm>
using namespace std;
using std::ifstream;
using std::ofstream;

char a[4][4]={'.'};

bool diagonal(char o){
	bool ans=false;
	int T=0;
	if (a[0][0]==o || a[0][0]=='T')
	{
		if(a[0][0]=='T')
			T++;
		if(a[1][1]==o || (a[1][1]=='T' && T<1))
		{
			if(a[1][1]=='T')
				T++;
			if(a[2][2]==o || (a[2][2]=='T' && T<1))
			{
				if(a[2][2]=='T')
					T++;
				if (a[3][3]==o || (a[3][3]=='T' && T<1))
					return true;
			}

		}
	}

	if (a[3][0]==o || a[3][0]=='T')
	{
		if(a[3][0]=='T')
			T++;
		if(a[2][1]==o || (a[2][1]=='T' && T<1))
		{
			if(a[2][1]=='T')
				T++;
			if(a[1][2]==o || (a[1][2]=='T' && T<1))
			{
				if(a[1][2]=='T')
					T++;
				if (a[0][3]==o || (a[0][3]=='T' && T<1))
					return true;
			}

		}
	}

	return false;

}

bool column(char o){
	bool ans=false;
	int T=0;
	for(int i=0;i<4;i++)
		if (a[0][i]==o || a[0][i]=='T')
		{
			if(a[0][i]=='T')
				T++;
			if(a[1][i]==o || (a[1][i]=='T' && T<1))
			{
				if(a[1][i]=='T')
					T++;
				if(a[2][i]==o || (a[2][i]=='T' && T<1))
				{
					if(a[2][i]=='T')
						T++;
					if (a[3][i]==o || (a[3][i]=='T' && T<1))
						return true;
				}

			}
		}
		return false;	
}

bool row(char o){
	bool ans=false;
	int T=0;
	for(int i=0;i<4;i++)
		if (a[i][0]==o || a[i][0]=='T')
		{
			if(a[i][0]=='T')
				T++;
			if(a[i][1]==o || (a[i][1]=='T' && T<1))
			{
				if(a[i][1]=='T')
					T++;
				if(a[i][2]==o || (a[i][2]=='T' && T<1))
				{
					if(a[i][2]=='T')
						T++;
					if (a[i][3]==o || (a[i][3]=='T' && T<1))
						return true;
				}

			}
		}
		return false;	
}



int main()
{
	ofstream out;
//	out.open("output.txt");
	int T, empty;
	char s;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		empty=1;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>a[i][j];
				if(a[i][j]=='.')
					empty=0;
			}
		}

		cout<<"Case #"<<t<<": ";
	//	out<<"Case #"<<t<<": ";
		if(row('O') || column('O') || diagonal('O'))
		{
			cout<<"O won\n";
		//	out<<"O won\n";
		}
		else if(row('X') || column('X') || diagonal('X'))
		{
			cout<<"X won\n";
		//	out<<"X won\n";
		}
		else if(empty==0)
		{
			cout<<"Game has not completed\n";
		//	out<<"Game has not completed\n";
		}
		else 
		{
			cout<<"Draw\n";
		//	out<<"Draw\n";
		}
	}

	//out.close();

	return(0);
}