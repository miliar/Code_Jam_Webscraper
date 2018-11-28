#include <iostream>
#include <math.h>
#include <algorithm>
#include <sstream>
using namespace std;
int main()
{
	char a[30];
	a[1]='y';
	a[2]='h';
	a[3]='e';
	a[4]='s';
	a[5]='o';
	a[6]='c';
	a[7]='v';
	a[8]='x';
	a[9]='d';
	a[10]='u';
	a[11]='i';
	a[12]='g';
	a[13]='l';
	a[14]='b';
	a[15]='k';
	a[16]='r';
	a[17]='z';
	a[18]='t';
	a[19]='n';
	a[20]='w';
	a[21]='j';
	a[22]='p';
	a[23]='f';
	a[24]='m';
	a[25]='a';
	a[26]='q';

	int b;
	int c;
	cin>>c;
        string s;
        cin.ignore();
        for(int i=1;i<=c;i++)
        {
        getline(cin,s);
        stringstream ss;
        ss<<s;
	cout<<"Case #"<<i<<":"<<" ";
        while(ss>>s)
        {
        for(int i=0;i<s.size();i++)
                {
                b=s[i]-96;
                cout<<a[b];
                }
        cout<<" ";
        }
        cout<<endl;
        }
return 0;
}
