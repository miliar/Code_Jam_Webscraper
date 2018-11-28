
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	char T1[26];
	string str= "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvqz";
	string str2="ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupzq";
	for(int i=0;i<str.length();i++)
	{
		T1[int(str[i])-97]=str2[i];
	}

    string test;
	fstream input,output;
	input.open("A-small-attempt2.in");
	output.open("out.txt");
	int T;
	input>>T;
	for (int t=0;t<T+1;t++)
	{
        getline(input,test);
		if(test!="")
		{
            	output<<"Case #"<<t<<": ";
			for(int i=0;i<test.length();i++)
			{
				if(97<=test[i]<=122)
				output<<char(T1[test[i]-97]);
				else
				output<<test[i];
			}
		if(t!=T)
			output<<endl;
		}
		
	}
	cout<<endl;
	system("pause");
	return 0;
}

