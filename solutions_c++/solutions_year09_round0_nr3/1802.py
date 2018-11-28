#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>
#include <algorithm>

using namespace std;

ifstream myin("C-small-attempt0.in");
ofstream myout("3.out");

unsigned int findsub(int srcEnd, int objEnd);
string src;
string obj = "welcome to code jam"; //welcome to code jam
int main()
{
	int N;
	myin >> N;
	string tmp;
	getline(myin, tmp);//eat up
	for(int caseCnt=0; caseCnt<N; ++caseCnt)
	{
		unsigned int res = 0;
		string str;
		src = "";
		getline(myin, str);
		for(size_t i=0; i<str.size(); ++i)
		{
			if( (src == "") && (str[i]!=obj[0]) )
				continue;
			if(obj.find(str[i]) != string::npos)
				src += str[i];
		}
		res = findsub(src.size(), obj.size());
		myout << "Case #" << caseCnt+1 << ": " << setw(4) << setfill('0') << res << endl;
	}
	return 0;
}

unsigned int findsub(int srcEnd, int objEnd)
{
	if(srcEnd < objEnd || srcEnd<=0 || objEnd<=0)	return 0;
	if(srcEnd == objEnd)
	{
		return(src.substr(0, srcEnd).compare( obj.substr(0, objEnd) ) == 0);
	}
	if(objEnd == 1)
		return (count(src.begin(), src.begin()+srcEnd, obj[0]) );
	if(src[srcEnd-1] != obj[objEnd-1])
		return(findsub(srcEnd-1, objEnd));
	else
		return( (findsub(srcEnd-1, objEnd)  %10000) + 
				(findsub(srcEnd-1, objEnd-1)%10000) );
}