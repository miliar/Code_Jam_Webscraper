#include<iostream>
#include<fstream>
#include<string>
using namespace std;
void findnext(int * matrix,int &i,int & j,int row ,int coloum)
{
	
	int * array= new int[row];
	for(int k=0;k<row;k++)
	{
		
		
		for(int l=j+1;l<coloum;l++)
		{
			if(matrix[k*coloum + l]!=0)
				break;
		}
		array[k]=l;
		
		
		
		
	}
	array[i]=-1;
	int max=0;
	for(int b=0;b<row;b++)
	{
		if(array[b]>array[max])
			max=b;
		
		
	}
	
	i=max;
	j=array[max];
	
	
	
	
	
	
	return;
	
	
	
}
int final(int * matrix,int row,int coloum)
{
	int counter=0;
	int i=-1;
	int j=-1;
	while(j<coloum)
	{
		findnext(matrix,i,j,row,coloum);
		counter++;
		
		
		
	}
	
	
	return counter-1;
	
	
	
	
	
	
	
	
	
}
bool equal(string first,string second)
{
	
	
	int size1=first.size();
	int size2=second.size();
	if(size1!=size2)
		return false;
	for(int i=0;i<size1;i++)
	{
		
		if(first[i]!=second[i])
			return false;
		
		
	}
	
	
	return true;
	
}
int main()
{
	
	int last;
	
	ofstream outfile;
	outfile.open("output.txt");
	ifstream infile;
	infile.open("A-small.in");
	int term;
	infile>>term;
	int size1,size2;
	char name[100];
	int * matrix;
	string * array;
	string dummy;
	for(int i=0;i<term;i++)
	{
		
		infile>>size1;
		array = new string[size1];
		infile.getline(name,100,'\n');
		for(int k=0;k<size1;k++)
		{
			infile.getline(name,100,'\n');
			array[k]=name;
		}
		infile>>size2;
		matrix=new int [size1* size2];
		for(int l=0;l<size1;l++)
		{
			
			
			for(int m=0;m<size2;m++)
			{
				
				matrix[l*size2+m]=0;
				
				
			}
			
			
			
			
		}
		
		infile.getline(name,100,'\n');
		for(int j=0;j<size2;j++)
		{
			
			infile.getline(name,100,'\n');
			dummy=name;
			for(int u=0;u<size1;u++)
			{
				if(equal(dummy,array[u]))
					break;
				
			}
			
			matrix[u*size2+j]=1;
			
		}
		
			for(l=0;l<size1;l++)
		{
			
			
			for(int m=0;m<size2;m++)
			{
				
				cout<<matrix[l*size2+m]<<"   ";
				
				
			}
			cout<<endl;
			
			
			
		}
		
		
		last=final(matrix,size1,size2);
		outfile<<"Case #"<<i+1<<":  "<<last<<endl;
		cout<<endl<<endl;
		
	}
	
	
	
	
	
	return 0;
}