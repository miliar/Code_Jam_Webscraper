#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <list>

using namespace std;

int main (int argc, char * const argv[]) {
	string line;
	ifstream myfile ("solve2.txt");
	list <int> nums;
	int T,N,S,P,i,j,out=0,temp;
	if (myfile.is_open())
	{
		//getline (myfile,line);
		myfile>>T;
		for (i=1;i<=T;i++)
		{
			myfile>>N>>S>>P;
			for (j=0;j<N;j++)
			{
				myfile>>temp;
				nums.push_back(temp);
			}
			nums.sort();
			nums.reverse();
			for (list<int>::iterator id=nums.begin();id!=nums.end();id++)
			{
				if(((double)*id)/3>=P){
					out++;
				} else if (*id==0){
					break;
				} else if(*id/3+2>=P){
					temp=*id-P;
					if (temp%2<=1){
						if (P-temp/2==2 && S>0){
							S--;out++;
						} else if(P-temp/2==1){
							out++;
						}
					}	
				}
				//cout<<*id<<" ";
			}
			cout<<"Case #"<<i<<": "<<out<<endl;
			nums.erase(nums.begin(),nums.end());
			out=0;
		}
		myfile.close();	
	}
	else cout << "Unable to open file"; 
    return 0;
}