#include<fstream>
using namespace std;
char a[103],b[103],ch[30]="yhesocvxduiglbkrztnwjpfmaq";
int i,j,n;
int main()
{
	ifstream f("speak_tongue.in");ofstream g("speak_tongue.out");
	f>>n; f.get();
	for(i=1;i<=n;i++)
	{
		f.getline(a,104);
		for(j=0;j<strlen(a);j++)
		  if(a[j]!=' ')a[j]=ch[a[j]-'a'];
		g<<"Case #"<<i<<": "<<a<<"\n";
	}
	f.close();g.close();
return 0;}
