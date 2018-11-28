#include <iostream>
using std::cout;
using std::cin;
#include <string>
#include <string.h>
#include <sstream>
using std::istringstream;
using namespace std;

int main()
{
	int cases;
	char ch,arr[30];
	string line;
	istringstream iss;
	arr[1]='y';
    arr[2]='h';
    arr[3]='e';
    arr[4]='s';
    arr[5]='o';
    arr[6]='c';
    arr[7]='v';
    arr[8]='x';
    arr[9]='d';
    arr[10]='u';
    arr[11]='i';
    arr[12]='g';
    arr[13]='l';
    arr[14]='b';
    arr[15]='k';
    arr[16]='r';
    arr[17]='z';
    arr[18]='t';
    arr[19]='n';
    arr[20]='w';
    arr[21]='j';
    arr[22]='p';
    arr[23]='f';
    arr[24]='m';
    arr[25]='a';
    arr[26]='q';
    
	cin>>cases;
	getline(cin,line);
	for(int kase=1;kase<=cases;kase++)
	{
		getline(cin,line);
		iss.str(line);
		cout<<"Case #"<<kase<<": ";
		while((ch=iss.get())!=-1)
		{
			if(ch==' ')cout<<' ';
			else
				cout<<arr[ch-'a'+1];
		}
		cout<<"\n";
		iss.clear();
	}
	return 0;
}