#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
using namespace std;

int count=0;	// the final answer to each case, as a global variable
vector < vector<int> > freq;
vector <int> line;
//using a 2-D vector to map each string , for this problem can be changed into a pure recursion problem

void cal(int start,int pre){
	if(start==19){
		count=(count+1)%10000;
		return;
	}
	for(int i=0;i<freq[start].size();i++){
		if(freq[start][i]>pre)
				cal(start+1,freq[start][i]);
	}
	
}
// using a recursive way to calculate the possible way to form the "welcome to code jam"
void check_by_letter(string str){
	int i=0;
	int length=str.length();
	
	freq.clear();
	for(int j=0;j<19;j++){
		freq.push_back(line);
	}
	
	while(i<length){
		
		switch(str[i]){
			case 'w' : freq[0].push_back(i);
						break;
			case 'e' : freq[1].push_back(i);
						freq[6].push_back(i);
						freq[14].push_back(i);
						break;
			case 'l' : freq[2].push_back(i);
						break;
			case 'c' : freq[3].push_back(i);
						freq[11].push_back(i);
						break;
			case 'o' : freq[4].push_back(i);
						freq[9].push_back(i);
						freq[12].push_back(i);
						break;
			case 'm' : freq[5].push_back(i);
						freq[18].push_back(i);
						break;
			case ' ' : freq[7].push_back(i);
						freq[10].push_back(i);
						freq[15].push_back(i);
						break;
			case 't' : freq[8].push_back(i);
						break;
			case 'd' : freq[13].push_back(i);
						break;
			case 'j' : freq[16].push_back(i);
						break;	
			case 'a' : freq[17].push_back(i);
						break;
			default: break;
		}
		i++;
	}
}
// the function to map  a string into a 2-D vector

int main(){
	
	int N,i=0;
	cin >>N;
	string str[N];
	
	cin.ignore();
	for(;i<N;i++)
		getline(cin,str[i]);
		
	i=0;
	//dealing with each case in a loop
	while(i<N){
		check_by_letter(str[i]);
		cal(0,-1);
		cout<<"Case #"<<i+1<<": "<<setw(4)<<setfill('0')<<count<<endl;
		i++;
		count=0;
	}
}