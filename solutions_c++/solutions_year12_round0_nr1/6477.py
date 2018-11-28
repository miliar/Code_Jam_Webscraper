#include <iostream>
#include <cstring>
#include <string>

using namespace std;

int main()
{
char a;
string string1, string2;
int num;

int j=0;

cin>>num;

getline(cin,string1);
do
{
	
	//string1=cin.get();
	if(j>0){
	cout<<"Case #"<<j<<": ";
	}
	for(int i=0;i<=string1.length();i++){	

	


	if(string1[i]==' ')
		cout<<" ";//whtspace
	if(string1[i]=='y')
		cout<<"a";
	if(string1[i]=='n')
		cout<<"b";
	if(string1[i]=='f')
		cout<<"c";
	if(string1[i]=='i')
		cout<<"d";
	if(string1[i]=='c')
		cout<<"e";
	if(string1[i]=='w')
		cout<<"f";
	if(string1[i]=='l')
		cout<<"g";
	if(string1[i]=='k')
		cout<<"i";
	if(string1[i]=='b')
		cout<<"h";
	if(string1[i]=='u')
		cout<<"j";
	if(string1[i]=='o')
		cout<<"k";
	if(string1[i]=='m')
		cout<<"l";
	if(string1[i]=='x')
		cout<<"m";
	if(string1[i]=='s')
		cout<<"n";
	if(string1[i]=='e')
		cout<<"o";
	if(string1[i]=='v')
		cout<<"p";
	if(string1[i]=='z')
		cout<<"q";
	if(string1[i]=='p')
		cout<<"r";
	if(string1[i]=='d')
		cout<<"s";
	if(string1[i]=='r')
		cout<<"t";
	if(string1[i]=='j')
		cout<<"u";
	if(string1[i]=='g')
		cout<<"v";
	if(string1[i]=='t')
		cout<<"w";
	if(string1[i]=='h')
		cout<<"x";
	if(string1[i]=='a')
		cout<<"y";
	if(string1[i]=='q')
		cout<<"z";

	//a=cin.get();
	
	}//end for
	cout<<endl;
j++;
getline(cin,string1);
string2=string1;

}while(j<num);//end of while
	cout<<"Case #"<<j<<": ";
	for(int i=0;i<=string2.length();i++){	

	if(string1[i]==' ')
		cout<<" ";//whtspace
	if(string1[i]=='y')
		cout<<"a";
	if(string1[i]=='n')
		cout<<"b";
	if(string1[i]=='f')
		cout<<"c";
	if(string1[i]=='i')
		cout<<"d";
	if(string1[i]=='c')
		cout<<"e";
	if(string1[i]=='w')
		cout<<"f";
	if(string1[i]=='l')
		cout<<"g";
	if(string1[i]=='k')
		cout<<"i";
	if(string1[i]=='b')
		cout<<"h";
	if(string1[i]=='u')
		cout<<"j";
	if(string1[i]=='o')
		cout<<"k";
	if(string1[i]=='m')
		cout<<"l";
	if(string1[i]=='x')
		cout<<"m";
	if(string1[i]=='s')
		cout<<"n";
	if(string1[i]=='e')
		cout<<"o";
	if(string1[i]=='v')
		cout<<"p";
	if(string1[i]=='z')
		cout<<"q";
	if(string1[i]=='p')
		cout<<"r";
	if(string1[i]=='d')
		cout<<"s";
	if(string1[i]=='r')
		cout<<"t";
	if(string1[i]=='j')
		cout<<"u";
	if(string1[i]=='g')
		cout<<"v";
	if(string1[i]=='t')
		cout<<"w";
	if(string1[i]=='h')
		cout<<"x";
	if(string1[i]=='a')
		cout<<"y";
	if(string1[i]=='q')
		cout<<"z";
	}
	cout<<endl;
return 0;
}//end of main
