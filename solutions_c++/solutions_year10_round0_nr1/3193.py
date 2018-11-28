#include <fstream>
using namespace std;
ifstream cin("input.txt");
ofstream cout("output.txt");

int main()
{
	int s;
	cin>>s;
	for(int i=0;i<s;i++)
	{
		int n,k;
		cin>>n>>k;
		cout<<"Case #"<<i+1<<": ";
		if((k%(1<<n))==((1<<n)-1))cout<<"ON";
		else cout<<"OFF";
		cout<<endl;
	}
	return 0;
}