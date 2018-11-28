#include <string>
#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std;

string source = "qzejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv";
string mapped = "zqourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";

string mapping(1 << 8, ' ');

void InitMapping()
{
	for(size_t i = 0; i < source.size(); i++)
	{
		mapping[source[i]] = mapped[i];
	}
}

char TransformChar(char ch)
{
	return mapping[ch];
}

int main(int argc, char * argv[])
{
	InitMapping();
	freopen("in.txt", "r", stdin);
	string buf;
	getline(cin, buf);
	string out;
	int cases = atoi(buf.c_str());
	for(int test = 1; test <= cases; test++)
	{
		getline(cin, buf);
		out.resize(buf.size());
		transform(buf.begin(), buf.end(), out.begin(), TransformChar);
		cout << "Case #" << test << ": " << out << endl;
	}
	return 0;
}