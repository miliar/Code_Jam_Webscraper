#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

int main(){

	//変数用意
	int N;
	string buf;
	vector<int> num;


	cin>>N;


	ofstream cou("gjamB.txt");
	for(int n=1;n<=N;n++){//計算・出力
		cin>>buf;
		for(int i=0;i<buf.size();i++){
			num.push_back((int)buf[i]-48);
		}

		bool find = false;

		for(int i=num.size()-1;i>0;i--){

			if(num[i]>num[i-1]){
				find = true;
				int min = 10;
				int index = -1;
				for(int j=i;j<num.size();j++){
					if(num[i-1]<num[j]&&num[j]<min){
						min = num[j];
						index = j;
					}
				}
				num[index] = num[i-1];
				num[i-1] = min;

				bool flag = true;
				while(flag){
					flag = false;
					for(int j=i;j<num.size()-1;j++){
						if(num[j]>num[j+1]){
							min = num[j];
							num[j] = num[j+1];
							num[j+1] = min;
							flag = true;
						}
					}
				}
				break;

			}

		}

		if(!find){
			num.push_back(0);

			int min = 10;
			int index = -1;
			for(int i=0;i<num.size();i++){
				if(num[i]<min&&num[i]!=0){
					min = num[i];
					index = i;
				}
			}
			num[index] = num[0];
			num[0] = min;

			bool flag = true;
			while(flag){
				flag = false;
				for(int j=1;j<num.size()-1;j++){
					if(num[j]>num[j+1]){
						min = num[j];
						num[j] = num[j+1];
						num[j+1] = min;
						flag = true;
					}
				}
			}
		}

		cou<<"Case #"<<n<<": ";
		for(int i=0;i<num.size();i++)
			cou<<num[i];
		cou<<endl;
		num.clear();
	}//計算・出力





	return 0;
}