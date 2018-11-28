#include<iostream>
#include<cstring>
#include<fstream>
using namespace std;

int main()
{
    ifstream in("A-small-attempt0.in");
	ofstream out("A.out");
	char p[27]="yhesocvxduiglbkrztnwjpfmaq";
	int t,i;
	in >> t;
	in.get();
    for(i=0;i<t;i++)
    {
        char g[110]={};
		in.getline(g,110);
		int len=strlen(g);
		int j;
		out << "Case #" << i+1 << ": ";
		for(j=0;j<len;j++)
		{
			if(g[j]==' ') out << ' ';
			else
				out << p[g[j]-'a'];
		}
		out << endl;
    }
    return 0;
}
