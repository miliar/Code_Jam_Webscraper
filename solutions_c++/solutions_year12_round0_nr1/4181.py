#include<iostream>
#include<fstream>
#include<stdio.h>
using namespace std;

int main()
{	char M[26][3]={"ay","bh","ce","ds","eo","fc","gv","hx","id","ju","ki","lg","ml","nb","ok","pr","qz","rt","sn","tw","uj","vp","wf","xm","ya","zq"};
	int t,t1;
	char c;
	char output[] = "output.txt";
	ofstream OutFile;
	OutFile.open(output);
	cin>>t;
	t1=t;
	c=getchar();
	while(t--){
		OutFile<<"Case #"<<t1-t<<": ";
		c=getchar();
		while(c!=10){
			if(c==32)
				OutFile<<" ";
			else
				OutFile<<M[c-97][1];
			c=getchar();
		 }
		 //if(t!=0)
		 OutFile<<endl;		
		}
	}
