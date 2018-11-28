#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <set>

using namespace std;

int n,a,b,y,end; 
string temp,swapped;
set<int>nums;
set<int>::iterator it;

bool check(int num,int bigger);
bool not_exists(int num);
string swap(string input, int end);
string i2string(int i);\

int main (int argc, char * const argv[]) {
	
	string line;
	ifstream myfile ("solve.txt");

	int i,j,k,current,total,this_total,last_int;
	if (myfile.is_open())
	{
		myfile>>n;
		for (i=1;i<=n;i++)
		{
			myfile>>a>>b;
			y=0;
			total=0;
			this_total=0;
			last_int=0;
			if (b>9){
				for(j=a;j<=b;j++){
						temp=i2string(j);
						for(k=1;k<temp.size();k++){
							swapped=swap(temp,k);
							current=atoi(swapped.c_str());
							if (check(current,j)){
								if(last_int!=current){
									nums.insert(current);
									nums.insert(j);
									last_int=current;
									total++;//found a pair
								}
							}
						}
				}

			}
			
			cout<<"Case #"<<i<<": "<<total<<endl;
			//cout<<total<<endl;
			nums.erase(nums.begin(),nums.end());
		}
		myfile.close();	
	}
	
    return 0;
}
bool check(int num,int bigger){
	if (num<=b && num>bigger){
		return true;
	}
	return false;
}
bool not_exists(int num){
	it=nums.find(num);
	if (it==nums.end()){//not found
		return true;
	}
	return false;
}

string i2string(int i) {
	ostringstream buffer;
	buffer << i;
	return buffer.str();
}
string swap(string input, int end){
	int from = input.size()-end;
	string move=input.substr(from, end);
	string front=input.substr(0,from);
	return front.insert(0,move);
}
