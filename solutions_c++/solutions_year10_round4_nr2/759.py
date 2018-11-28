#include<iostream>

#include<fstream>


using namespace std;

ifstream in("B.in");
ofstream out("B.out");


int P;
int miss[1024];
int must[1024];
bool played[10][512];
int price[10][512];
int main()
{
	int T;
	in>>T;

	
	for(int c=0;c<T;c++)
	{
		memset(played,false,sizeof(played));
		memset(price,0,sizeof(price));
		in>>P;
		for(int i=0;i<(1<<P);i++)
		{
			in>>miss[i];
			must[i] = P-miss[i];
		}
		for(int i=0;i<P;i++)
		{
			for(int seq=0;seq<(1<<(P-1-i));seq++)
			{
				in>>price[i][seq];
				
			}

		}
		//for small case
		int res = 0;
		for(int i=0;i<(1<<P);i++)
		{
			for(int j=0;j<must[i];j++)
			{

				played[P-1-j][i>>(P-j)] = true;
			

			}
		}
		for(int i=0;i<P;i++)
		{
			for(int j=0;j<512;j++)
				if(played[i][j])
					res+= price[i][j];
			
		}

		
		out<<"Case #"<<c+1<<": "<<res<<endl;
	}
		
	return 0;
}