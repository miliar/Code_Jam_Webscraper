#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
int l,d,n;
cin>>l;
int counter=0;
cin>>d;
cin>>n;
char words[25][10];
char words2[25][10];
int array_for_words[25];
int j=0;
for(int q=0;q<d;q++)
{
array_for_words[q]=1;
}
char test[500];
int token_number=0;
long int answer;

for(int i=0;i<d;i++)   // number of words in dictionary namely d
{
cin>>words[i];
}
for(int i=0;i<n;i++)   // number of cases we enter N
{
	cin>>test;
	
	for(int u=0;u<l;u++) // number of lettrs in a word, l
	{
		if(test[j]=='(')
		{
		
		j++;
		int buffer=j;
		for(int k=0;k<d;k++)
		{
		j=buffer;
		int flag=0;
		while(test[j]!=')')
		{
		if(words[k][u]==test[j])
			{	
			flag++;
			}
			j++;
		}
		if(flag==0) array_for_words[k]=0;
				
		}
		
		}
		
		if(test[j]!='(' && test[j]!=')')
		{
			
		    for(int k=0;k<d;k++)
			{
			
			if(test[j]==words[k][u])
			{
			
			if(array_for_words[k]==1)
			array_for_words[k]=1;
			
			}
			else
			{
			array_for_words[k]=0;
			}
			
			
			}
		
		}
		for(int p=0;p<d;p++)
	{
	
	}
	
	
		j++;
	}
	
	
	for(int p=0;p<d;p++)
	{ 
	if(array_for_words[p]==1)
	{
	counter++;
	}
	}
cout<<"Case #"<<i+1<<": "<<counter<<endl;
counter=0;

for(int p=0;p<d;p++)
	{ 
	array_for_words[p]=1;
	}
j=0;
}
return 0;
}
