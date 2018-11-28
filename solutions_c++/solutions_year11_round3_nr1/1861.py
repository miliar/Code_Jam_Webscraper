#include<iostream>
#include<fstream>

using namespace std;
int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-output.in");
	
	int testcases;
	int row, col;
	char arr[50][50];
	bool impossible;
	fin>>testcases;
//	cout<<testcases<<endl;
	for(int z = 1; z <= testcases; z++)
	{
		impossible = false;
		fin>>row>>col;
	//	cout<<row<<" "<<col<<endl;
		for(int i=0; i<row; i++)
		{
			for(int j=0; j<col; j++)
			{
				fin>>arr[i][j];
			//	cout<<arr[i][j];
			}
		//	cout<<endl;
		}
		for(int i=0; i<row;i++)
		{
			for(int j=0; j<col;)
			{
				if(arr[i][j]=='.')
				{
				//	cout<<arr[i][j]<<endl;
					j++;
					continue;
				}
				if(arr[i][j]=='#' && arr[i+1][j] == '#' && arr[i][j+1] =='#' && arr[i+1][j+1]=='#' && i+1<row && j+1<col)
				{
					arr[i][j]='/';
					arr[i+1][j]='\\';
					arr[i][j+1]='\\';
					arr[i+1][j+1]='/';	
					j+=2;
				}
				else if(arr[i][j]=='/' || arr[i][j]=='\\')
				{
					j++;
				}
				else
				{
					impossible = true;
					break;
				}
			}
			if(impossible == true)
				break;
		}		
		fout<<"Case #"<<z<<":"<<endl;
		if(impossible==true)
			fout<<"Impossible"<<endl;
		else	
		{
			for(int i=0;i<row;i++)
			{
				for(int j=0; j<col ;j++)
				{
					fout<<arr[i][j];
				}
				fout<<endl;
			}
		}
	}
	
	return 0;
}
