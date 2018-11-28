#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<iostream>
#include<stdlib.h>
#include<math.h>
using namespace std;

int case_no= 0;
int index=0,number=0;

char source[10000],target[10000];
char letter[100]= {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
char given[100] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};



void main ()
{

freopen ("d:/input/A-small-attempt1.in","r",stdin);
freopen ("d:/input/A-small-attempt1.out","w",stdout);
cin>>case_no;
		for(int in=0;in<=case_no;in++)
		{
			gets(source);
			for (int i=0; i< strlen(source); i++)
			{
				if(source[i]==' ')
						target[i]=source[i];
				else
				for(int j=0 ; j < strlen(letter); j++)
				{
					if(source[i]==letter[j])
						target[i] = given[j];
				}
			}
			target[strlen(source)]='\0';
			if(in>0)
			cout<<"Case #"<<in<<": "<<target<<"\n";
			//cout<<target;
		}

}

