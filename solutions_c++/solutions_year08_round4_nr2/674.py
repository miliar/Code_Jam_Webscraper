
#include<stdio.h> 
#include<math.h> 
#include<string.h> 
#include<stdlib.h> 
#include<iostream>

using namespace std;
double xmult(double x1,double y1,double x2,double y2,double x0,double y0){
	return (x1-x0)*(y2-y0)-(x2-x0)*(y1-y0);
}

double area_triangle(double x1,double y1,double x2,double y2,double x3,double y3){
	return fabs(xmult(x1,y1,x2,y2,x3,y3))/2;
}

int main() 
{ 
	int rn,n,m,a;
	cin >> rn;
	for (int ri=1;ri<=rn;ri++)
	{
		cin >> n >> m >> a;
		cout << "Case #" << ri << ": ";
		if (n*m<a)
		{
			cout << "IMPOSSIBLE" << endl;
			continue;
		} 
/*		if (n>m)
		{
			int t=n;
			n=m;
			m=t;
		}
		bool f=0;
		int e=sqrt(m*m+n*n);
		for (int i=1;i<=n;++i)
			if (a%i==0 && a/i<=m)
			{
				f=1;
				cout << "0 0 " << i << " 0 0 " << a/i << endl;
				break;
			}*/
		bool f=0;
		for (int x1=0;x1<=n && !f;x1++)
			for (int y1=0;y1<=m && !f;++y1)
				for (int x2=0;x2<=n && !f;x2++)
					for (int y2=0;y2<=m && !f;++y2)
						for (int x3=0;x3<=n && !f;++x3)
							for (int y3=0;y3<=m;++y3)
								if (area_triangle(x1,y1,x2,y2,x3,y3)*2==a)
								{
									cout << x1 << " " << y1 << " " << x2 << " " <<
									y2 << " " << x3 << " " << y3 << endl;
									f=1;
									break;
								}
		if (f==0)
		{
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
	}
		
			
		


//	system("PAUSE");
	return 0;
	
} 


