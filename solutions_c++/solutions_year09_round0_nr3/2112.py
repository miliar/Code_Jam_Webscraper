#include<string>
#include<iostream>
#include<vector>
#include<iomanip>
using namespace std;

int magia(char *w,char* t)
{
	int i=0;
	int cant=0;
	if(w[0]=='\0')
		return 1;
	while(t[i]!='\0')
	{
		if(t[i]==w[0])
			cant+=magia(w+1,t+i);
		i++;
	}
	return cant;
}

int main()
{
	char * wel="welcome to code jam";
	char s[502];
	int n,cant;
	cin>>n;
	cin.ignore();
	for(int i=0;i<n;i++){
		cant=0;
		cin.getline(s,502,'\n');
		cant=magia(wel,s);
		cout<<"Case #"<<i+1<<": "<<setw(4)<<setfill('0')<<cant%10000<<endl;
	}
//	cin>>n;
	return 0;
}

