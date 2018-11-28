#include<fstream>

using namespace std;

char *a="yhesocvxduiglbkrztnwjpfmaq";

int main()
{
	ifstream f1("1.in");
	ofstream f2("1.out");
	int n,l,i;
	char c[200];
	f1 >> n;
	f1.getline(c,200,'\n');
	for (i = 0; i < n; i++)
	{
		f1.getline(c,200,'\n');
		f2 << "Case #" << i+1 << ": ";
		l=strlen(c);	
		for (int j = 0; j < l; j++)
		{
			if (c[j]!=' ') c[j]=a[c[j]-'a'];
		}
		f2 << c;
		f2<<'\n';
	}
	f1.close();
	f2.close();
	return 0;
}