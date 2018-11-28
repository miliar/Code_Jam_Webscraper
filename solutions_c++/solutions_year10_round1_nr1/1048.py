
#include <math.h>
#include <iostream>
#include <fstream>
#include <limits.h>
#include <list>

#define F(a,b,c) for(size_t a = b;a != c;a++)
#define FF(a,b,c) for(size_t a = b;a != c-1;a--)

using namespace std;

int main(){
	ifstream input("inputA.txt");
	ofstream output("outputA.txt");
	size_t T;
	input >> T;
	size_t N,K;
	char ** buff,*r,*b;
	size_t maxr,maxb;
	list<string>  search;
	F(i,0,T){
		maxb = maxr = 0;
		input >> N >> K;
		buff = new char*[N];
		r = new char[K+1];
		b = new char[K+1];
		r[K] = '\0';
		b[K] = '\0';
		F(j,0,K){
			r[j] = 'R';
			b[j] = 'B';
		}
		cout<< r << "\n" << b << "\n";
		search.clear();
		F(j,0,N){
			buff[j] = new char[N];
			input >> buff[j];
			size_t next_post = N-1;
			FF(k,N-1,0){
				if(buff[j][k] != '.'){
					buff[j][next_post] = buff[j][k];
					if(k!=next_post)
						buff[j][k] = '.';
					next_post--;
				}
			}
			search.push_back(string(buff[j]));
		}
		F(j,0,N){
			string temp(N,'.');
			F(k,0,N){
				temp[k] = buff[k][j];
			}
			search.push_back(temp);
		}
		{
			string temp1(N,'.'),temp2(N,'.');
			F(k,0,N){
				temp1[k] = buff[k][k];
				temp2[k] = buff[k][N-k-1];
			}
			search.push_back(temp1);
			search.push_back(temp2);
		}
		F(j,1,N-K+1){
			string temp1(N-j,'.'),temp2(N-j,'.'),temp3(N-j,'.'),temp4(N-j,'.');
			F(k,0,N-j){
				
				temp1[k] = buff[j+k][k];
				temp2[k] = buff[k][j+k];
				temp3[k] = buff[k+j][N-k-1];
				temp4[k] = buff[k][N-k-1-j];
			}
			search.push_back(temp1);
			search.push_back(temp2);
			search.push_back(temp3);
			search.push_back(temp4);
		}
		for(list<string>::iterator it = search.begin();it!=search.end()&&((maxr+maxb)<2);it++){
			if((*it).find(string(r)) != (*it).npos){
				maxr = 1;
			}
			if((*it).find(string(b)) != (*it).npos){
				maxb = 1;
			}
			//cout << (*it).c_str()<<endl;
		}
		if((maxr+maxb)==2){
			output << "Case #"<<(i+1)<<": Both\n";
		}else{
			if((maxr+maxb)==0){
				output << "Case #"<<(i+1)<<": Neither\n";
			}else{
				if(maxr==1){
					output << "Case #"<<(i+1)<<": Red\n";
				}else{
					output << "Case #"<<(i+1)<<": Blue\n";
				}
			}
		}
		/*char respon;
		cout << maxr << maxb << " right?";
		cin>>respon;
		if(respon=='n'){
			return 0;
		}*/
	}
	return 0;
}