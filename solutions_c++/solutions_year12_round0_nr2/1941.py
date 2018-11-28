#include<iostream>
#include<fstream>
using namespace std;
int main()
{	int *temp,i,n,num,s,p,te,j;
	ifstream infs;
	infs.open("B-large.in");
	ofstream outf;
	outf.open("result.txt");
	//int data=0,temp*,i,n,num,s,p,te;
	infs>>n;
	for(i=0;i<n;i++){
		infs>>num;infs>>s;infs>>p;

		te=0;
		temp=new int[num];
		for(j=0;j<num;j++)
			infs>>temp[j];
		for(j=0;j<num;j++)
		{
		if(!p) {
			te++;
			continue;
		}
		if(p && !temp[j])
			continue;
		if(temp[j]>=(3*p-2))
		te++;
	 if(((temp[j]==(3*p-3))||(temp[j]==(3*p-4)))&&(s>0)){
			te++;
			s--;
		}
			
		
	
	} 
	outf<<"Case #"<<i+1<<": ";
		outf<<te<<endl;
	//	delete(temp);
	//cout<<data;
	}
}
