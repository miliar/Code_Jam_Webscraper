#include<iostream>
#include<cstdio>
#include<vector>
#include<fstream>
using namespace std;

int main(){

	ifstream fin("B-large.in");
	ofstream fout("googlecodejamq2large.txt");
	
	int testcase;
	fin>>testcase;
	int count=0;
	int n,s,p;int i;
	int o=1;int thres,supCount;
	while(testcase--){
	
		fin>>n>>s>>p;
		vector<int>numbers(n);
		for(i=0;i<n;i++){
			fin>>numbers[i];
		}

		thres = p*3;
		supCount = s;
		for(i=0;i<n;i++){
		
			if(p==0){
				count=n;
				break;
			}
			else if(numbers[i] > thres){
				count++;
			}
			else if(numbers[i] <= thres && numbers[i] >=(thres-2))
				count++;
			else if((numbers[i] < (thres -2)) && (numbers[i] >=(thres-4)) && supCount>0 && numbers[i]>0){
				count++;
				supCount--;
			}
			//cout<<numbers[i]<<"\t"<<count<<"\t"<<supCount<<"\n";
		}			
			
		fout<<"Case #"<<o<<": "<<count<<"\n";		
		o++;
		count=0;
	}


	return 0;
}
