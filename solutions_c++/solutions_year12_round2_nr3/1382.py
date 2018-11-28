#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<fstream>

using namespace std;

vector<int>subset1,subset2;
map<int,int> resp;
map<int,vector<int>>mapa;
int size;
bool coinciden(int A, int B){
	for(int i=0;i<23;++i){
		if(((A>>i)&1)==1 && ((B>>i)&1)==1)return false;
	}
	return true;
}
bool OK;
void findsubsets(vector<int>&subset,int sub1=0,int sum=0,int bit=0){
	if(OK==true)return;
	if(bit==size-1){
		resp[sum]++;
		if(resp[sum]>1 && sum!=0){
			for(int i=0;i<mapa[sum].size();++i){
				if(coinciden(mapa[sum][i],sub1)==true){
					int sub2=mapa[sum][i];
					for(int j=0;j<subset.size();++j){
						if(((sub1>>(j))&1)==1)
							subset1.push_back(subset[j]);
					}
					for(int j=0;j<subset.size();++j){
						if(((sub2>>(j))&1)==1)
							subset2.push_back(subset[j]);
					}
					OK=true;
					return;
				}
			}
		}
		mapa[sum].push_back(sub1);
		return;
	}

	findsubsets(subset,sub1,sum,bit+1);
	if(OK==true)return;
	findsubsets(subset,sub1|(1<<bit),sum+subset[bit],bit+1);
	return;
}

int main(){
	ifstream in;
	ofstream out;
	in.open("Equal_Sums_in.txt");
	out.open("Equal_Sums_out.txt");
	int T;
	in>>T;
	for(int caso=1;caso<=T;++caso){
		vector<int>temp;
		subset1=subset2=temp;
		map<int,int> temp1;
		resp=temp1;
		map<int,vector<int>>temp2;
		mapa=temp2;

		int N;
		in>>N;
		size=N;
		vector<int>subset;
		for(int i=0;i<N;++i){
			int number;
			in>>number;
			subset.push_back(number);
		}
		OK=false;
		findsubsets(subset);

		out<<"Case #"<<caso<<":"<<endl;
		out<<subset1[0];
		for(int j=1;j<subset1.size();++j){
			out<<" "<<subset1[j];
		}
		out<<endl<<subset2[0];
		for(int j=1;j<subset2.size();++j){
			out<<" "<<subset2[j];
		}
		out<<endl;

	}
	in.close();
	out.close();
	return 0;
}