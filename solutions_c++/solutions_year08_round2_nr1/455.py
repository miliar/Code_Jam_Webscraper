#include <stdio.h>
#include <vector>

using namespace std;

class point
{
public:
	unsigned long X;
	unsigned long Y;
	point(unsigned long a, unsigned long b):X(a),Y(b){}
	point operator+(point m){return point(X+m.X,Y+m.Y);}
	bool divisible(){return (X%3==0)&&(Y%3==0);}
};


vector<point> p;
void print_trees(unsigned long n,unsigned long A,unsigned long B,unsigned long C,unsigned long D,unsigned long x0,unsigned long y0,unsigned long M)
{
	unsigned int X=x0,Y=y0;
//	printf("%lu %lu\n",X,Y);
	p.push_back(point(X,Y));

	for(unsigned long i=0;i<n-1;i++)
	{
		X=(A*X + B)%M;
		Y=(C*Y + D)%M;
		//printf("%lu %lu\n",X,Y);
		p.push_back(point(X,Y));
	}
}

int main(int argc,char* argv[])
{
	FILE *f=fopen(argv[1],"r");
	int cases;
	fscanf(f,"%u\n",&cases);
	for(int l=0;l<cases;l++)
	{
		p.clear();
		unsigned long n, A, B, C, D,  x0, y0, M;
		fscanf(f,"%lu %lu %lu %lu %lu %lu %lu %lu\n",&n,&A,&B,&C,&D,&x0,&y0,&M);

		//print_trees(4,10,7,1,2,0,1,20);
		//print_trees(6, 2, 0, 2, 1, 1,2,11);
		print_trees(n,A,B,C,D,x0,y0,M);
		unsigned long ret=0;
		for(int j=0;j<n;j++)
		{
			for(int i=j;i<n;i++)
			{
				if(i==j)
					continue;
				for(int k=i;k<n;k++)
				{
					if(k==i || k==j)
						continue;
					point center=p[i]+p[j]+p[k];
					//printf("%lu %lu\n",center.X,center.Y);

					if(center.divisible())
						ret++;
				}
			}
		}
		printf("Case #%u: %lu\n",l+1,ret);
	};
	return 0;
}
