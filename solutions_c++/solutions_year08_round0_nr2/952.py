#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
#include<vector>

using namespace std;

int get_dep(string x);
int get_arr(string x);
void startnum();
void sortab();
void sortba();

int na,nb,as,bs,T;
vector<int> ab_dep,ab_arr,ba_dep,ba_arr;

int main()
{
	int N;
	string stn;
	cout<<"Input the filename:"<<endl;
		//从文件输入
	string filename;
	cin>>filename;
	ifstream infile(filename.c_str());

	if(!infile)
	{
		cerr<<"error: enable to open input file: "
			<<filename<<endl;
		exit(0);
	}

	getline(infile, stn);
	stringstream input_string(stn);
	input_string>>N;

	ofstream outfile("outl.txt");

	for(int i=0;i<N;i++)
	{
		//T
		getline(infile, stn);
		istringstream T_string(stn);
		T_string>>T;

		//NA NB
		getline(infile, stn);
		istringstream N_string(stn);
		N_string>>na>>nb;

		as=na;
		bs=nb;
		ab_dep.resize(na);
		ab_arr.resize(na);
		ba_dep.resize(nb);
		ba_arr.resize(nb);

		//timetable
		for(int k=0;k<na;k++)
		{
			getline(infile, stn);
			ab_dep[k]=get_dep(stn);
			ab_arr[k]=get_arr(stn);
		}
		for(int k=0;k<nb;k++)
		{
			getline(infile, stn);
			ba_dep[k]=get_dep(stn);
			ba_arr[k]=get_arr(stn);
		}

		startnum();
		
		ab_dep.clear();
		ba_dep.clear();
		ab_arr.clear();
		ba_arr.clear();

		outfile<<"Case #"<<i+1<<": "<<as<<" "<<bs<<"\n";
		cout<<"Case #"<<i+1<<": "<<as<<" "<<bs<<endl;
	}

	outfile.close();

	return 0;
}

int get_dep(string x)
{
	return ((int)x[0]-48)*600+((int)x[1]-48)*60+((int)x[3]-48)*10+((int)x[4]-48);
}

int get_arr(string x)
{
	return ((int)x[6]-48)*600+((int)x[7]-48)*60+((int)x[9]-48)*10+((int)x[10]-48)+T;
}

void startnum()
{
	sortab();
	sortba();
	vector<bool> flag;
	flag.resize(nb);
	//for(int i=0;i<nb;i++)
	//	flag[i]=false;

	for(int i=0;i<na;i++)
	{
		for(int j=0;j<nb;j++)
		{
			if(flag[j]==false && ab_dep[i]>=ba_arr[j])
			{
				as--;
				flag[j]=true;
				break;
			}
		}
	}
	flag.clear();

	flag.resize(na);
	//for(int i=0;i<na;i++)
	//	flag[i]=false;

	for(int i=0;i<nb;i++)
	{
		for(int j=0;j<na;j++)
		{
			if(flag[j]==false && ba_dep[i]>=ab_arr[j])
			{
				bs--;
				flag[j]=true;
				break;
			}
		}
	}
}

void sortab()
{
	int temp;
	size_t pos;
	for(size_t i=0;i<ab_arr.size();i++)
	{
		temp=ab_arr[i];
		pos=i;
		for(size_t j=i+1;j<ab_arr.size();j++)
		{
			if(ab_arr[j]>temp)
			{
				temp=ab_arr[j];
				pos=j;
			}
		}
		ab_arr[pos]=ab_arr[i];
		ab_arr[i]=temp;
	}
}

void sortba()
{
	int temp;
	size_t pos;
	for(size_t i=0;i<ba_arr.size();i++)
	{
		temp=ba_arr[i];
		pos=i;
		for(size_t j=i+1;j<ba_arr.size();j++)
		{
			if(ba_arr[j]>temp)
			{
				temp=ba_arr[j];
				pos=j;
			}
		}
		ba_arr[pos]=ba_arr[i];
		ba_arr[i]=temp;
	}
}
