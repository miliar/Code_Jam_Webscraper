#include <iostream>
#include<fstream>
using namespace std;

class Basin{
private:
	int H;
	int W;
public:
	static ofstream fout;
	char ctu;
	char **cpp;
	int **ipp;
	Basin(int h,int w);
	~Basin();
	void Evaluate(int x,int y);
	void Evaluate(int x,int y,char c);
	void Output(int i);
};

int main(int argc,char* argv[])
{
	ifstream fin("C:/watersheds/B-large.in");
	int N = 0;
	fin>>N;

	for(int i = 0; i < N; ++i)
	{
		int H = 0, W = 0;
		fin>>H>>W;
		
		Basin B(H,W);

		for(int j = 0; j < H; ++j)
		{
			for(int k = 0; k < W; ++k)
			{
				fin>>(B.ipp)[j][k];				
			}
		}
		
		B.Evaluate(0,0);

		for(int j = 0; j < H; ++j)
		{
			for(int k = 0; k < W; ++k)
			{
				if(B.cpp[j][k]=='*')
				{
					++B.ctu;
					B.cpp[j][k]=B.ctu;
					B.Evaluate(j,k);
				}
			}
		}

		B.Output(i+1);
		
	}

	return 0;
}
ofstream Basin::fout("C:/watersheds/B-large.out");
Basin::Basin(int h, int w)
{
	H = h;
	W = w;
	ctu = 'a';

	ipp  = new int*[H];
	cpp = new char*[H];
	for(int j = 0; j < H; ++j)
	{
		ipp[j] = new int[W];
		cpp[j] = new char[W];

		for(int k = 0; k < W; ++k)
		{
			cpp[j][k] = '*';
		}
	}
	cpp[0][0]  = ctu;
}

Basin::~Basin()
{
	for(int j = 0; j < H; ++j)
		{
			cpp[j] = 0;
			delete []cpp[j];
			ipp[j] = 0;
			delete []ipp[j];
		}
		delete []cpp;
		delete []ipp;
}

void Basin::Output(int i)
{
	fout<<"Case #"<<i<<": "<<endl;
	for(int j = 0; j < H; ++j)
	{
		for(int k = 0; k < W; ++k)
		{
			fout<<cpp[j][k]<<" ";
		}
		fout<<endl;
	}
}

void Basin::Evaluate(int x,int y)
{
	if(x<0 || y<0)
		return;

	int m = 0 ,r = 0, s = 0, val = ipp[x][y];

	if(x!=0)
	{
		if(ipp[x-1][y]<val)
		{
			val = ipp[x-1][y]; 
			r = x-1;
			s = y; 
		}
		else if(ipp[x-1][y]>ipp[x][y])
		{
			m|=1;
		}
	}

	if(y!=0)
	{
		if(ipp[x][y-1]<val)
		{
			val = ipp[x][y-1]; 
			r = x;
			s = y-1;
		}
		else if(ipp[x][y-1]>ipp[x][y])
		{
			m|=2;
		}
	}

	if(y!=W-1)
	{
		if(ipp[x][y+1]<val)
		{
			val = ipp[x][y+1]; 
			r = x;
			s = y+1;
		}
		else if(ipp[x][y+1]>ipp[x][y])
		{
			m|=4;
		}
	}

	if(x!=H-1)
	{
		if(ipp[x+1][y]<val)
		{
			val = ipp[x+1][y]; 
			r = x+1;
			s = y;
		}
		else if(ipp[x+1][y]>ipp[x][y])
		{
			m|=8;
		}
	}

	if(cpp[r][s]=='*')
	{
		cpp[r][s] = cpp[x][y];
		Evaluate(r,s);
	}

	if((m&1)==1)
	{
		if(cpp[x-1][y]=='*')
		{
			Evaluate(x-1,y,cpp[x][y]);
		}
	}
	if((m&2)==2)
	{
		if(cpp[x][y-1]=='*')
		{
			Evaluate(x,y-1,cpp[x][y]);
		}
	}
	if((m&4)==4)
	{
		if(cpp[x][y+1]=='*')
		{
			Evaluate(x,y+1,cpp[x][y]);
		}
	}
	if((m&8)==8)
	{
		if(cpp[x+1][y]=='*')
		{
			Evaluate(x+1,y,cpp[x][y]);
		}
	}	
}
void Basin::Evaluate(int x,int y,char c)
{
	if(x<0 || y<0)
		return;
	int m = 0 ,r = 0, s = 0, val = ipp[x][y];

	if(x!=0)
	{
		if(ipp[x-1][y]<val)
		{
			val = ipp[x-1][y]; 
			r = x-1;
			s = y; 
		}
		else if(ipp[x-1][y]>ipp[x][y])
		{
			m|=1;
		}
	}

	if(y!=0)
	{
		if(ipp[x][y-1]<val)
		{
			val = ipp[x][y-1]; 
			r = x;
			s = y-1;
		}
		else if(ipp[x][y-1]>ipp[x][y])
		{
			m|=2;
		}
	}

	if(y!=W-1)
	{
		if(ipp[x][y+1]<val)
		{
			val = ipp[x][y+1]; 
			r = x;
			s = y+1;
		}
		else if(ipp[x][y+1]>ipp[x][y])
		{
			m|=4;
		}
	}

	if(x!=H-1)
	{
		if(ipp[x+1][y]<val)
		{
			val = ipp[x+1][y]; 
			r = x+1;
			s = y;
		}
		else if(ipp[x+1][y]>ipp[x][y])
		{
			m|=8;
		}
	}

	if(cpp[r][s]!='*')
	{
		cpp[x][y] = cpp[r][s];
	}

	if(cpp[x][y]!='*')
	{
		if((m&1)==1)
		{
			if(cpp[x-1][y]=='*')
			{
			Evaluate(x-1,y,cpp[x][y]);
			}
		}
		if((m&2)==2)
		{
			if(cpp[x][y-1]=='*')
			{
				Evaluate(x,y-1,cpp[x][y]);
			}
		}
		if((m&4)==4)
		{
			if(cpp[x][y+1]=='*')
			{
				Evaluate(x,y+1,cpp[x][y]);
			}
		}
		if((m&8)==8)
		{
			if(cpp[x+1][y]=='*')
			{
				Evaluate(x+1,y,cpp[x][y]);
			}
		}
	}
}