#include <iostream>
#include <string>

using namespace std;

const char Hash[27] = {'y','h','e','s','o','c',
                       'v','x','d','u','i','g',
                       'l','b','k','r','z','t',
                       'n','w','j','p','f','m','a','q'};
int main()
{
	FILE *in,*out;
	in = freopen("A-small-attempt2.in","r",stdin);
	out = freopen("Redownload A-small.txt","w",stdout);
	int TCases;
	int NCase = 1;
	cin >>TCases;
	getchar();
	while(TCases--)
	{
		string Str;
		getline(cin,Str);
		for(string::size_type i = 0; i != Str.size();i++)
		{
			if(' ' != Str[i])
				Str[i] = Hash[Str[i]-'a'];
		}
		cout <<"Case #" <<NCase++ <<": " <<Str <<endl;
	}
	fclose(in);
	fclose(out);
	return 0;
}