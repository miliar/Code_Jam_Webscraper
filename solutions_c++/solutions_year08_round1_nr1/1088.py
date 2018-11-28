#include<iostream>
#include<fstream>
using namespace std;
int main(int argc,char *argv[])
{
	ifstream infile1,infile2,infile3;ofstream outfile,outfile1;
	int *v1,*v2;int sum=0,c1,c2,i,j,cases,v;
	char *line;line =new char[100];
	infile1.open(argv[1]);
	infile1.getline(line,100,'\n');
	cases=atoi(line);
	
//	cout<<"cases:"<<cases<<endl;
	for(j=0;j<cases;j++)
	{
	infile1.getline(line,100,'\n');
	v=atoi(line);
	
//	cout<<"v:"<<v<<endl;
	v1=new int[v];
	v2=new int[v];
	infile1.getline(line,100,'\n');
	v1[0]=atoi(strtok(line," "));
	for(i=1;i<v;i++)
	{
		v1[i]=atoi(strtok(NULL," "));
	}
	infile1.getline(line,100,'\n');
        v2[0]=atoi(strtok(line," "));
	for(i=1;i<v;i++)
	{
		v2[i]=atoi(strtok(NULL," "));

	}
//	for(i=0;i<v;i++)
//	cout<<"v1[i]:"<<v1[i]<<" v2[i]:"<<v2[i]<<endl;
	outfile.open("temp.temp");
	for(i=0;i<v;i++)
	{
		outfile<<v1[i]<<endl;
	}
	system("sort -n temp.temp > temp.temp1");
//	outfile.close();
	outfile1.open("temp.temp2");
	for(i=0;i<v;i++)
        {
                outfile1<<v2[i]<<endl;//cout<<"outfile1"<<v2[i]<<endl;
        }
        system("sort -r -n temp.temp2 > temp.temp3");
	infile2.open("temp.temp1");
	infile3.open("temp.temp3");
	sum=0;
	for(i=0;i<v;i++)
	{
		infile2.getline(line,100,'\n');
	//	cout<<"line1:"<<line<<endl;
		c1=atoi(line);
		infile3.getline(line,100,'\n');
	//	cout<<"line2:"<<line<<endl;	
		c2=atoi(line);
	//	cout<<"c1:"<<c1<<" c2:"<<c2<<endl;
		sum+=c1*c2;
	}
	cout<<"Case #"<<j+1<<": "<<sum<<endl;
    infile2.close();infile3.close();outfile.close();outfile1.close();

	system("rm -rf temp.temp temp.temp1 temp.temp2 temp.temp3");

	}
//	infile1.close();infile2.close();outfile.close();outfile1.close();
//	system("rm -rf temp.temp temp.temp1 temp.temp2 temp.temp3");
}	
