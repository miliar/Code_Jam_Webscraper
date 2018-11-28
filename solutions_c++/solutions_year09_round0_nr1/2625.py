#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <fstream>
using namespace std;

vector<string> data;
int l, d, n;
string nul;

void get_data(ifstream &inp);
int counter(vector<string> vec);
void check(vector<string> &b, vector<char> &c, int i);

int main()
{	
	string st;
	ifstream indata;
	int count, pnt;
	vector<string> bck;
	vector<char> vch;
	vector<string>::iterator it;
	cout << "Name of the file with the data: " << endl;
	cin >> st;
	indata.open(st.c_str());
	if (!indata.is_open())
	{
	cout << "Wrong file!" << endl;
	return 1;
	}
	get_data(indata);
	cout << "Name the file with the output: " << endl;
	cin >> st;
	ofstream out(st.c_str());
	if(!out) {
	cout << "Cannot open file.\n";
	return 1;
	}
	for (int i=0; i<n ;i++)
	{
		bck=data;
		count=0;
		pnt=0;
		indata >> st;
		for (int j=0; j<l ; j++)
		{
			vch.clear();
			if(st[pnt]=='(')
			{
				pnt++;
				while (st[pnt]!=')')
				{
					vch.push_back(st[pnt]);
					pnt++;
				}
				check(bck, vch, j);
				pnt++;
			}
			else
			{
				for(it=bck.begin(); it!=bck.end(); it++)
				{
					if(*it!=" ")
					{
						if (st[pnt]!=(*it)[j])
							*it=nul;
					}
				}
				pnt++;
			}
		}
		out << "Case #" << i+1 << ": " << counter(bck) << endl;
	}
}

void get_data(ifstream &inp)
{
	string st;
	inp >> l;
	inp >> d;
	inp >> n;
	for (int i=0; i< d; i++)
	{
		inp >> st;
		data.push_back(st);
	}
	for(int i=0; i<l+1; i++)
		nul+=' ';
}
int counter(vector<string> vec)
{
	int cc=0;
	vector<string>::iterator it;
	for (it=vec.begin();it!=vec.end(); it++)
		if (*it!=nul)
			cc++;
	return cc;
}

void check(vector<string> &b, vector<char> &c, int i)
{
	vector<string>::iterator it1;
	vector<char>::iterator it2;
	int a;
	for (it1=b.begin(); it1!= b.end(); it1++)
	{
		a=1;
		for (it2=c.begin(); it2!= c.end(); it2++)
		{
			if((*it1)[i]==*it2)
				a=0;
		}
		if (a==1)
			*it1=nul;
	}
}