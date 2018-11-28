#include<iostream>
#include<set>
#include<string>
#include<vector>
#include<iomanip>
#include<map>
#include<fstream>
#include<algorithm>
#include<cstdio>
//#include<strstream>
#define f(i,n) for(int i=0;i<n;i++)
struct node{
	string s;
	float f;
	node *left,*root;
};

int main(){
	ifstream fin;
	ofstream fout;
	fin.open("input.txt");
	fout.open("output.txt");
	
	int t1;
	int c=1;
	fin>>t1;
	while(t1--){
	//	stringstream ss (stringstream::in | stringstream::out);
		int n;
		fin>>n;
		int x,y,z,v1,v2,v3;
		int x1=0,x2=0,x3=0,vx=0,vy=0,vz=0;
		f(i,n){
			fin>>x>>y>>z>>v1>>v2>>v3;
			x1+=x;
			x2+=y;
			x3+=z;
			vx+=v1;
			vy+=v2;
			vz+=v3;
		}
		double a1,a2,a3,b1,b2,b3;
		a1=(double)x1/(double)n;
		a2=(double)x2/(double)n;
		a3=(double)x3/(double)n;
		b1=(double)vx/(double)n;
		b2=(double)vy/(double)n;
		b3=(double)vz/(double)n;
		double k1=b1*b1+b2*b2+b3*b3;
		double k2=(a1*b1+a2*b2+a3*b3);
		double k3=(a1*a1+a2*a2+a3*a3);
		//cout<<k1<<k2<<k3<<"fs"<<endl;;
		double t;
		if(k1==0.0)
			t=0.0;
		else
			 t=-1.0*(k2/k1);
		if(t<0)
			t=0.0;
		cout<<t<<endl;
		cout<<k1*t*t+k2*t*2.0+k3;
		double d=(k1*t*t)+(k2*t*2.0)+k3;
		cout<<d<<" jrger"<<endl;
		if(d<=0.0)
			d=0.0;
		else
			d=sqrt(d);
//		char  s1[20],s2[20];
//		sprintf(s1,"%.8d",d);
//		sprintf(s2,"%.8d",t);




//d+=.00000001;
//t+=.00000001;
//printf("%0.9d",d);
		fout<<"Case #"<<c<<": "<<d<<" "<<t<<endl;



		c++;

	}


	fin.close();
	fout.close();
	return 0;
}
		




		

