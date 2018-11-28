#include<iostream>
#include<fstream>
#include<vector>

using namespace std;
void main(){
	int testcases;
    int totalRides,numGroups,groupSize;
	int seats,occ;
	int rev=0;
	vector<int> grps;
	ifstream in("C-small-attempt0.in");
	ofstream out("output.txt");
	if(in.good()){
	//cout<<"\nEnter number of Groups: ";
	//cin>>numGroups;
	//for(int i=0;i<numGroups;i++){
	//	int s;
	//	cout<<"\nEnter group "<<i+1<<"size: ";
	//	cin>>s;
	//	grps.push_back(s);
	//}
	//cout<<"\nEnter total number of rides:";
 //   cin>>totalRides;
	//cout<<"\nEnter of Seats available:";
	//cin>>seats;
		in>>testcases;
		if(testcases>=1&&testcases<=50){
			for(int t=0;t<testcases;t++){
				out<<"Case #"<<(t+1)<<": ";
				in>>totalRides;				
			    in>>seats;
				in>>numGroups;
				rev=0;
				grps.clear();				
				for(int i=0;i<numGroups;i++){
					int s;			
					in>>s;
					if(s<=seats)
					 grps.push_back(s);
					else
						out<<"invalid group size for group "<<i+1;
				}	
				for(int i=0;i<totalRides;i++){
					int j=0;
					occ=0;
					for(j=0;j<grps.size();j++){
						if(occ+grps[j]<=seats){
							occ+=grps[j];								
						}
						else
							break;
					}
					if(j!=grps.size()){			
						for(int k=0;k<j;k++){
							vector<int>::iterator iter=grps.begin();
							int temp=*iter;
							grps.erase(iter);
							grps.push_back(temp);
						}
					}
					rev+=occ;
				}
				out<<rev<<"\n"; 
			}	
		}
		else{
			out<<"Invalid number of testcases.Should be between 1 and 50";
		}
	}
	else{
		out<<"cannot open file";
	}
}