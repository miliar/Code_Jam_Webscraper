#include <string>
#include <vector>
#include <map>
#include <math.h>
#include <algorithm>
#include <iostream>
#include <sstream>

using namespace std;

void func(int casen);

int main()
{
	int cases;
	cin >> cases;

	for(int i=0;i<cases;i++)
	  func(i+1);	
}

map<string, bool> dirs;

int adddirs(string d)
{
//	cout << "addirs: " << d << endl;

	if(d.length()<2)
		return 0;

	int res=0;


	int pos=d.length()-1;
	if(d[pos]=='/')
	{
		d = d.substr(0, pos);
		pos--;
	}
	
	if(dirs[d])
		return 0;

	while(pos>0 && d[pos]!='/')
		pos--;

//	cout << "pos: " << pos << endl;
	res = adddirs(d.substr(0, pos));
//	cout << "res: " << res << endl;

	res++;
	dirs[d] = true;

//	cout << "res: " << res << endl;

	return res;
}

void func(int casen)
{
	dirs.clear();

	int c1, c2, i, res;
	char d[500];
	
	cin >> c1 >> c2;
	cin.getline(d, 500);
	for(i=0;i<c1;i++)
	{
		cin.getline(d, 500);
		adddirs(d);
	}

	res = 0;
	for(i=0;i<c2;i++)
	{
		cin.getline(d, 500);
		res+=adddirs(d);
//		cout << d << "---" << res << endl;
	}


    cout << "Case #" << casen << ": " << res << endl;
}