#include<iostream>
#include<fstream>
using namespace std;

int calculate_maxbest(int n, int s, int p, int* scores,int& surprise){

	int count_sreq=0;
	int count_snreq = 0;

	for(int i=0;i<n;i++){
		int k = scores[i]/3;
		int r = scores[i]%3;
		
		if(r==0 && k==0){ //special case for zero
			if(0>=p)
				count_snreq++;
		}else if(r==1 && k==0){ //special case for 1;
			if(1>=p)
				count_snreq++;
		}else if(r==0 && k-1>=0){
			if(k>=p)
				count_snreq++;
			else if(k+1>=p)
				count_sreq++;
		}else if(r==1 && k-1>=0){
			if(k+1>=p)
				count_snreq++;
		}else if(r==2 && k>=0){
			if(k+1>=p)
				count_snreq++;
			else if(k+2>=p)
				count_sreq++;
		}
		
	}
	
	 surprise = ((count_sreq>s)?s:count_sreq);
	int maxcount = count_snreq +surprise;
	return maxcount;
}


int main(){
	
	int ncases;
	int n,s,p;
	int scores[100];
	fstream in("inputfile.txt",ios::in);
	fstream out("outputfile.txt",ios::out);
	in>>ncases;
	for(int i=0;i<ncases;i++){
		in>>n;
		in>>s;
		in>>p;
		for(int j=0;j<n;j++)
			in>>scores[j];
		int surprise;
		int result = calculate_maxbest(n,s,p,scores,surprise);
		out<<"Case #"<<(i+1)<<": "<<result<<endl;
	}
	in.close();
	out.close();
}