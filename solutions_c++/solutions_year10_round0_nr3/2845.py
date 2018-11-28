#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int T,N,j,i,p;
    long sum=0,add=0,R,K;
    unsigned long int a[1000];
    ifstream infile;
    infile.open("ip33.txt");
    ofstream outfile;
    outfile.open("op33.txt");
    if(infile){
    infile>>T;
    for(i=1;i<=T;i++){  sum=0;
    infile>>R;
    infile>>K;
    infile>>N;
    for(j=0;j<N;j++)
    infile>>a[j];
    p=0;

    for(j=0;j<R;j++)
    {  int c=0;
	while(add+a[p]<=K&& c<N){
			   add+=a[p]; p=(p+1)%N;c++;
			  }
	sum+=add;
	add=0;
    }

    outfile<<"Case #"<<i<<": "<<sum;
    outfile<<endl;;
    } }
   infile.close();
   outfile.close();
   return 1;
}
