#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

ifstream ifs ("A-small.in", ifstream::in);
ofstream ofs ("A-small.out", ofstream::out|ofstream::trunc);

char temp=0;

int getNextNumb()
{
	char c[16];
	int i=0;
	c[0]=ifs.get();
    do
	{
		i++;
		c[i]=ifs.get();
	}
	while ((c[i]!='\n')&&(c[i]!=' ')&&(c[i]!=EOF));
	int number=0;
	std::string conv(c,i);
	std::istringstream ss( conv );
	ss >> number;
	return number;
}

int getTab(char tabTemp[], int Nt)
{
	for(int i=0;i<Nt;i++)
	{
		for(int j=0;j<Nt;j++) tabTemp[i*Nt+j]=ifs.get();
		temp=ifs.get();
		if ((temp!='\n')&&(temp!=EOF)) return 1;
	}
	return 0;
}

int rotateTab(char tabTemp[], int Nt)
{
	for(int j=0;j<(Nt-1);j++)
	{
		for(int i=(Nt*Nt-2);i>=0;i--)
		{
			if ((tabTemp[i+1]=='.')&&((i+1)%Nt)) {tabTemp[i+1]=tabTemp[i]; tabTemp[i]='.';}
		}
	}
	return 0;
}

int rowLeft(char tab[],int j,char c,int Ktt)
{
	for(int i=1;i<Ktt;i++) if(tab[j-i]!=c) return 0;
	return 1;
}

int colUp(char tab[],int j,char c,int Ktt,int Ntt)
{
	for(int i=1;i<Ktt;i++) if(tab[j-Ntt*i]!=c) return 0;
	return 1;
}

int diaLD(char tab[],int j,char c,int Ktt,int Ntt)
{
	for(int i=1;i<Ktt;i++) if(tab[j+Ntt*i-i]!=c) return 0;
	return 1;
}

int diaLU(char tab[],int j,char c,int Ktt,int Ntt)
{
	for(int i=1;i<Ktt;i++) if(tab[j-Ntt*i-i]!=c) return 0;
	return 1;
}

int winsBorR(char tabTemp[], int Nt, int Kt)
{
	int foundB=0, foundR=0;
	for(int i=0; i<(Nt*Nt); i++)
	{
		if (tabTemp[i]=='B')
		{
			if ((((i%Nt)+1)>=Kt)) /*se sta abbastanza a destra*/
			{
				if (rowLeft(tabTemp,i,tabTemp[i],Kt)) { foundB=1; break; }
				if (i>=((Kt-1)*Nt))/*se sta abbastanza in basso*/ if(diaLU(tabTemp,i,tabTemp[i],Kt,Nt)) { foundB=1; break; }
				if (i<=(Nt*Nt-((Kt-1)*Nt)-1))/*se sta abbastanza in alto*/ if(diaLD(tabTemp,i,tabTemp[i],Kt,Nt)) { foundB=1;  break; }
			}
			if (i>=((Kt-1)*Nt))/*se sta abbastanza in basso*/ if(colUp(tabTemp,i,tabTemp[i],Kt,Nt)) { foundB=1; break; }
		}
	}
	for(int i=0; i<(Nt*Nt); i++)
	{
		if (tabTemp[i]=='R')
		{
			if ((((i%Nt)+1)>=Kt)) /*se sta abbastanza a destra*/
			{
				if (rowLeft(tabTemp,i,tabTemp[i],Kt)) { foundR=1; break; }
				if (i>=((Kt-1)*Nt))/*se sta abbastanza in basso*/ if(diaLU(tabTemp,i,tabTemp[i],Kt,Nt)) { foundR=1; break; }
				if (i<=(Kt*Nt-1))/*se sta abbastanza in alto*/ if(diaLD(tabTemp,i,tabTemp[i],Kt,Nt)) { foundR=1; break; }
			}
			if (i>=((Kt-1)*Nt))/*se sta abbastanza in basso*/ if(colUp(tabTemp,i,tabTemp[i],Kt,Nt)) { foundR=1; break; }
		}
	}
	int temp=foundB+foundR*2;
	return temp;
}

int main ()
{
	int T=getNextNumb(),N=0,K=0;
	for(int i=0;i<T;i++)
	{
		N=getNextNumb();
		K=getNextNumb();
		char *tab=new char[N*N];
		getTab(tab,N);
		rotateTab(tab,N);
		for(int j=0;j<N;j++) { for(int k=0;k<N;k++) cout<<tab[j*N+k]; cout<<'\n'; }

		int result=winsBorR(tab,N,K);

		cout<<result<<endl;

		ofs.write("Case #",6);
		std::string s;
		std::stringstream out;
		out << (i+1);
		s = out.str();
		ofs.write(s.c_str(),s.length());
		ofs.put(':');
		ofs.put(' ');
		if (result==3) ofs.write("Both",4);
		if (result==1) ofs.write("Blue",4);
		if (result==2) ofs.write("Red",3);
		if (result==0) ofs.write("Neither",7);
		ofs.put('\n');
		delete tab;
	}
	system("pause");
	return 0;
}
