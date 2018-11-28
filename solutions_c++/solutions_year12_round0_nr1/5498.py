#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<vector>

using namespace std;

vector<string> VS;

void draw(char &c)
{
	switch( c )
	{
	case'a':
		cout<<'y';
		break;
	case'b':
		cout<<'h';
		break;
	case'c':
		cout<<'e';
		break;
	case'd':
		cout<<'s';
		break;
	case'e':
		cout<<'o';
		break;
	case'f':
		cout<<'c';
		break;
	case'g':
		cout<<'v';
		break;
	case'h':
		cout<<'x';
		break;
	case'i':
		cout<<'d';
		break;
	case'j':
		cout<<'u';
		break;
	case'k':
		cout<<'i';
		break;
	case'l':
		cout<<'g';
		break;
	case'm':
		cout<<'l';
		break;
	case'n':
		cout<<'b';
		break;
	case'o':
		cout<<'k';
		break;
	case'p':
		cout<<'r';
		break;
	case'q':
		cout<<'z';// l 
		break;
	case'r':
		cout<<'t';
		break;
	case's':
		cout<<'n';
		break;
	case't':
		cout<<'w';
		break;
	case'u':
		cout<<'j';
		break;
	case'v':
		cout<<'p';
		break;
	case'w':
		cout<<'f';
		break;
	case'x':
		cout<<'m';
		break;
	case'y':
		cout<<'a';
		break;
	case'z':
		cout<<'q';//
		break;
	}
}

void go(int index)
{
	int t = VS[index].size();
	for(int i = 0;i<t;++i)
	{
		draw(VS[index][i]);
	}
}

void go()
{
	int t= VS.size();
	for(int i=0;i<t;++i)
	{
		go(i);
		if ( i!= (t-1) )
		{
			cout<<" ";
		}
	}
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	string s;
	int n;
	getline(cin,s);
	stringstream in(s);in>>n;
	int caso = 1;
	while(n--)
	{
		getline(cin,s);
		stringstream en(s);
		VS.clear();
		string temp;
		while(en>>temp)
		{
			VS.push_back(temp);
		}
		if(caso >1)cout<<endl;
		cout<<"Case #"<<caso++<<": ";
		go();
	}
}