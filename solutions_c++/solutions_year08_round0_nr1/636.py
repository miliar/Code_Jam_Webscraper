#include <fstream>
#include <string>
#include <stack>
#include <iostream>
#include <map>

using namespace std;

#define MAXNOMBRE 100

char buscador[MAXNOMBRE+1];

int main(int argc,char* argv[])
{
	string inputfile,outputfile;
	if(argc==2)
		inputfile=argv[1];
	else
	{
		cout<<"Input: ";
		cin>>inputfile;
	}
	outputfile=inputfile;
	if(inputfile.find("in")!=inputfile.npos)
		outputfile.replace(outputfile.find("in"),2,"out");
	else
		outputfile.append(".out.txt");
	ifstream in(inputfile.c_str());
	ofstream out(outputfile.c_str());
	int n;
	in>>n;
	for(int i=0;i<n;i++)
	{
		map<string,char> Buscadores;
		int S;
		in>>S;
		in.get();
		for(int j=0;j<S;j++)
		{
			in.getline(buscador,sizeof(buscador));
			Buscadores[(string)buscador]=0;
		}
		int Q;
		in>>Q;
		stack<string> Qrs;
		string Qr;
		in.get();
		for(int j=0;j<Q;j++)
		{
			in.getline(buscador,sizeof(buscador));
			Qr=buscador;
			Qrs.push(Qr);
		}
		int Y=0;
		map<string,char> BTemp=Buscadores;
		for(int j=0;j<Q;j++)
		{
			Qr=Qrs.top();
			Qrs.pop();
			if(BTemp.count(Qr))
			{
				BTemp.erase(Qr);
				if(!BTemp.size())
				{
					Y++;
					BTemp=Buscadores;
					BTemp.erase(Qr);
				}
			}
		}
		out<<"Case #"<<i+1<<": "<<Y<<endl;
	}
	out.close();
	in.close();
}