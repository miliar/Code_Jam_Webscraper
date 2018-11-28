#include<iostream>
#include<stdio.h>
#include<string>
using namespace std;

void sort(int x[],int length)
{
  int key,i;
  for(int j=1;j<length;j++)
  {
     key=x[j];
     i=j-1;
     while(x[i]>key && i>=0)
     {
               x[i+1]=x[i];
         i--;
     }
     x[i+1]=key;
  }
}

int main()
{
        int k,cases;
	cin>>cases;
	for(k=0;k<cases;k++)
	{
	int i,j;
 	int tatime,tripab,tripba,trainA=0,trainB=0;
	cin>>tatime;
	cin>>tripab,
	cin>>tripba;
	int depA[tripab],arrB[tripab];
	int depB[tripba],arrA[tripba];
	int hr,min;
	for(i=0;i<tripab;i++)
	{
		scanf("%02d:%02d",&hr,&min);
		depA[i] = 60*hr+min;
		scanf("%02d:%02d",&hr,&min);
		arrB[i] = 60*hr+min ;
	}		
	sort(depA,tripab);	
	sort(arrB,tripab);
		
	for(i=0;i<tripba;i++)
	{
		scanf("%02d:%02d",&hr,&min);
		depB[i] = 60*hr+min;
		scanf("%02d:%02d",&hr,&min);
		arrA[i] = 60*hr+min;
	}
	sort(depB,tripba);
	sort(arrA,tripba);
	
	i=0,j=0;
	while(i<tripab && j<tripba)
	{
		if(depA[i]<arrA[j]+tatime)
		{
			trainA++;
			i++;
		}
		else
		{
			i++;j++;
		}
	}
	trainA += (tripab-i);
	
	i=0,j=0;
	while(i<tripba && j<tripab)
	{
		if(depB[i]<arrB[j]+tatime)
		{
			trainB++;
			i++;
		}
		else
		{
			i++;j++;
		}
	}
	trainB += (tripba -i);
	cout<<"Case #"<<k+1<<": "<<trainA<<" "<<trainB<<endl;
	}
	return 0;
}		

