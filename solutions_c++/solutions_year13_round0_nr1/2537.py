#include <iostream>
#include <math.h>
#include <stdlib.h>
using namespace std;

float min(float a,float b ,float c,float d)
{
	if(a<=b&&a<=c&&a<=d)
	return a;
	if(b<=a&&b<=c&&b<=d)
	return b;
	if(c<=a&&c<=b&&c<=d)
	return c;
	if(d<=a&&d<=c&&d<=b)
	return d;
}
float max(float a,float b ,float c,float d)
{
	if(a>=b&&a>=c&&a>=d)
	return a;
	if(b>=a&&b>=c&&b>=d)
	return b;
	if(c>=a&&c>=b&&c>=d)
	return c;
	if(d>=a&&d>=c&&d>=b)
	return d;
}
	

void ifwin(float a[][4])
{
	int win=-1;	

	for (int i=0; i<4; i++) {
		if (abs(a[i][0]-a[i][1])<=0.5&&abs(a[i][0]-a[i][2])<=0.5&&abs(a[i][0]-a[i][3])<=0.5&&abs(a[i][1]-a[i][2])<=0.5&&abs(a[i][1]-a[i][3])<=0.5&&abs(a[i][2]-a[i][3])<=0.5) {  // Horizontal line checked
			win=a[i][0];
			if(win!=-1)
			{
				if(win==0.5)
				win=min(a[i][3],a[i][1],a[i][2],a[i][0]);
				if(win==0.5)
				win=max(a[i][3],a[i][1],a[i][2],a[i][0]);
				if(win==1)
				{
				cout<<"X won"<<endl;
				return;
				}
				if(win==0){
				cout<<"O won"<<endl;
				return;}
			}

		}

		if (abs(a[0][i]-a[1][i])<=0.5&&abs(a[0][i]-a[2][i])<=0.5&&abs(a[0][i]-a[3][i])<=0.5&&abs(a[1][i]-a[2][i])<=0.5&&abs(a[1][i]-a[3][i])<=0.5&&abs(a[2][i]-a[3][i])<=0.5) {   // Vertical lines checked
			win=a[0][i];
			if(win!=-1)
			{
				if(win==0.5)
				win=min(a[0][i],a[2][i],a[1][i],a[3][i]);
				if(win==0.5)
				win=max(a[0][i],a[2][i],a[1][i],a[3][i]);
				if(win==1)
				{
				cout<<"X won"<<endl;
				return;
				}
				if(win==0){
				cout<<"O won"<<endl;
				return;}
			}
		}
	}

	if (abs(a[0][0]-a[1][1])<=0.5&&abs(a[1][1]-a[2][2])<=0.5&&abs(a[1][1]-a[3][3])<=0.5&&abs(a[0][0]-a[2][2])<=0.5&&abs(a[0][0]-a[3][3])<=0.5&&abs(a[2][2]-a[3][3])<=0.5) {   // Main diagonal checked
		win=a[0][0];
		if(win!=-1)
			{
				if(win==0.5)
				win=min(a[1][1],a[0][0],a[2][2],a[3][3]);
				if(win==0.5)
				win=max(a[0][0],a[1][1],a[2][2],a[3][3]);
				if(win==1)
				{
				cout<<"X won"<<endl;
				return;
				}
				if(win==0){
				cout<<"O won"<<endl;
				return;}
			}
	}

	if (abs(a[0][3]-a[2][1])<=0.5&&abs(a[2][1]-a[1][2])<=0.5&&abs(a[0][3]-a[3][0])<=0.5&&abs(a[0][3]-a[1][2])<=0.5&&abs(a[2][1]-a[3][0])<=0.5&&abs(a[1][2]-a[3][0])<=0.5) {   // The other diagonal is checked
		win=a[0][3];
		if(win!=-1)
			{
				if(win==0.5)
				win=min(a[0][3],a[2][1],a[1][2],a[3][0]);
				if(win==0.5)
				win=max(a[0][3],a[2][1],a[1][2],a[3][0]);
				if(win==1)
				{
				cout<<"X won"<<endl;
				return;
				}
				if(win==0){
				cout<<"O won"<<endl;
				return;}
			}
	}
		bool t=true;
		for(int k1=0;k1<4;k1++)
		for(int k2=0;k2<4;k2++)
		t=t && (a[k1][k2]!=-1);
		
		if(t)
		cout<<"Draw"<<endl;
		else cout<<"Game has not completed"<<endl;
}


int main()
{
	int n;
	cin>>n;
	for(int i=1;i<=n;i++)
	{
		float a[4][4];
		for(int k=0;k<4;k++)
		{			
			for(int l=0;l<4;l++)
			{
				char c;
				cin>>c;
				switch (c)
				{
					case 'X' : a[k][l]=1;
					break;
					case '0' : a[k][l]=0;
					break;
					case 'O' : a[k][l]=0;
					break;
					case 'T' : a[k][l]=0.5;
					break;
					case '.': a[k][l]=-1;
					break;
				}
		  }
	  }
	  cout<<"Case #"<<i<<": ";
	  ifwin(a);
  }
}
