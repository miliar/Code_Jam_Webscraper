#include <iostream>
#include <vector>
#include <string>
#include <iomanip>

using namespace std;

static string phrase = "welcome to code jam";

unsigned int tronquer(unsigned int a)
{
	float tf = ( (float) a)/10000;
	float ti = (unsigned int) tf;
	return 10000*(tf - ti);
}

unsigned int search(string text, int i,int j)
{
	unsigned int r=0;
	if (j>=phrase.size())
		return 1;
	if (i>=text.size())
		return 0;
	if (text[i]==phrase[j])
		r=search(text,i+1,j+1);
	r+=search(text,i+1,j);
	if (r>=10000)
		r = tronquer(r);
	return r;
}

int main()
{
	unsigned int N=0,i=0;
	char temp[510];
	cin >> N;
	cin.getline(temp,10);
	for (i=0;i<N;i++)
	{
		cin.getline(temp,510);
		cout << "Case #" << i+1 << ": " << setfill('0') << setw(4) << search(string(temp),0,0) << "\n";
	}
}

