#include<fstream>
#include<string>
#include<set>
#include<cassert>
using namespace std;

int main(){
	ifstream is("2010Round1B\\A.txt");	
	ofstream os("2010Round1B\\Ao.txt");
	int C;
	while(is>>C)
	{
		for (int i = 1; i <= C; ++i)
		{
			int N, M;  is>>N>>M;
			os<<"Case #"<<i<<": ";
			set<string> dic;
			int res = 0;
			string input;
			for (int n = 0; n < N; ++n){
				is>>input;
				dic.insert(input);
			}

			for (int m = 0; m < M; ++m){
				is>>input;
				assert (input[input.size()-1] != '/') ;
				if (dic.find(input) != dic.end()) continue;
				dic.insert(input);
				++res;
				for (int x = 1; x < input.size(); ++x)
					if (input[x]=='/'){
						string temp(input.begin(), input.begin()+x);
						if (dic.find(temp) == dic.end()){
							++res;
							dic.insert(temp);
						}
					}
			}

			os<<res<<endl;
		}
	}

}