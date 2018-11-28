#include <iostream>
#include <string>
using namespace std;

int count(char*);

void main()
{
	char a[5];
	char** text;

	int N;
	cin>>N;
	cin.ignore();

	text=new char*[N];
	for(int j=0;j!=N;j++)
	{
		text[j]=new char[500];
		cin.getline((char*)text[j],500);
	}

	for(int i=0;i<N;i++)
	{
		cout<<"Case #"<<i+1<<": ";
		cout.width(4);
		cout.fill('0');
		itoa(count(text[i]),a,10);
		cout<<a<<endl;
	}
	

}

int count(char*text)
{
	int s[19]={0};
	
	for(int i=0;i<500;i++)
	{
		switch(text[i])
		{
		case 'w':
			s[0]++;
			break;
		case 'e':
		
			s[1]+=s[0];
			s[6]+=s[5];
			s[14]+=s[13];
			break;
		
		case 'l':
			s[2]+=s[1];
			break;
		case 'c':
			s[3]+=s[2];
			s[11]+=s[10];
			break;
		case'o':
			s[4]+=s[3];
			s[9]+=s[8];
			s[12]+=s[11];
			break;
		case 'm':					
			s[5]+=s[4];
			s[18]+=s[17];
			break;
		case' ':			
			s[7]+=s[6];
			s[10]+=s[9];
			s[15]+=s[14];			
			break;
		case't':
			s[8]+=s[7];
			break;
		case'd':
			s[13]+=s[12];
			break;
		case'j':
			s[16]+=s[15];
			break;
		case'a':
			s[17]+=s[16];
			break;

		}

		
	}
	return s[18];
}