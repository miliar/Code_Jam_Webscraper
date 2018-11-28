#include <iostream>

// basic file operations
#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>


using namespace std;
struct RPI
{
	double wp;
	double owp;
	double oowp;
};
void main()
{
	ifstream in ("inputL.in");
	ofstream out("outputL.out");
	
	double T;
	double Case=0;
	
	in>>T;
	char ch[100][100];
	RPI r[100];
	for(Case = 1;Case<=T;Case++)
	{
		out<<"Case #"<<Case<<": "<<endl;

		int N;
		in>>N;
		
		//RPI *r = new RPI[N];

		for (int i=0;i<N;i++)
		{
			for(int j =0;j<N;j++)
			{
				in>>ch[i][j];
			}
		}

		//wp
		for(int i=0;i<N;i++)
		{
			int count =0;
			double avr = 0.0;
			for(int j=0;j<N;j++)
			{
				
				if(ch[i][j]=='.') 
					continue;
				
				avr+=(double)(ch[i][j]-48);
				count++;
				
			}
			if (count==0)
				r[i].wp=0.0;
			else
				r[i].wp = avr/(double)count;
		}
		//owp
		for(int i=0;i<N;i++)
		{
			int count =0;
			double avr = 0.0;
			for(int k=0;k<N;k++)
			{
				
				if(ch[k][i]=='.')
					continue;
				int c=0;
				double a=0.0;
				
				for(int j = 0;j<N;j++)
				{
					if(ch[k][j]=='.'||j==i) continue;
					c++;
					a+=(double)(ch[k][j]-48);
				}

				if(c==0) 
					avr==0.0;
				else
				{
					avr+=a/(double)c;
					count++;
				}
			}
			if(count==0)
				r[i].owp=0.0;
			else
				r[i].owp=avr/(double)count;
		}
		//oowp
		for(int i=0;i<N;i++)
		{
			int count =0;
			double avr = 0.0;

			for(int j=0;j<N;j++)
			{
				if(ch[i][j]=='.') continue;
				avr+=r[j].owp;
				count++;
			}
			if(count==0) 
				r[i].oowp = 0.0;
			else
				r[i].oowp = avr/(double)count;
		}

		//print
		for(int i=0;i<N;i++)
		{
			out<<setprecision(12)<<(0.25*r[i].wp+0.5*r[i].owp+0.25*r[i].oowp)<<endl;
		}
	}
	in.close();
	out.close();
}
