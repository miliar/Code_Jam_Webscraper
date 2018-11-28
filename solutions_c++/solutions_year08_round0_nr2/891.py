#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
#include<vector>
#include<stack>
using namespace std;
struct Time
{
	int start;
	int end;
	int train;
	Time()
	{
		train=-1;
	}
};
int GetTime(string time)
{
	string::size_type pos=time.find_first_of(':');
	string tmp=string(time.begin(),time.begin()+pos);
	int Re=atoi(tmp.c_str())*60;
	tmp=string(time.begin()+pos+1,time.end());
	Re+=atoi(tmp.c_str());
	return Re;
}
void MakeTime(Time& ptime, string word)
{
	ptime.train=-1;//no train;
	string::size_type pos=word.find_first_of(' ');
	string tmp=string(word.begin(),word.begin()+pos);
	ptime.start=GetTime(tmp);
	tmp=string(word.begin()+pos+1,word.end());
	ptime.end=GetTime(tmp);
}
int main(){
	//string filein("test.txt");
	//string filein("A-large.in");
	//string filein("A-small-attempt0.in");
	string filein("B-large.in");
	//string filein("B-small-attempt0.in");
	string fileout("AnsBlarge.txt");
	ifstream fin;
	fin.open(filein.c_str());
	ofstream fout;
	fout.open(fileout.c_str());
	string word;
	int Case;
	stringstream strint;
	getline(fin,word,'\n');
	strint<<word;
	strint>>Case;
	cout<<"TotalCase: "<<Case<<endl;
	for(int i=1;i<=Case;i++)
	{
		fout<<"Case #"<<i<<": ";
		int T;
		getline(fin,word,'\n');
		strint.clear();
		strint<<word;
		strint>>T;
		int Na,Nb;
		getline(fin,word,'\n');
		strint.clear();
		strint<<word;
		strint>>Na>>Nb;
		vector<Time>A;
		vector<Time>B;
		for(int j=0;j<Na;j++)
		{
			getline(fin,word,'\n');
			Time tmp;
			MakeTime(tmp,word);
			A.push_back(tmp);
		}
		for(int j=0;j<Nb;j++)
		{
			getline(fin,word,'\n');
			Time tmp;
			MakeTime(tmp,word);
			B.push_back(tmp);
		}
		int AnsA=0;
		int AnsB=0;
		stack<int>Ta;
		stack<int>Tb;
		for(int j=999;j>=1;j-=2)
			Ta.push(j);
		for(int j=1000;j>=0;j-=2)
			Tb.push(j);
		for(int j=0;j<=23*60+59;j++)
		{
			for(int k=0;k<Na;k++)
			{
				if(j==A[k].end+T)
				{
					Tb.push(A[k].train);
				}
			}
			for(int k=0;k<Nb;k++)
			{
				if(j==B[k].end+T)
				{
					Ta.push(B[k].train);
				}
			}
			for(int k=0;k<Na;k++)
			{
				if(j==A[k].start)
				{
						int Train=Ta.top();
						Ta.pop();
						if(Train%2==1)
						{
							if((Train+1)/2>AnsA)
								AnsA=(Train+1)/2;
						}
						A[k].train=Train;
						continue;
				}
			}
			for(int k=0;k<Nb;k++)
			{
			
				if(j==B[k].start)
				{
						int Train=Tb.top();
						Tb.pop();
						if(Train%2==0)
						{
							if(Train/2+1>AnsB)
								AnsB=Train/2+1;
						}
						B[k].train=Train;
						
				}
			
			}
		}
		fout<<AnsA<<' '<<AnsB<<endl;
	}
	return 0;
}