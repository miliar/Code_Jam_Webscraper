#include<iostream>
#include<stdio.h>
#include<vector>
using namespace std;
int main(){
//	char* dict="abcdefghijklmnopqrstuvxywz";
//	char* dict="yhesocvxduiglbkrztnwjpmafq";

//	char* dict="abcdefghijklmnopqrstuvwxyz";
	char* dict="yhesocvxduiglbkrztnwjpfmaq";

	vector<vector<char> > output;
	
	char* input="deneme";
	int N;
	cin>>N;
	output.resize(N);
	for(int j=0;j<N;j++)
		output[j].resize(0);
	int i=0;
	char c;
	i = N;
	c=getchar();
	while (N>0)
	{	
		c=getchar();
		if(c=='\n')
		{
			N=N-1;
			continue;
		}
		if(c==' '){
			output[i-N].push_back(' ');//			cout<<' ';
		}
		else
		{	
			output[i-N].push_back(dict[((int)c)-((int)'a')]);//cout<<dict[((int)c)-((int)'a')];
		}
	}

	for(int j=0;j<i;j++)
	{
		cout<<"Case #"<<j+1<<": ";
		for(int k=0;k<output[j].size();k++)
			cout<<output[j].at(k);
		cout<<endl;
	}

	return 0;
}
