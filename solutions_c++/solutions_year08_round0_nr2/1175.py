#include <iostream>
#include <string>
#include <fstream>
using namespace std;
void sort(int (*a)[2],int);
int main()
{
ifstream infile("A-small1.in");
ofstream outfile("A-output1.in");
int n;
int NA,NB,turn;
string temp_str;
const char* temp;
int i,j;
int serial=0;
int A_train=0;
int B_train=0;
infile>>n;
while(n>0)
{
n--;
//cout<<"enter turnaround time: \n";
infile>>turn;
//cout<<"enter trains from station A: ";
infile>>NA;
//cout<<"enter trains from station B: ";
infile>>NB;
int A_dep[NA][2];
int A_arr[NA][2];
int B_dep[NB][2];
int B_arr[NB][2];
getline(infile,temp_str);
//read one by one
for(i=0;i<NA;i++)
{
	getline(infile,temp_str);
	//cout<<temp_str;
	temp=(temp_str.substr(0,2)).c_str();
	A_dep[i][0]=atoi(temp);
	A_dep[i][1]=atoi((temp_str.substr(3,2)).c_str());
	A_arr[i][0]=atoi((temp_str.substr(6,2)).c_str());
	A_arr[i][1]=atoi((temp_str.substr(9,2)).c_str())+turn;
	if(A_arr[i][1]>59)
	{
		A_arr[i][1]=A_arr[i][1]-60;
		A_arr[i][0]=A_arr[i][0]+1;
	}
	//cout<<A_dep[i][0]<<"  "<<A_dep[i][1]<<"  "<<A_arr[i][0]<<"  "<<A_arr[i][1]<<endl;
}
for(i=0;i<NB;i++)
{
	getline(infile,temp_str);
	B_dep[i][0]=atoi((temp_str.substr(0,2)).c_str());
	B_dep[i][1]=atoi((temp_str.substr(3,2)).c_str());
	B_arr[i][0]=atoi((temp_str.substr(6,2)).c_str());
	B_arr[i][1]=atoi((temp_str.substr(9,2)).c_str())+turn;
	if(B_arr[i][1]>59)
	{
		B_arr[i][1]=B_arr[i][1]-60;
		B_arr[i][0]=B_arr[i][0]+1;
	}
	//cout<<B_dep[i][0]<<"  "<<B_dep[i][1]<<"  "<<B_arr[i][0]<<"  "<<B_arr[i][1]<<endl;
}
sort(A_dep,NA);
sort(A_arr,NA);

sort(B_dep,NB);
sort(B_arr,NB);

/*for(i=0;i<NA;i++)
cout<<A_dep[i][0]<<":"<<A_dep[i][1]<<endl;
for(i=0;i<NB;i++)
cout<<B_arr[i][0]<<":"<<B_arr[i][1]<<endl;
*/
int p1=0;
int p2=0;
int counter_A=0, counter_B=0;
//take two pointers p1 and p2
for(i=0;i<NA;i++)
{
	if(A_dep[i][0]>=B_arr[p1][0] && p1<NB)
	{
		if(A_dep[i][0]==B_arr[p1][0])
		{
			if(A_dep[i][1]>=B_arr[p1][1])
			p1++;
			else
			counter_A++;
		}
		else
		p1++;
	}
	else 
		{
			counter_A++;
			//cout<<A_dep[i][0]<<endl;
		}
}
for(i=0;i<NB;i++)
{
	if(B_dep[i][0]>=A_arr[p2][0] && p2<NA)
	{
		if(B_dep[i][0]==A_arr[p2][0])
		{
			if(B_dep[i][1]>=A_arr[p2][1])
			p2++;
			else
			counter_B++;
		}
		else
		p2++;
	}
	else 
		{
			counter_B++;
			//cout<<B_dep[i][0]<<endl;
		}
}
serial++;
if(serial==1)
outfile<<"Case #"<<serial<<": "<<counter_A<<" "<<counter_B;
else
outfile<<endl<<"Case #"<<serial<<": "<<counter_A<<" "<<counter_B;

	
}
return 0;
}

void sort(int (*a)[2],int n)
{
	int i,j;
	int temp;
	for(i=0;i<n-1;i++)
	{
		for(j=i+1;j<n;j++)
		{
			if(a[i][0]>=a[j][0])
			{
				if(a[i][0]==a[j][0])
				if(a[i][1]<a[j][1])
				continue;
				temp = a[i][0];
				a[i][0]=a[j][0];
				a[j][0]=temp;
				temp = a[i][1];
				a[i][1]=a[j][1];
				a[j][1]=temp;
			}
		}
	}
}
				

