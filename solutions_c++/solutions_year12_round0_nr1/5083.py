#include <iostream>
#include <string>
#include <fstream>
using namespace std;

void parsesentence(string google, string english, char * letters)
{
	if(google.length()!=english.length())
	{
	    cout<<"The sentences aren't the same length\n";
		return;
	}
	for(int i=0;i<english.length();i++)
	{
	   if(google[i]!=' ')
	   {
		  if(letters[google[i]-'a']=='F')
			 letters[google[i]-'a']=english[i];
		  else if(letters[google[i]-'a']!=english[i])
			  cout<<"Conflict with "<<google[i]<<endl;
	   }
	}
}

char findmissing(char * letters)
{
	bool chars[26];
	for(int i=0;i<26;i++)
		chars[i]=false;
	for(int i=0;i<26;i++)
	{
		if(letters[i]!='F')
		  chars[letters[i]-'a']=true;
	}
	for(int i=0;i<26;i++)
	{
	   if(chars[i]==false)
	     return i+'a';
	}
	return '\0';
}

string translate(string input, char * letters)
{
	string result="";
	for(int i=0;i<input.length();i++)
	{
		if(input[i]==' ')
			result+=" ";
		else
			result+=letters[input[i]-'a'];
	}
	return result;
}

int main()
{
	char letters[26];//indices google letters, values are english translations
	for(int i=0;i<26;i++)
	  letters[i]='F';//Sentinel
   // letters['y'-'a']='a';
	//letters['q'-'a']='o';
	//letters['e'-'a']='z';
	string google="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string english="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	parsesentence(google,english,letters);
	letters[25]=findmissing(letters);
	letters[16]=findmissing(letters);
	string input;
	string output;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int n;
	fin>>n;
	getline(fin,input);
	for(int i=1;i<=n;i++)
	{
		getline(fin,input);
		fout<<"Case #"<<i<<": "<<translate(input,letters)<<endl;
	}

}
