#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	int T,N,M,i,j,k,flag=0,lendata;
	char data[101],c;
	ifstream ip("A-small-attempt1.in");
	ofstream op("write.txt");
	ip>>T;
	ip.get();
	for(i=0;i<T;i++)
	{
		k=0;
				
		while((c=ip.get())!='\n')
		{
			data[k]=c;
			k++;
		}
		data[k]='\0';
		lendata=k;
		for(j=0;j<lendata;j++)
		{
			switch(data[j])
			{
				case 'a': data[j]='y'; break;
				case 'b': data[j]='h'; break;
				case 'c': data[j]='e'; break;
				case 'd': data[j]='s'; break;
				case 'e': data[j]='o'; break;
				case 'f': data[j]='c'; break;
				case 'g': data[j]='v'; break;
				case 'h': data[j]='x'; break;
				case 'i': data[j]='d'; break;
				case 'j': data[j]='u'; break;
				case 'k': data[j]='i'; break;
				case 'l': data[j]='g'; break;
				case 'm': data[j]='l'; break;
				case 'n': data[j]='b'; break;
				case 'o': data[j]='k'; break;
				case 'p': data[j]='r'; break;
				case 'q': data[j]='z'; break;
				case 'r': data[j]='t'; break;
				case 's': data[j]='n'; break;
				case 't': data[j]='w'; break;
				case 'u': data[j]='j'; break;
				case 'v': data[j]='p'; break;
				case 'w': data[j]='f'; break;
				case 'x': data[j]='m'; break;
				case 'y': data[j]='a'; break;
				case 'z': data[j]='q'; break;
				default: data[j]=data[j];
			}
		}
		op<<"Case #"<<i+1<<": "<<data<<endl;
	}
	ip.close();
	op.close();
	return 0;
}
