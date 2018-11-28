#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iostream>

using namespace std;

int Traducir(string Hora)
{
	stringstream ss;
	ss<<Hora;
	int hora,min;
	ss>>hora;
	ss.get();
	ss>>min;
	return (hora*60)+min;
}

bool EsMenor(pair<int,bool> a, pair<int,bool> b)
{
	if(a.first<b.first)
		return true;
	else if(a.first==b.first)
	{
		if(a.second==b.second)
			return false;
		else
			return b.second;
	}
	else
		return false;
}

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
	int N;
	in>>N;
	for(int i=0;i<N;i++)
	{
		int T,NA,NB;
		in>>T>>NA>>NB;
		string hora;
		vector<pair<int,bool>> SchA,SchB;
		for(int j=0;j<NA;j++)
		{
			in>>hora;
			SchA.push_back(pair<int,bool>(Traducir(hora),true));
			in>>hora;
			SchB.push_back(pair<int,bool>(Traducir(hora)+T,false));
		}
		for(int j=0;j<NB;j++)
		{
			in>>hora;
			SchB.push_back(pair<int,bool>(Traducir(hora),true));
			in>>hora;
			SchA.push_back(pair<int,bool>(Traducir(hora)+T,false));
		}
		sort(SchA.begin(),SchA.end(),EsMenor);
		sort(SchB.begin(),SchB.end(),EsMenor);
		int A=0,B=0,listo=0;
		for(int j=0;j<SchA.size();j++)
		{
			if(SchA[j].second)
			{
				if(listo<1)
					A++;
				else
					listo--;
			}
			else
				listo++;
		}
		listo=0;
		for(int j=0;j<SchB.size();j++)
		{
			if(SchB[j].second)
			{
				if(listo<1)
					B++;
				else
					listo--;
			}
			else
				listo++;
		}
		out<<"Case #"<<i+1<<": "<<A<<' '<<B<<endl;
	}
	out.close();
	in.close();
}