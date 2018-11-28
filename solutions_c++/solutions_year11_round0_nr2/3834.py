#include <iostream>

// basic file operations
#include <iostream>
#include <fstream>

using namespace std;

void main()
{
	ifstream in ("input9.in");
	ofstream out("output9.in");
	//out.open("output.in");
	int T=0;
	int C=0;
	int D=0;
	int N=0;
	char cCom[4];
	char cOpp[3];
	int Case=0;
	int found=-1;
	int Oflag=0;

	in>>T;
	while (!in.eof())
	{
		Case++;
		Oflag=-1;
		in>>C;
		found=-1;
		for(int i=0;i<C;i++)
			in>>cCom;
		in>>D;
		for(int i=0;i<D;i++)
			in>>cOpp;
		in>>N;
		char* cElems=new char[N];
		in>>cElems;

		bool changed=false;//is there an element changed?

		
		if(D>0)
		{
			Oflag=(cElems[0]==cOpp[0])?0:Oflag;
			Oflag=(cElems[0]==cOpp[1])?1:Oflag;
			if(Oflag>-1) found=0;
		}

		for (int i=1;i<N;i++)
		{
			if(C>0)
			{
				if( (cElems[i]==cCom[0]		&&	cElems[i-1]==cCom[1])
					||
					(cElems[i]==cCom[1]	&&	cElems[i-1]==cCom[0]) )
				{
					//if(cElems[i-1]==cOpp[0]||cElems[i-1]==cOpp[1])
					//	Oflag=-1;
					//if(cElems[i]==cOpp[0]||cElems[i]==cOpp[1])
					//	Oflag=-1;

					cElems[i]=cCom[2];
					cElems[i-1]='-';
					if(found==(i-1)||found==i) {found=-1;Oflag=-1;}
					
					changed=true;
				}
			}				
			if(D>0)
			{
				if(found>-1)
				{
					if(cElems[i]==cOpp[!Oflag])
					{
						for (int j=0;j<=i;j++)
							cElems[j]='-';
						Oflag=-1;//finish deleting
						found=-1;
						continue;
					}
				}
				else
				{
					Oflag=(cElems[i]==cOpp[0])?0:Oflag;
					Oflag=(cElems[i]==cOpp[1])?1:Oflag;
					if(Oflag>-1) found=i;
				}
			}
			if(changed)
			{
				i=i-1;
				changed = false;
			}
		}

		bool f=false;
		out<<"Case #"<<Case<<": [";
		for(int i=0;i<N;i++)
		{
			if(cElems[i]!='-')
			{
				if (f==false)
				{
					out<<cElems[i];
					f=true;
				}
				else
					out<<", "<<cElems[i];
			}
		}
		out<<']'<<endl;
	}
	//delete cOpp;
	
	in.close();
	out.close();
}
