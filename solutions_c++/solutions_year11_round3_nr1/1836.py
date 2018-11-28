#include <iostream>
#include <fstream>

//#define size_r 6;
//#define size_co 6;

using namespace std;

int main(void)
{
	int test_cases, r, c, count, check;
	char arr[50][50];
	ifstream in("inp.txt", ios::in);
	ofstream out("out.txt", ios::out);
	in>>test_cases;
	for(int i=1; i<=test_cases; ++i)
	{
		count =0;
		check=1;
		in>>r>>c;
		for(int j=0; j<r; ++j)
		{
			for(int k=0; k<c; ++k)
			{
				in>>arr[j][k];
				if(arr[j][k]=='#')
				{++count;}
			}
		}
		if(count%4==0)
		{
			//cout<<"executed\n" && cout<<"in here"<<endl;
			for(int j=0; j<r; ++j)
			{
				for(int k=0; k<c; ++k)
				{
					//cout<<"j is: "<<j<<"k is: "<<k<<endl;
					if(arr[j][k]=='.')
					{continue;}
					else if(arr[j][k]=='#' )
					{
						//cout<<"first level\t";
						if(k+1 < c && arr[j][k+1]=='#')
						{
						//	cout<<"second level\t";
							if(j+1 < r && arr[j+1][k]=='#')
							{
					//			cout<<"third level\t";
								if(arr[j+1][k+1]=='#')
								{
									///cout<<"fourth level"<<endl;
									arr[j][k]=47;
									arr[j][k+1]=92;
									arr[j+1][k]=92;
									arr[j+1][k+1]=47;
									++k;	//incrementing k
								}
								else
								{check=-1;}
							}
							else
							{check=-1;}
						}
						else
						{check=-1;}
					}
					else if(arr[j][k]==92 && arr[j][k+1]==47)
					{++k;}
					else
					{check = -1;}
					if(check==-1)
					{break;}
					//cout<<endl;
				}
				if(check==-1)
				{break;}
			}
		}
		else
		{check=-1;}
		if(check==1)
		{
			out<<"Case #"<<i<<":\n";
			for(int j=0; j<r; ++j)
			{
				for(int k=0; k<c; ++k)
				{out<<arr[j][k];}
				out<<"\n";
			}
		}
		else
		{out<<"Case #"<<i<<":\nImpossible\n";}
		
	}
	return 0;
}
