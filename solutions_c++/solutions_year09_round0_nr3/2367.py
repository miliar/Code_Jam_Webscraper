#include<iostream>
#include<string>
#include<fstream>
using namespace std;

char* ss="welcome to code jam";
int cnt = 0;
char* text;
int sizeofs;

void searchA(int pos1,int pos2)
{
	int i;
	for(i=pos1;i<sizeofs;i++){
		if(text[i]==ss[pos2])
			if(pos2==18){
				cnt++;
			}
			else
				searchA(i,pos2+1);
}
	return;	
				
}

int main(void)
{
	string str;
	fstream text2;
	text2.open("ABCD");

	getline(text2,str);
        int NL = 0;
	NL = atoi(str.c_str());
	int j;
	for(j=0;j<NL;j++)		
	{
		cnt = 0;
		getline(text2,str);
		text = (char*) str.c_str();
                sizeofs = str.size();
		searchA(0,0);
		cnt = cnt % 10000;
		if(cnt>1000)
			cout<<"Case #"<<j+1<<": "<<cnt<<endl;	
		else if(cnt>100)
			cout<<"Case #"<<j+1<<": 0"<<cnt<<endl;
		else if(cnt>10)
			cout<<"Case #"<<j+1<<": 00"<<cnt<<endl;
		else
			cout<<"Case #"<<j+1<<": 000"<<cnt<<endl;
	}	

}

