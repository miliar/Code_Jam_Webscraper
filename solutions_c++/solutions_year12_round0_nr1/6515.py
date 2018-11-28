#include "iostream"
#include "cstdio"
#include "cstring"
#include "cstdlib"
#include "cctype"
#include "string"
#include "algorithm"
#include "map"
#include "queue"
#include "vector"
#include "limits"
#include "fstream"
#define MAX 2000000000
#define MIN -2000000000
using namespace std;


int main()
{
    ofstream fout("out.txt");
	char ar[500], c;
	ar['a']='y'; ar['b']='h'; ar['c']='e';  ar['d']='s';  ar['e']='o';  ar['f']='c';  ar['g']='v';
	 ar['h']='x';  ar['i']='d';  ar['j']='u';
	 ar['k']='i';  ar['l']='g';  ar['m']='l';  ar['n']='b';  ar['o']='k';  ar['p']='r';
	 ar['q']='z';  ar['r']='t';  ar['s']='n';  ar['t']='w';
	  ar['u']='j';  ar['v']='p';  ar['w']='f';  ar['x']='m';  ar['y']='a';  ar['z']='q';

	int tcase, bol=1, cas=1;
	cin>>tcase;
	getchar();
	while(tcase--)
	{
	    bol=1;
		while((c=getchar())!=EOF)
		{
			if(c=='\n')
				break;
			if(c>='a' && c<='z')
			{
			    if(bol==1)
			    {
                    //cout<<"Case #"<<cas++<<": ";
                    fout<<"Case #"<<cas++<<": ";
			    }
				//cout<<ar[c];
				fout<<ar[c];
				bol=0;
			}
			else
            {
				//cout<<c;
				fout<<c;
				bol=0;
            }
		}
		//cout<<endl;
		fout<<endl;
	}

    return 0;
}
