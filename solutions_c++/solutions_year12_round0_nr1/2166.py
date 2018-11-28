#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

char ch[256];
char txt1[]="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
char txt2[]="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

int ap[256];

int main()
{
	memset(ch,0,sizeof(ch));
	memset(ap,0,sizeof(ap));
	ch['y']='a';
	ch['e']='o';
	ch['q'] ='z';
	ch['z'] = 'q';
	ch[' '] = ' ';
	int l = strlen(txt1);
	for(int i=0;i<l;i++){
		if(txt1[i]!=' '){
			ch[txt1[i]]=txt2[i];
			//printf("1:%c  2:%c\n",txt1[i], txt2[i]);
		}
	}
	int n = 0;
	cin>>n;
	char buf[300];
	cin.getline(buf, 300);
	for(int i=0;i<n;i++){
		cout<<"Case #"<<i+1<<": ";
		cin.getline(buf, 300);
		l = strlen(buf);
		for(int i=0;i<l;i++)cout<<ch[buf[i]];
		cout<<"\n";
	}
/*
	for(char i = 'a'; i<='z';i++)
	{
		ap[ch[i]]=1;
	}
	for(char i = 'a'; i<='z';i++)
	{
		if(ch[i])printf("%c %c",i,ch[i]);
		else printf("%c ???",i);
		if(ap[i])printf(" v \n");
		else printf(" x \n");
	}*/


	return 0;
}
