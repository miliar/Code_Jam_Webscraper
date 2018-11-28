#include<iostream>
#include<fstream>
using namespace std;

const int MAXN=10+1,MAXC=1+1,MAXD=1+1;
int T,N,C,D,anp;
char cstr[MAXC][3];
char dstr[MAXD][2];
char ans[MAXN];

int main()
{
	ifstream in ("B.in");
	ofstream out ("B.out");
	in>>T;
	for(int t=0;t<T;t++)
	{
		anp=0;
		in>>C;
		for(int i=0;i<C;i++)
			in>>cstr[i];
		in>>D;		
		for(int i=0;i<D;i++)
			in>>dstr[i];
		in>>N;
		for(int i=0;i<N;i++)
		{
			in>>ans[anp];
			anp++;
			if(anp>1)
			{
				bool key=true;
				while(key)
				{
					key=false;	
					for(int j=0;j<C;j++)
						if(((cstr[j][0]==ans[anp-1])&&(cstr[j][1]==ans[anp-2]))
						 ||((cstr[j][1]==ans[anp-1])&&(cstr[j][0]==ans[anp-2])))
						{
							ans[anp-2]=cstr[j][2];
							anp--;
							key=true;
							break;
						}
				}
				for(int j=0;j<D&&!key;j++)
					for(int jj=0;jj<anp-1;jj++)
						if(((dstr[j][0]==ans[anp-1])&&(dstr[j][1]==ans[jj]))
						 ||((dstr[j][1]==ans[anp-1])&&(dstr[j][0]==ans[jj])))
						{
							anp=0;
							key=true;
							break;				
						}
			}
		}
		out<<"Case #"<<t+1<<": [";
		for(int i=0;i<anp;i++)
			if(i!=anp-1)
				out<<ans[i]<<", ";
			else
				out<<ans[i];
		out<<"]"<<endl;
						
	}
	return 0;
}
