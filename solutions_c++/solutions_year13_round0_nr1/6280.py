#include<iostream>
#include<fstream>
using namespace std;
bool check(int row1 , int column1 , char symbol , int & count);
char A[4][4];
ofstream fout("Out.txt"); 
ifstream fin("A-small-attempt1.in");
int main()
{
	int i , j , counter=1; bool c2 = true;
	int NUMBER;
	fin>>NUMBER;
	for(int s=0 ; s<NUMBER ; s++)
	{
		fout<<"Case #"<<s+1<<": ";
		counter = 1;
		c2 = true;

		for(i=0 ; i<4 ; i++)
			for(j=0 ; j<4 ; j++)
				fin>>A[i][j];
		for(i=0 ; i<4 ; i++)
		{
			for(j=0 ; j<4 ; j++)
			{
				if(check(i , j , A[i][j] , counter))
				{
					goto end;
				}
				else if( counter == 17 )
				{	
					for(int i1=0 ; i1<4 ; i1++)
						for(int j1=0 ; j1<4 ; j1++)
							if(A[i1][j1] == '.')
							{
								fout<<"Game has not completed"<<endl; 
								c2 = false;
								goto end;
							}
							if(c2)
							{	fout<<"Draw"<<endl;  goto end;}
				}
			}
		}
end:
		cout<<"";
	}

	return 0;
}

bool check(int row1 , int column1 , char symbol , int & count)
{
	if(symbol == 'X' || symbol == 'O')
	{
		int k=1, a=0;
		if(column1 != 0)
			while(A[row1][column1-k] == symbol || A[row1][column1-k] == 'T')
			{
				a++; 
				if( (column1-k)==0 )   break;
				else k++;  
			}
			k=1;
			if(column1 != 3)
				while(A[row1][column1+k]==symbol || A[row1][column1+k] == 'T')
				{
					a++; 
					if((column1+k)==3)  break;
					else k++;
				}
				if(a==3) 
				{
					fout<<symbol<<" won"<<endl;
					return true;
				}
				else { 
					k=1; a=0;
					if(row1!=0)   
						while(A[row1-k][column1]==symbol || A[row1-k][column1]=='T')
						{
							a++;
							if( (row1-k)==0 ) break;
							else k++;
						}
						k=1;
						if(row1!=3)
							while(A[row1+k][column1]==symbol || A[row1+k][column1]=='T')
							{
								a++;
								if( (row1+k)==3 ) break;
								else k++;
							}
				}
				if(a==3) {
					fout<<symbol<<" won"<<endl; 
					return true; 
				}
				else {
					k=1; a=0;
					if( (row1!=0) && (column1!=0) )
						while(A[row1-k][column1-k]==symbol || A[row1-k][column1-k]=='T')
						{
							a++;
							if( ((row1-k)==0) || ((column1-k)==0) ) break;
							else k++;
						}
						k=1;
						if( (row1 != 3) || (column1 != 3) )
							while(A[row1+k][column1+k]==symbol || A[row1+k][column1+k]=='T')
							{
								a++;
								if( (row1+k) == 3 || (column1+k) == 3 ) break;
								else k++;
							}
				}
				if(a==3) {
					fout<<symbol<<" won"<<endl;
					return true;
				}
				else {
					k=1; a=0;
					if( (row1)!=3 && (column1)!=0 )
						while(A[row1+k][column1-k]==symbol || A[row1+k][column1-k]=='T')
						{
							a++;
							if( (row1+k)==3 || (column1-k)==0 ) break;
							else k++;
						}
						k=1;
						if( (row1)!=0 && (column1)!=3 )
							while(A[row1-k][column1+k]==symbol || A[row1-k][column1+k]=='T')
							{
								a++;
								if( (row1-k)==0 || (column1+k)==3 ) break;
								else k++;
							}
				}
				if(a==3) {
					fout<<symbol<<" won"<<endl;
					return true;
				}
				else {
					count++;
					return false;
				}
	}
	else {
		count++;
		return false;
	}
}