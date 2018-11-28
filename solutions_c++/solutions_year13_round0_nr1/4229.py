#include<iostream>
#include<fstream>

using namespace std;

int set[16]={0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
int main()
{
	int cas=1;
	fstream m,t;
	t.open("out.txt");
	m.open("A-large.in");
	int tt;
	m>>tt;
	while(tt--)
	{
		int a[4]={0,0,0,0};
		int b[4]={0,0,0,0};
		for(int i=0;i<4;i++)
		{
			char s;
			string sw;
			m>>sw;
			for(int j=0;j<4;j++)
			{set[i*4+j]=sw[j];
			a[i]+=set[i*4+j];}
		}
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				b[i]+=set[j*4+i];
			}
		}
		int d1=set[0]+set[5]+set[10]+set[15];
		int d2=set[3]+set[6]+set[9]+set[12];
		int r=0;
		for(int i=0;i<4;i++)
		{
			if(a[i]==316||a[i]==321||b[i]==316||b[i]==321)
			{
				r=1;
				break;
			}
			if(a[i]==348||a[i]==352||b[i]==348||b[i]==352)
			{
				r=2;
				break;
			}	
		}
		if(d2==316||d2==321||d1==316||d1==321)
		r=1;
		if(d2==348||d2==352||d1==348||d1==352)
		r=2;
		for(int i=0;i<16;i++)
		{
		if(set[i]==46)
		{
		if(r==0)
		r=3;
		break;
		}}
		t<<"Case #"<<cas<<": ";
		if(r==0)
		t<<"Draw";
		else if(r==2)
		t<<"X won";
		else if(r==1)
		t<<"O won";
		else t<<"Game has not completed";
		t<<endl;;
		cas=cas+1;
	}
	
		t.close();
		m.close();
	return 0;
}
