#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

int switchnumber(int s,int q,vector <string> engine,vector <string> query);

int num(string eng,vector <string> engine);


void main()
{
	int n,s,q,number=0;
	string eng,que,space;
	vector <string> engine;
	vector <string> query;
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	in>>n;

	for (int i=0;i<n;i++)
	{
		vector <string> engine;
		vector <string> query;
		number=0;
		in>>s;
		getline(in,space);

		for (int j=0;j<s;j++)
		{
			getline(in,eng);
			engine.push_back(eng);
		}

		in>>q;
		if (q>1)
		{
		getline(in,space);
		for (int k=0;k<q;k++)
		{
			getline(in,que);
			query.push_back(que);
		}
		}

		if (q>1) number=switchnumber(s,q,engine,query);
		out<<"Case #"<<i+1<<": "<<number<<endl;
	}
}

int switchnumber(int s,int q,vector <string> engine,vector <string> query)
{
	int time=0;
	int count=s;
	int aim=0,i=0;

	vector <int> eng;

	for (int ti=0;ti<s;ti++) eng.push_back(aim);

		do
		{
			//cout<<"i:"<<i<<" count:"<<count<<" aim:"<<aim<<" query"<<i<<":"<<query[i]<<endl;
		if (count==1 && eng[num(query[i],engine)]==aim) 
		{
			count=s;
			time++;
			eng[num(query[i],engine)]=abs(1-aim);
			aim=abs(1-aim);
		}
		if (eng[num(query[i],engine)]==aim) {eng[num(query[i],engine)]=abs(1-aim);count--;}
		i++;
		}
		while (i<q);
return time;
}

int num(string eng,vector <string> engine)
{
	int number=0;
	for (int i=0;i<engine.size();i++)
	{
		if (eng==engine[i]) {number=i;break;}
	}
	return number;
}
