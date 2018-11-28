#include<iostream.h>
#include<conio.h>
#include<stdio.h>
#define max 26
// input string is in lower case
struct input
{
    char ipstr[350];
    input *next;
};
void main()
{
	char str[26]={'y','h','e','s','o','c','v','x','d','u','i',
		       'g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int i,j;
	int testcase;
	input *ptr,*ip;
	cin>>testcase;
	ptr=new input;
	ptr->next=NULL;
	ip=ptr;
	for(i=1;i<=testcase;i++)
	{
	      gets(ptr->ipstr);
	      ptr->next=new input;
	      ptr=ptr->next;
	      ptr->next=NULL;

	}
	cout<<"\nOUTPUT";
	ptr=ip;
	for(i=1;i<=testcase;i++)
	{

	      cout<<"\nCASE #"<<i<<" : ";
	      for(j=0;ptr->ipstr[j]!='\0';j++)
	      {
		   if(ptr->ipstr[j]==' ')
		   {
		       cout<<" ";
		   }
		   else
		   if((int)ptr->ipstr[j]>=97 && (int)ptr->ipstr[j]<123)
		   {

		      cout<< str[((int)ptr->ipstr[j])-97];
		   }
	      }
	      ptr=ptr->next;

	}
}