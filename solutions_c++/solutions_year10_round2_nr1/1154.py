#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

struct Item
{
	string str;
	vector<Item *> ptr;
	Item(){}
};

int main()
{
	int cas, N, M, res;
	Item root;
	ifstream fin("t.in");
	ofstream fout("t.out");

	fin>>cas;
	for(int ii=1; ii<=cas; ii++)
	{
		res = 0;
		fin>>N>>M;
		root.ptr.clear();
		for(int i=0; i<N; i++)
		{
			char tmp;
			string t = "";
			Item *q, *p = &root;

			while( fin.get() != '/' )
				;
			while( 1 )
			{
				tmp = fin.get();
				if( tmp=='/' || tmp=='\n' )
				{
					bool f = false;
					for(int j=0; j<p->ptr.size(); j++)
						if( p->ptr[j]->str == t )
						{
							p = p->ptr[j];
							f = true;
							break;
						}
					if( f == false )
					{
						//cout<<t<<endl;
						q = new Item();
						q->str = t;
						p->ptr.push_back(q);
						p = q;
					}
					if( tmp == '\n' )
						break;
					t = "";
				}
				else
					t += tmp;
			}
		}

		//cout<<root.ptr.size()<<endl;
		for(int i=0; i<M; i++)
		{
			char tmp;
			string t = "";
			Item *q, *p = &root;

			while( fin.get() != '/' )
				;
			while( 1 )
			{
				tmp = fin.get();
				if( tmp=='/' || tmp=='\n' )
				{
					bool f = false;
					for(int j=0; j<p->ptr.size(); j++)
						if( p->ptr[j]->str == t )
						{
							p = p->ptr[j];
							f = true;
							break;
						}
					if( f == false )
					{
						res++;
						//cout<<t<<endl;
						q = new Item();
						q->str = t;
						p->ptr.push_back(q);
						p = q;
					}
					if( tmp == '\n' )
						break;
					t = "";
				}
				else
					t += tmp;
			}
		}
		fout<<"Case #"<<ii<<": "<<res<<endl;
	}

	return 0;
}
