#include<fstream>
#include<set>
#define rep(I,N) for(int I=0;I<N;I++)
using namespace std;
struct pa
{
	char a,b;
	bool operator<(pa);
};
bool pa::operator<(pa q1)
{
	return this->a<q1.a;
}
int main()
{
	ifstream cin("in.txt");
	ofstream cout("out.txt");
	int n;
	cin>>n;
	char a[31][120]={0};
	char b[31][120]={0};
	char w[12];
	cin.getline(w,3);
	rep(i,n)
		cin.getline(a[i],150);
	int t;
	rep(i,n)
	{
		t=strlen(a[i]);
		rep(j,t)
		{
			switch(a[i][j])
			{
			case'a': b[i][j]='y'; break;
			case'b': b[i][j]='h'; break;
			case'c': b[i][j]='e'; break;
			case'd': b[i][j]='s'; break;
			case'e': b[i][j]='o'; break;
			case'f': b[i][j]='c'; break;
			case'g': b[i][j]='v'; break;
			case'h': b[i][j]='x'; break;
			case'i': b[i][j]='d'; break;
			case'j': b[i][j]='u'; break;
			case'k': b[i][j]='i'; break;
			case'l': b[i][j]='g'; break;
			case'm': b[i][j]='l'; break;
			case'n': b[i][j]='b'; break;
			case'o': b[i][j]='k'; break;
			case'p': b[i][j]='r'; break;
			case'q': b[i][j]='z'; break;
			case'r': b[i][j]='t'; break;
			case's': b[i][j]='n'; break;
			case't': b[i][j]='w'; break;
			case'u': b[i][j]='j'; break;
			case'v': b[i][j]='p'; break;
			case'w': b[i][j]='f'; break;
			case'x': b[i][j]='m'; break;
			case'y': b[i][j]='a'; break;
			case'z': b[i][j]='q'; break;
			case' ': b[i][j]=' '; break;
		}
	}
	}
	rep(i,n)
	{
		cout<<"Case #"<<i+1<<": "<<b[i]<<'\n';
	}
}