#include<iostream>
#include<string.h>
using namespace std;
char inputstring[101];
char finalstring[101];
char convert[36][4];
char opposed[28][3];
int combine,clear;

int clearstring(char current[])
{
	//cout<<"string in clear string function "<<current<<"\n";
	for(int i=0;i<clear;i++)
	{
	if(strchr(current,opposed[i][0])&&strchr(current,opposed[i][1]))
	return 1;
	else
	continue;
	}
	return 0;
}

char findreplacement(char a, char b)
{
	for(int i=0;i<combine;i++)
	{
		if((a==convert[i][0]&&b==convert[i][1])||(a==convert[i][1]&&b==convert[i][0]))
		return(convert[i][2]);
	}
	return '*';
}

int main()
{
	string base_string("QWERASDF");
int testcases;
int sampleinput;
int t=1;
	cin>>testcases;
	while(t<=testcases)
	{
		cin>>combine;
		for(int j=0;j<combine;j++)
		cin>>convert[j];
		cin>>clear;
		for(int k=0;k<clear;k++)
		cin>>opposed[k];
		cin>>sampleinput;
		cin>>inputstring;
		int final_pos = 0;
		finalstring[final_pos]=inputstring[final_pos];
		for(int p=1;inputstring[p]!='\0';p++)
		{
			
				char substitute = findreplacement(finalstring[final_pos],inputstring[p]);
				//cout<<"Substitute"<<substitute<<"final pos value is"<<final_pos<<"\n";
				if(substitute != '*')
				{
				finalstring[final_pos] = substitute;
				}
				else
				finalstring[++final_pos]=inputstring[p];
			
			finalstring[final_pos+1]='\0';
			//cout<<"String before clear string func "<<finalstring<<"final pos values"<<final_pos<<"\n";
			int val = clearstring(finalstring);
			//cout<<"Val"<<val<<"  p:"<<p<<"\n";
			if(val)
			{
			finalstring[0]=inputstring[++p];
			final_pos=0;
			}
		}
		finalstring[++final_pos]='\0';
			if(finalstring[0]!='\0')
			{
				cout<<"Case #"<<t<<": ["<<finalstring[0];
				int h=1;
				while(finalstring[h]!='\0')
				{
					cout<<", "<<finalstring[h++];
				}
			}
			else
			cout<<"Case #"<<t<<": [";
			cout<<"]\n";
		t++;
	}
}
