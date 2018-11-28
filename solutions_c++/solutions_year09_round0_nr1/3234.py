#include<iostream>
#include<fstream>
#include<string>
using namespace std;

string * find(string * wordlist,string key,int words,int index)
{
	int i,j;
	int count=0;
	int length=key.length();
	string * returnlist=new string[words];
	for(i=0;i<words;++i)
	{
		for(j=0;j<length;++j)
		{
			if((wordlist[i].c_str())[index]==key[j])
			{
				returnlist[count]=wordlist[i].c_str();
				count++;
				break;
			}
		}
	}
	return returnlist;
}

int findnonblank(string * wordlist,int words)
{
	int i;
	int count=0;
	for(i=0;i<words;++i)
	{
		if(wordlist[i].length()==0)
		{
			continue;
		}
		count++;
	}
	return count;
}

int main()
{
	int length;
	int words;
	int tests;
	int i,j,k;
	ifstream in;
	in.open("A-small.in");
	in>>length>>words>>tests;
	string *wordlist=new string [words];
	for(i=0;i<words;++i)
	{
		in>>wordlist[i];
	}

	string *list=new string [words];
	char ch;
	char *chr=new char[512];
	string str;
	for(j=0;j<tests;++j)
	{	
		list=wordlist;
		for(i=0;i<length;++i)
		{
			in>>ch;
			if(ch=='(')
			{
				in.getline(chr,512,')');
				str=chr;
			}
			else
			{
				str=ch;
			}
			list=find(list,str,words,i);
		}
		cout<<"Case #"<<j+1<<": "<<findnonblank(list,list->length())<<endl;
	}

	return 0;
}