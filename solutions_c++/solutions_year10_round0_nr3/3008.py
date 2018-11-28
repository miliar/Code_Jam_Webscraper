#include <iostream>
#include <fstream>
#include <cmath>

#include <sstream>



using namespace std;

ifstream ifs ("C-small.in", ifstream::in);
ofstream ofs ("C-small.out", ofstream::out|ofstream::trunc);

long int getnextnumb()
{
	char c[256];
	int n[256], i=0, ndigit=0;
	i=ndigit=0;
	c[0]=ifs.get();
    do
	{
		n[i]=c[i]-'0';
		i++;
		c[i]=ifs.get();
	}
	while ((c[i]!='\n')&&(c[i]!=' ')&&(c[i]!=EOF));
	long int number=0;
	ndigit = --i;
	while (i>=0)
	{
		number+=n[i]*pow(10.0,(ndigit-i));
		i--;
	}
	cout << number;
	return number;
}

unsigned long int calcEuro(long int Rf, long int kf, long int Nf, long int *vecf)
{
	unsigned long int earnings=0;
	long int qn=0,remaining=kf,cont=0;
	for(int i=0;i<Rf;i++)
	{
		remaining=kf;
		cont=0;
		do
		{
			cont++;
			remaining-=vecf[qn];
			if (Nf>1) qn=((++qn)%(Nf));
			else qn=0;
		}while((remaining>=vecf[qn])&&(cont<Nf));
		earnings+=(kf-remaining);
	}
	return earnings;
}

int main(int argc, char *argv[])
{
	
	long int	intres;

	long int T=getnextnumb();

	cout<<endl;
	for(int i=0;i<T;i++)
	{


		long int R=getnextnumb();
		cout<<' ';
		long int k=getnextnumb();
		cout<<' ';
		long int N=getnextnumb();
		cout<<'\n';
		long int *vec=new long int[N];
		for(long int l=0;l<N;l++)
		{
			vec[l]=getnextnumb();
			cout<<' ';
		}
		intres=calcEuro(R,k,N,vec);
		cout<<endl<<intres<<endl;
		ofs.write("Case #",6);


		std::string st;
		std::stringstream outt;
		outt << (i+1);
		st = outt.str();
		ofs.write(st.c_str(),st.length());


		ofs.put(':');
		ofs.put(' ');
		std::string s;
		std::stringstream out;
		out << intres;
		s = out.str();
		ofs.write(s.c_str(),s.length());
		ofs.put('\n');
		delete vec;

	}
	system("pause");
	return 0;
}	