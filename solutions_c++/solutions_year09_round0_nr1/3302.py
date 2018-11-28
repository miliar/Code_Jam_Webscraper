#include<iostream>
#include<fstream>
#include<string>
using namespace std;

class Alienlang
{
public:
	char *ch;
};

int match(char *test,Alienlang *ptr,int patterns);
bool match_lang(char *test,char *pattern);
char *getchars(char *test,int t_index);
bool tester(char *p,char ch);
int move(char *,int);
int main()
{
	int length,patterns,testcases;
	char *c=new char[10];

	Alienlang *ptr;

	ofstream fout;
	fout.open("output.txt");

	ifstream fin;
	fin.open("A-small-attempt1.in");

	if(!fin)
	{
		cerr<<"error: cannot open file"<<endl;
		exit(1);
	}

	fin.getline(c,10,' ');
	length=atoi(c);
	fin.getline(c,10,' ');
	patterns=atoi(c);
	fin.getline(c,10,'\n');
	testcases=atoi(c);

	ptr=new Alienlang[patterns];
	for(int i=0;i<patterns;i++)
	{
		ptr[i].ch=new char[length];
	}
	//char c;
	//fin>>c;
	for(int i=0;i<patterns;i++)
	{
		fin.getline(ptr[i].ch,strlen(ptr[i].ch),'\n');
	}
	/////////////////////////////read file

	char *test=new char[10000];

	for(int i=0;i<testcases;i++)
	{
		fin.getline(test,10000,'\n');
		int matchcases=match(test,ptr,patterns);
		cout<<"Case #"<<i+1<<": "<<matchcases<<endl;
		fout<<"Case #"<<i+1<<": "<<matchcases<<endl;
//		strcpy(test,"");
	}

	fin.close();
	fout.close();
	return 1;
}

int match(char *test,Alienlang *ptr,int patterns)
{
	int match_count=0;
	for(int i=0;i<patterns;i++)
	{
		bool check = match_lang(test,ptr[i].ch);
		if(check==true)
			match_count++;
	}
	return match_count;
}

bool match_lang(char *test,char *pattern)
{
	int t_index=0;
	int p_index=0;
	
	char *p=new char[10000];

	while(test[t_index]!='\0')
	{
		if(test[t_index]=='(')
		{
			p=getchars(test,t_index);
			bool check=tester(p,pattern[p_index]);
			if(check!=true)
			{
				return false;
			}
			t_index=move(test,t_index);
			p_index++;
		}
		else
		{
			if(test[t_index]==pattern[p_index])
			{
				t_index++;
				p_index++;
				//return true;
			}
			else
			{
				return false;
			}
		}
	}

	//delete p;
	return true;
}
char *getchars(char *test,int t_index)
{
	char *ch=new char[10000];
	
	t_index++;
	int i=0;
	while(test[t_index]!=')')
	{
		ch[i]=test[t_index];
		i++;
		t_index++;
	}
	ch[i]='\0';

	return ch;
}

bool tester(char *p,char ch)
{
	int i=0;
	while(p[i]!='\0')
	{
		if(p[i]==ch)
		{
			return true;
		}
		i++;
	}
	return false;
}

int move(char *test,int t_index)
{
	while(test[t_index]!=')')
	{
		t_index++;
	}
	return t_index+1;
}