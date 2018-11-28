// GCJ_2011_2.cpp : Defines the entry point for the console application.
//
#include<stdio.h>
#include <iostream>
using namespace std;


void print(char* mylist, int n)
{
	//[E, A]
	cout<<"[";
	for(int i=0;i<n;i++)
	{
		if(i) cout<<", ";
		cout<<mylist[i];
	}
	cout<<"]";
}
void magicka()
{
	char output[102];
	char input[100];
	int n_output=0;
	 char combine[26][26];
	 char oppose[26];
	 int in_list[26];
	 
	 memset((void*)combine,0,26*26*sizeof(char));
	 memset((void*)oppose,0,26*sizeof(char));
	 memset((void*)in_list,0,26*sizeof(int));
	 int i,n_combine,n_input,n_oppose;
	 cin>>n_combine;
	 for(i=0;i<n_combine;i++) 
	 {
		 char val[4];
		 cin>>val;
		 combine[val[0]-'A'][val[1]-'A']=val[2];
		 combine[val[1]-'A'][val[0]-'A']=val[2];
	 }
	 cin>>n_oppose;
	 for(i=0;i<n_oppose;i++) 
	 {
		 char val[4];
		 cin>>val;
		 oppose[val[1]-'A']=val[0];
		 oppose[val[0]-'A']=val[1];
	 }
	 cin>>n_input;
	 cin>>input;
	 for(i=0;i<n_input;i++) 
	 {
		 output[n_output++]=input[i];
		 in_list[input[i]-'A']++;
		 if(n_output>1)
		 {
			 int last=output[n_output-1]-'A';
			 int last_1 = output[n_output-2]-'A';
			 if(combine[last][last_1]!=0)
			 {
				 in_list[last]--;
				 in_list[last_1]--;
				 output[n_output-2]=combine[last][last_1];
				 n_output--;
				 in_list[combine[last][last_1]-'A']++;
			 }
		 }
		 int last=output[n_output-1]-'A';
		 
		 if(oppose[last])
		 if(in_list[oppose[last]-'A'])
		 {
			 n_output=0;
			 memset((void*)in_list,0,26*sizeof(int));
		 }

	 }
	 print(output,n_output);


}
void magicka1()
{
	char output[102];
	char input[100];
	int n_output=0;
	 char combine[26][26];
	 bool oppose[26][26];
	 int in_list[26];
	 
	 memset((void*)combine,0,26*26*sizeof(char));
	 memset((void*)oppose,0,26*26*sizeof(bool));
	 memset((void*)in_list,0,26*sizeof(int));
	 int i,n_combine,n_input,n_oppose;
	 cin>>n_combine;
	 for(i=0;i<n_combine;i++) 
	 {
		 char val[4];
		 cin>>val;
		 combine[val[0]-'A'][val[1]-'A']=val[2];
		 combine[val[1]-'A'][val[0]-'A']=val[2];
	 }
	 cin>>n_oppose;
	 for(i=0;i<n_oppose;i++) 
	 {
		 char val[4];
		 cin>>val;
		 oppose[val[0]-'A'][val[1]-'A']=true;
		 oppose[val[1]-'A'][val[0]-'A']=true;
	 }
	 cin>>n_input;
	 cin>>input;
	 for(i=0;i<n_input;i++) 
	 {
		 output[n_output++]=input[i];
		 in_list[input[i]-'A']++;
		 if(n_output>1)
		 {
			 int last=output[n_output-1]-'A';
			 int last_1 = output[n_output-2]-'A';
			 if(combine[last][last_1]!=0)
			 {
				 in_list[last]--;
				 in_list[last_1]--;
				 output[n_output-2]=combine[last][last_1];
				 n_output--;
				 in_list[combine[last][last_1]-'A']++;
			 }
		 }
		 int last=output[n_output-1]-'A';
		 
		 for(int k=0;k<26;k++)
			 {
				 if(oppose[last][k])
				 if(in_list[k])
				 {
					 n_output=0;
					 memset((void*)in_list,0,26*sizeof(int));
				 }
		 }

	 }
	 print(output,n_output);


}

int main(int argc, char* argv[])
{
	int num_test;
	cin>>num_test;
	for(int i=0;i<num_test;i++)
	{
		cout<<"Case #"<<i+1<<": ";
		magicka1();
		cout<<"\n";
	}
	return 0;
}