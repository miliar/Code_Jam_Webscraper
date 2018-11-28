#include<fstream>
#include<iostream>
using namespace std;

ofstream out("output.txt");
char map[26];
bool mappato[26];
char da[105];

int main(void)
{
	FILE *fp=fopen("input.txt", "r");
	string from="ejp mysljylc kd kxveddknmc re jsicpdrysi";
	string to="our language is impossible to understand";
	for(int i=0;i<from.size();i++)
	{
		map[from[i]-'a']=to[i];
		//mappato[to[i]-'a']=true;
	}
	from="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	to="there are twenty six factorial possibilities";
	for(int i=0;i<from.size();i++)
	{
		map[from[i]-'a']=to[i];
		//mappato[to[i]-'a']=true;
	}
	from="de kr kd eoya kw aej tysr re ujdr lkgc jv";
	to="so it is okay if you want to just give up";
	for(int i=0;i<from.size();i++)
	{
		map[from[i]-'a']=to[i];
		//mappato[to[i]-'a']=true;
	}
	
	map['q'-'a']='z';
	map['z'-'a']='q';
	/*for(int i=0;i<26;i++)
		if(map[i]==0)
			cout << (char)(i+'a') << endl;
	cout << endl;
	for(int i=0;i<26;i++)
		if(mappato[i]==0)
			cout << (char)(i+'a') << endl;*/
	int x;
	fscanf(fp, "%d\n", &x);
	for(int p=1;p<=x;p++)
	{
		out << "Case #" << p << ": ";
		fgets(da, 105, fp);
		for(int i=0;da[i+1]!=0;i++)
			if(da[i]==' ')
				out << ' ';
			else out << map[da[i]-'a'];
		out << endl;
	}
	out.close();
	fclose(fp);
}
