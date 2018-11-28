#include<fstream>
#include<string>
#include<cstdlib>
#include<cstring>
#include<iostream>
using namespace std;

const int NMAX=100;
void init(int m[][NMAX])
{
	for(int i=0;i<NMAX;i++)
		for(int j=0;j<NMAX;j++)
			m[i][j]=-1;
}
	
int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	int combine[NMAX][NMAX],opose[NMAX][NMAX];

	int t;
	string line;
	getline(in,line);
	t=atoi(line.c_str());

	for(int i=0;i<t;i++)
	{
		init(combine);
		memset(opose,0,sizeof(opose));
		getline(in,line);
		string s1="";

		int ind=0;
		while(line[ind]!=' ')
		{
			s1+=line[ind];
			++ind;
		}
		int C=atoi(s1.c_str());
		++ind;
		for(int j=0;j<C;j++)
		{
			s1="";
			while(line[ind]!=' ')
			{
				s1+=line[ind];
				++ind;
			}
			++ind;
			combine[s1[0]-'A'][s1[1]-'A']=s1[2]-'A';
			combine[s1[1]-'A'][s1[0]-'A']=s1[2]-'A';
		}
		s1="";
		while(line[ind]!=' ')
		{
			s1+=line[ind];
			++ind;
		}
		++ind;
		int D=atoi(s1.c_str());
		for(int j=0;j<D;j++)
		{
			s1="";
			while(line[ind]!=' ')
			{
				s1+=line[ind];
				++ind;
			}
			++ind;
			opose[s1[0]-'A'][s1[1]-'A']=1;
			opose[s1[1]-'A'][s1[0]-'A']=1;
		}
		s1="";	
		while(line[ind]!=' ')
		{
			s1+=line[ind];
			++ind;
		}
		++ind;
		int N=atoi(s1.c_str());
		s1="";
		for(int j=0;j<N;j++)
			s1+=line[ind++];
		

		//now solve the test case
		int v[NMAX],index=-1;
		for(int j=0;j<(int) s1.size();j++)
		{
			int code=s1[j]-'A';
			if(index>=0 && combine[v[index]][code]!=-1)
				v[index]=combine[v[index]][code];
			else
			{
				int found=0;
				for(int k=0;k<=index;k++)
				{
					if(opose[code][v[k]])
					{
						index=-1;
						found=1;
						break;
					}
				}
				if(!found)
					v[++index]=code;
			}
		}
		string rez="[";
		for(int j=0;j<index;j++)
		{
			rez+= v[j]+'A';
			rez+=", ";
		}
		if(index>=0)
			rez+=v[index]+'A';
		rez+=']';
		out<<"Case #"<<i+1<<": "<<rez<<"\n";
	}
	in.close();
	out.close();
}

